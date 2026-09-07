# Spatiotemporal Mobility Energy Load Modeling

**Problem:** Model energy load patterns from mobility data across space and time for urban energy planning.

## Data
- **Source:** Urban mobility challenge dataset
- **Size:** 2,184 samples (train), 2,184 samples (test)
- **Features:** Mobility patterns, temporal indicators, seasonal regime codes, geographic data
- **Challenge:** `seasonal_regime_code=3` appears in test but not in train (fully OOD)

## Approach

**Regression modeling** with careful handling of out-of-distribution categorical features.

**Key findings from exploratory analysis:**
- `seasonal_regime_code=3` in test is fully out-of-distribution (train only has {0, 1, 2})
- Regime is orthogonal to continuous features (R²=0.037 from PC1)
  - Cannot be reliably inferred from other variables
- Regime carries ~112 RMSE of independent signal, but unvalidatable for test regime=3
- PC1 of continuous features explains 98.8% of their joint variance

**Strategy:**
- Focus on robust continuous features that generalize
- Handle OOD regime with careful fallback or exclusion
- Principal component analysis for dimensionality insights
- Conservative prediction for unseen regime values

## Results

- **Metric:** Root Mean Squared Error (RMSE)
- **Challenge:** Out-of-distribution seasonal regime in test set
- **Insight:** PC1 captures 98.8% of continuous feature variance, but regime adds orthogonal signal

## Technologies

- Python, Pandas, NumPy
- Scikit-learn (PCA, regression)
- Matplotlib, Seaborn (visualization)

## How to Run

```bash
jupyter notebook "Spatiotemporal Mobility Energy Load Modeling.ipynb"
```

Dataset included in repository.

## Applications

- Urban energy demand forecasting
- Smart city planning
- Renewable energy integration
- Peak load management
