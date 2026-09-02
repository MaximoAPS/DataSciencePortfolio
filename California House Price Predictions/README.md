# California House Price Predictions

**Problem:** Predict house prices in California based on neighborhood characteristics and location.

## Data
- **Source:** California Census 1990
- **Size:** 56,244 observations, 10 variables
- **Dataset included:** `housing.csv` (~1.4 MB)
- **Features:** 
  - Geographic: longitude, latitude, ocean proximity
  - Neighborhood: median house age, population, households
  - Economic: median household income
  - Structural: total rooms, bedrooms

## Approach

**Key Feature Engineering:**
- Per-household normalization: rooms/household, bedrooms/household, population/household
- Median income identified as strongest predictor (R² = 0.6)
- Ocean proximity encoded as categorical variable

**Models evaluated:**
1. Decision Tree Regressor
2. Random Forest Regressor (best performance)
3. GridSearchCV for hyperparameter optimization

## Results

**Random Forest (final model):**
- **R² Score:** 75.7% of variance explained
- **Mean Absolute Error:** 16.9% of average house value
- **Main predictors:** Median income, ocean proximity, geographic location

**Key insight:** Per-household normalization was critical. Raw totals (rooms, population) were misleading due to variable block sizes.

## Technologies

- Python, Pandas, NumPy
- Scikit-learn (Random Forest, GridSearchCV)
- Matplotlib, Seaborn (visualization)

## How to Run

```bash
# Dataset included in repository
pip install pandas numpy scikit-learn matplotlib seaborn

jupyter notebook "California House Price Prediction.ipynb"
```

See: [`California House Price Prediction.ipynb`](./California%20House%20Price%20Prediction.ipynb)

## Applications

- Property valuation for real estate market
- Market analysis for investors
- Urban planning based on price patterns
