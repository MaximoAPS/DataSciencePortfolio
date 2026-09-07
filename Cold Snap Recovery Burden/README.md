# Cold Snap Recovery Burden

**Problem:** Predict infrastructure recovery burden following extreme cold weather events, measured as recovery resource requirements by location and timeframe.

## Data
- **Source:** Weather and infrastructure challenge dataset
- **Size:** 538 samples (train), 538 samples (test)
- **Features:** Weather variables (temperature, humidity, dewpoint, solar radiation), temporal indicators
- **Note:** Test cities have zero location overlap with training (fully out-of-distribution)

## Approach

**LightGBM regression** with careful feature engineering for out-of-distribution generalization.

**Key insights:**
- Target spans 170-11,866 with moderate skew (1.56)
- Raw MAE loss outperforms log-transformed target
- `prefix_hours` is critical conditioning feature (median: 12h=1442, 24h=1048, 36h=501)
- Most predictive features: `relhum_min` (r=0.25), `dew_dry_spread` (r=-0.21), `ghi_deficit`

**Validation strategy:**
- Cross-validation accounting for OOD test distribution
- Focus on robust features that generalize across locations

## Results

- **Metric:** Mean Absolute Error (MAE)
- **Challenge:** Fully OOD test set (no location overlap with train)
- **Approach:** LightGBM with weather-based features robust to location shift

## Technologies

- Python, Pandas, NumPy
- LightGBM
- Scikit-learn (preprocessing)
- Matplotlib (visualization)

## How to Run

```bash
jupyter notebook "Cold Snap Recovery Burden.ipynb"
```

Dataset included in repository.
