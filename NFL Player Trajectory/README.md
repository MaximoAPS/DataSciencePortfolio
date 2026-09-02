# NFL Player Trajectory

**Problem:** Predict future player positions on the field during American football plays for strategic analysis and visualization.

## Data
- **Source:** NFL Big Data Bowl 2026 (official NFL tracking data)
- **Size:** Millions of tracking records from 18 weeks of the 2023 season
- **Features:** Position (x, y), speed, acceleration, direction, orientation, player role, play context
- **Note:** Multi-GB dataset, **NOT included in this repository**

## Approach

**Two-stage architecture:**

1. **Endpoint Predictor (Stage 1)**
   - Predicts final position from initial state (frame 0)
   - CatBoost with 123 engineered features
   - GroupKFold cross-validation to prevent data leakage between plays

2. **Trajectory Corrector (Stage 2)**
   - Refines uniform rectilinear motion (MRU) predictions
   - Frame-by-frame corrections based on residuals
   - Ensures physically plausible trajectories

**Feature Engineering:**
- Temporal dynamics: lag features, velocity changes
- Spatial relationships: distances to nearby players, relative velocities
- Game context: target receiver, field position

## Results

- **RMSE:** 0.98 yards
- **MAE:** 0.56 yards
- **Median error:** 0.29 yards
- **85% of predictions** within 1 yard of actual position

**Performance by frame:**
- Frame 1: Mean error 0.14 yards
- Frame 5: Mean error 0.23 yards
- Frame 10: Mean error 0.63 yards

## Technologies

- Python, Pandas, NumPy
- CatBoost (gradient boosting)
- Parallel processing (ThreadPoolExecutor)
- Plotly for visualization

## How to Run

⚠️ **Requires NFL Big Data Bowl 2026 dataset** (several GB, not included)

```bash
# 1. Download data from Kaggle NFL Big Data Bowl 2026
# 2. Place CSVs in data/ folder
# 3. Install dependencies
pip install pandas numpy catboost plotly scikit-learn

# 4. Open and run notebook
jupyter notebook "NFL Big Data Bowl.ipynb"
```

See: [`NFL Big Data Bowl.ipynb`](./NFL%20Big%20Data%20Bowl.ipynb)

## Limitations

- Model predicts based on initial state; doesn't capture dynamic changes during play
- Additional context (down, distance, time remaining) could improve predictions
- Doesn't model player-specific characteristics
