import multiprocessing, warnings
import numpy as np
import pandas as pd
from pathlib import Path
from tqdm import tqdm

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore")
SEED = 42
np.random.seed(SEED)
torch.manual_seed(SEED)

# ════════════════════════════════════════════════════════════════════════
# RUTAS
# ════════════════════════════════════════════════════════════════════════
BASE_DIR    = Path(__file__).parent
DATA_DIR    = BASE_DIR / "dataset" / "public"
OUTPUT_DIR  = BASE_DIR / "working"
TRAIN_PATH  = DATA_DIR / "train.csv"
TEST_PATH   = DATA_DIR / "test.csv"
SUBMIT_PATH = OUTPUT_DIR / "submission.csv"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# ════════════════════════════════════════════════════════════════════════
# CONSTANTES
# ════════════════════════════════════════════════════════════════════════
FEATURES = [
    "rf_power_w", "chamber_pressure_mtorr", "cf4_flow_sccm",
    "o2_flow_sccm", "ar_flow_sccm", "substrate_temp_c",
    "electrode_gap_mm", "rotation_rpm",
]
ZONE_COLS = [f"z_{r}_{c}" for r in range(1, 8) for c in range(1, 8)]

def get_zone_weight(col):
    _, r, c = col.split("_")
    return 5.0 if (abs(int(r) - 4) >= 3 or abs(int(c) - 4) >= 3) else 1.0

ZONE_WEIGHTS = np.array([get_zone_weight(c) for c in ZONE_COLS], dtype=np.float32)

# ════════════════════════════════════════════════════════════════════════
# MÉTRICA
# ════════════════════════════════════════════════════════════════════════
def zwue_score(y_true, y_pred):
    rmses = []
    for j in range(49):
        err      = y_pred[:, j] - y_true[:, j]
        exp_err  = np.expm1(np.abs(err) / 50) + np.abs(err)
        asym_err = np.where(err < 0, 4.0 * exp_err, exp_err)
        rmses.append(np.sqrt(np.mean(asym_err ** 2)))
    return float(np.dot(ZONE_WEIGHTS, rmses) / ZONE_WEIGHTS.sum())

# ════════════════════════════════════════════════════════════════════════
# FEATURE ENGINEERING
# ════════════════════════════════════════════════════════════════════════
def engineer_features(df):
    df = df.copy()
    df["cf4_o2_ratio"]         = df["cf4_flow_sccm"] / (df["o2_flow_sccm"] + 1e-3)
    df["cf4_ar_ratio"]         = df["cf4_flow_sccm"] / (df["ar_flow_sccm"] + 1e-3)
    df["o2_ar_ratio"]          = df["o2_flow_sccm"]  / (df["ar_flow_sccm"] + 1e-3)
    df["total_gas"]            = df["cf4_flow_sccm"] + df["o2_flow_sccm"] + df["ar_flow_sccm"]
    df["cf4_fraction"]         = df["cf4_flow_sccm"] / (df["total_gas"] + 1e-3)
    df["o2_fraction"]          = df["o2_flow_sccm"]  / (df["total_gas"] + 1e-3)
    df["ar_fraction"]          = df["ar_flow_sccm"]  / (df["total_gas"] + 1e-3)
    df["power_pressure_ratio"] = df["rf_power_w"]    / (df["chamber_pressure_mtorr"] + 1e-3)
    df["power_per_gap"]        = df["rf_power_w"]    / (df["electrode_gap_mm"] + 1e-3)
    df["pressure_x_gap"]       = df["chamber_pressure_mtorr"] * df["electrode_gap_mm"]
    df["plasma_density_proxy"] = df["rf_power_w"] / (df["chamber_pressure_mtorr"] * df["electrode_gap_mm"] + 1e-3)
    df["is_rotating"]          = (df["rotation_rpm"] > 0).astype(float)
    df["log_rpm"]              = np.log1p(df["rotation_rpm"])
    df["temp_normalized"]      = (df["substrate_temp_c"] - 10) / 70.0
    df["power_x_gap"]          = df["rf_power_w"]       * df["electrode_gap_mm"]
    df["power_x_press"]        = df["rf_power_w"]       * df["chamber_pressure_mtorr"]
    df["cf4_x_power"]          = df["cf4_flow_sccm"]    * df["rf_power_w"]
    df["cf4_x_pressure"]       = df["cf4_flow_sccm"]    * df["chamber_pressure_mtorr"]
    df["o2_x_power"]           = df["o2_flow_sccm"]     * df["rf_power_w"]
    df["temp_x_power"]         = df["substrate_temp_c"] * df["rf_power_w"]
    df["log_power"]            = np.log(df["rf_power_w"])
    df["log_pressure"]         = np.log(df["chamber_pressure_mtorr"] + 1e-3)
    df["log_cf4"]              = np.log(df["cf4_flow_sccm"] + 1e-3)
    df["log_total_gas"]        = np.log(df["total_gas"] + 1e-3)
    return df

