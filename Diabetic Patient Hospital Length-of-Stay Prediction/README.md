# Diabetic Patient Hospital Length-of-Stay Prediction

**Problem:** Predict hospital length-of-stay for diabetic patients to optimize resource allocation and care planning.

## Data
- **Source:** Clinical challenge dataset
- **Size:** 14,304 patient records (train), 14,304 records (test)
- **Features:** Clinical variables including medications, lab procedures, admission details, readmission status, discharge disposition

## Approach

**Gradient boosting regression** with clinical feature engineering.

**Key insights from exploratory analysis:**
- `num_medications × num_lab_procedures` shows highest single correlation with target (r=0.508)
- `n_meds_changed` exhibits strong non-linear relationship (0 changes=4.4d, 2 changes=6.9d)
- `readmitted` is strong signal (NO=4.4d, >30=5.3d, <30=6.1d)
- `discharge_disposition_id` encodes clinical complexity (long-term care=7.8d vs home discharge)

**Feature engineering:**
- Interaction terms between medication count and lab procedures
- Non-linear transformations of medication changes
- Clinical complexity indicators

## Results

- **Metric:** Root Mean Squared Error (RMSE)
- **Note:** ⚠️ Notebook outputs may need refresh due to XGBoost API change (`early_stopping_rounds` parameter). Current code and analysis are valid; re-execution requires minor API update.

## Technologies

- Python, Pandas, NumPy
- XGBoost (requires API parameter update for re-execution)
- Scikit-learn (preprocessing, validation)
- Matplotlib, Seaborn (visualization)

## How to Run

```bash
jupyter notebook "Diabetic Patient Hospital Length-of-Stay Prediction.ipynb"
```

**Note:** To re-execute, update XGBoost `early_stopping_rounds` parameter to current API.

Dataset included in repository.
