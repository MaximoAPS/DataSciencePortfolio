# Plasma Etching Spatial Uniformity Prediction

**Problem:** Predict spatial uniformity patterns in semiconductor plasma etching processes to optimize manufacturing quality control.

## Data
- **Source:** Semiconductor manufacturing challenge dataset
- **Size:** 12,000 samples (train), 12,000 samples (test)
- **Features:** 8 process parameters
  - RF power (W)
  - Chamber pressure (mTorr)
  - Gas flows: CF4, O2, Ar (sccm)
  - Substrate temperature (°C)
  - Electrode gap (mm)
  - Rotation speed (RPM)
- **Target:** 49 zones (7×7 wafer grid), predicting etching uniformity per zone

## Approach

**PyTorch neural network** with custom loss function for spatial manufacturing constraints.

**Architecture:**
- Multi-output regression (49 zones)
- K-Fold cross-validation
- StandardScaler preprocessing
- Adam optimizer

**Feature engineering:**
- Gas flow ratios (CF4/O2, CF4/Ar, O2/Ar)
- Process physics features (power/pressure ratio, plasma density proxy)
- Total gas flow and individual gas fractions
- Temperature normalization
- Interaction terms (power × gap, CF4 × pressure)

**Custom metric:** ZWUE (Zone-Weighted Uniformity Error)
- Edge zones weighted 5× higher than center zones
- Asymmetric penalty (4× for under-etching vs over-etching)
- Exponential error transformation for large deviations

## Results

- **Metric:** Zone-Weighted Uniformity Error (ZWUE)
- **Method:** PyTorch neural network with domain-specific loss
- **Implementation:** Python script (`solution.py`) rather than notebook

## Technologies

- Python, Pandas, NumPy
- PyTorch (neural networks)
- Scikit-learn (StandardScaler, KFold)
- Custom physics-motivated features

## How to Run

```bash
python solution.py
```

**Note:** This project uses a Python script rather than a Jupyter notebook.

Dataset included in repository.