# ════════════════════════════════════════════════════════════════════════
# CARGA DE DATOS
# ════════════════════════════════════════════════════════════════════════
def load_data():
    print("📂 Cargando datos...")
    train = pd.read_csv(TRAIN_PATH)
    test  = pd.read_csv(TEST_PATH)
    print(f"   Train: {train.shape}  |  Test: {test.shape}")

    y_train  = train[ZONE_COLS].values.astype(np.float32)
    df_train = engineer_features(train[FEATURES])
    df_test  = engineer_features(test[FEATURES])
    test_ids = test["id"].values

    print(f"   Features: {df_train.shape[1]}")
    return df_train, y_train, df_test, test_ids

# ════════════════════════════════════════════════════════════════════════
# ARQUITECTURA
# ════════════════════════════════════════════════════════════════════════
class ResBlock(nn.Module):
    def __init__(self, dim, dropout):
        super().__init__()
        self.block = nn.Sequential(
            nn.Linear(dim, dim),
            nn.BatchNorm1d(dim),
            nn.SiLU(),
            nn.Dropout(dropout),
            nn.Linear(dim, dim),
            nn.BatchNorm1d(dim),
        )
        self.act = nn.SiLU()

    def forward(self, x):
        return self.act(x + self.block(x))


class EtchNet(nn.Module):
    def __init__(self, n_features, n_zones=49, hidden=256, n_blocks=4, dropout=0.15):
        super().__init__()
        self.input_block = nn.Sequential(
            nn.Linear(n_features, hidden),
            nn.BatchNorm1d(hidden),
            nn.SiLU(),
        )
        self.res_blocks = nn.ModuleList([
            ResBlock(hidden, dropout) for _ in range(n_blocks)
        ])
        self.head = nn.Sequential(
            nn.Linear(hidden, hidden // 2),
            nn.SiLU(),
            nn.Linear(hidden // 2, n_zones),
            nn.Softplus(),
        )

    def forward(self, x):
        x = self.input_block(x)
        for block in self.res_blocks:
            x = block(x)
        return self.head(x)


class AsymmetricZWUELoss(nn.Module):
    def __init__(self, zone_weights):
        super().__init__()
        self.register_buffer("w", torch.tensor(zone_weights, dtype=torch.float32))

    def forward(self, pred, target):
        err      = pred - target
        abs_err  = err.abs()
        exp_err  = torch.expm1(abs_err / 50) + abs_err
        asym_err = torch.where(err < 0, 4.0 * exp_err, exp_err)
        zone_mse = (asym_err ** 2).mean(dim=0)
        return (self.w * zone_mse).sum() / self.w.sum()

# ════════════════════════════════════════════════════════════════════════
# ENTRENAMIENTO CON KFOLD
# ════════════════════════════════════════════════════════════════════════
def train_nn_cv(df_train, y_train, df_test, n_folds=5,
                epochs=150, batch_size=512, lr=1e-3):

    scaler   = StandardScaler()
    X_all    = scaler.fit_transform(df_train.values).astype(np.float32)
    X_test_s = scaler.transform(df_test.values).astype(np.float32)

    kf          = KFold(n_splits=n_folds, shuffle=True, random_state=SEED)
    oof_preds   = np.zeros_like(y_train, dtype=np.float64)
    test_preds  = np.zeros((len(df_test), 49), dtype=np.float64)
    fold_scores = []
    criterion   = AsymmetricZWUELoss(ZONE_WEIGHTS).to(DEVICE)

    for fold, (trn_idx, val_idx) in enumerate(kf.split(X_all)):
        X_trn_t  = torch.tensor(X_all[trn_idx]).to(DEVICE)
        X_val_t  = torch.tensor(X_all[val_idx]).to(DEVICE)
        y_trn_t  = torch.tensor(y_train[trn_idx]).to(DEVICE)
        y_val_np = y_train[val_idx]
        X_test_t = torch.tensor(X_test_s).to(DEVICE)

        loader = DataLoader(
            TensorDataset(X_trn_t, y_trn_t),
            batch_size=batch_size, shuffle=True
        )

        model = EtchNet(n_features=X_all.shape[1]).to(DEVICE)
        opt   = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)
        sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=epochs, eta_min=1e-5)

        best_zwue  = float("inf")
        best_state = None
        patience   = 0

        epoch_bar = tqdm(range(epochs),
                         desc=f"  [NN] Fold {fold+1}/{n_folds}",
                         unit="ep", colour="magenta", leave=True)

        for epoch in epoch_bar:
            model.train()
            for xb, yb in loader:
                opt.zero_grad()
                loss = criterion(model(xb), yb)
                loss.backward()
                nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                opt.step()
            sched.step()

            if (epoch + 1) % 5 == 0:
                model.eval()
                with torch.no_grad():
                    val_pred = model(X_val_t).cpu().numpy()
                val_zwue = zwue_score(y_val_np, val_pred)
                epoch_bar.set_postfix({"val_ZWUE": f"{val_zwue:.4f}"})

                if val_zwue < best_zwue:
                    best_zwue  = val_zwue
                    best_state = {k: v.clone() for k, v in model.state_dict().items()}
                    patience   = 0
                else:
                    patience += 1
                    if patience >= 6:
                        tqdm.write(f"    Early stop en epoch {epoch+1}")
                        break

        model.load_state_dict(best_state)
        model.eval()
        with torch.no_grad():
            oof_pred  = model(X_val_t).cpu().numpy()
            test_pred = model(X_test_t).cpu().numpy()

        fold_zwue = zwue_score(y_val_np, oof_pred)
        fold_scores.append(fold_zwue)
        tqdm.write(f"     Fold {fold+1} ZWUE: {fold_zwue:.4f}  (best val: {best_zwue:.4f})")

        oof_preds[val_idx] = oof_pred
        test_preds        += test_pred / n_folds

    cv_zwue = zwue_score(y_train, oof_preds)
    print(f"\n  ✅ NN CV ZWUE: {cv_zwue:.4f}  "
          f"(folds: {[f'{s:.3f}' for s in fold_scores]})\n")
    return test_preds, cv_zwue

# ════════════════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════════════════
def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print("=" * 55)
    print("  ICP Etcher — Etch Rate Prediction  [Solo NN]")
    print(f"  Device: {DEVICE}")
    print("=" * 55)

    df_train, y_train, df_test, test_ids = load_data()

    print("\n🧠 Entrenando Red Neuronal (5-Fold CV)...")
    nn_preds, nn_zwue = train_nn_cv(
        df_train, y_train, df_test,
        n_folds=5, epochs=150, batch_size=512, lr=1e-3,
    )

    # Bias asimétrico +0.5%
    final = np.clip(nn_preds * 1.005, 0.01, None)

    submission = pd.DataFrame(final, columns=ZONE_COLS)
    submission.insert(0, "id", test_ids)
    submission.to_csv(SUBMIT_PATH, index=False)

    print(f"✅ {SUBMIT_PATH}")
    print(f"   Shape: {submission.shape}")
    print(f"   Rango: [{final.min():.1f}, {final.max():.1f}] nm/min")
    print(f"   NN CV ZWUE: {nn_zwue:.4f}")
    print("\n🏁 Listo!")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()