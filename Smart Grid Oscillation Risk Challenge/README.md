# Smart Grid Oscillation Risk Challenge

**Problem:** Predict oscillation risk in smart grid power systems to prevent instability and improve grid reliability.

## Data
- **Source:** Power grid simulation challenge dataset
- **Size:** 30,000 samples (train), 25,000 samples (test)
- **Features:** Grid state variables, bus measurements, power flow data
- **Target:** Multi-bus oscillation risk prediction (6 buses with different criticality weights)

## Approach

**CatBoost ensemble** with custom grid-risk weighted metric and neural network augmentation.

**Architecture:**
1. **CatBoost per bus** with asymmetric bias correction in out-of-fold predictions
2. **Multi-output neural network** with shared trunk for cross-bus learning
3. **Physics-motivated feature engineering** (features already orthogonal, no PCA needed)

**Custom metric: Grid Risk Weighted Error (GRWE)**
- Penalty multiplier of 2.5× when `y_true > Q75 AND y_pred < y_true`
  - Severely under-predicting high-risk states incurs 6.25× cost
- Bus-specific weights: 1.0, 1.2, 1.4, 1.6, 1.8, 2.0
- Asymmetric loss penalizing false negatives on critical events

**Key insight:** Avoiding catastrophic under-prediction on high-risk events is more critical than overall MAE.

## Results

- **Metric:** Grid Risk Weighted Error (GRWE)
- **Method:** CatBoost per bus + NN multi-output with asymmetric loss
- **Focus:** Minimize false negatives on critical high-risk oscillation events

## Technologies

- Python, Pandas, NumPy
- CatBoost
- Neural networks (likely PyTorch/TensorFlow)
- Custom asymmetric loss function

## How to Run

```bash
jupyter notebook "Smart Grid Oscillation Risk Challenge.ipynb"
```

Dataset included in repository.
