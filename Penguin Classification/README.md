# Penguin Classification

**Problem:** Classify three penguin species (Adelie, Chinstrap, Gentoo) based on physical measurements.

## Data
- **Source:** Palmer Penguins dataset (seaborn built-in)
- **Size:** 344 observations, 4 physical features
- **Features:** Bill length and depth, flipper length, body mass

## Approach
- EDA with visualizations by species
- Baseline model: Logistic Regression
- Improved model: Random Forest

## Results
- **Accuracy:** ~98% on test set
- **Key features:** Flipper length and bill length are the most important predictors

## How to Run

```bash
# Notebook uses built-in datasets, no data download required
pip install pandas numpy seaborn matplotlib scikit-learn
jupyter notebook clasificacion_penguins.ipynb
```

See: [`clasificacion_penguins.ipynb`](./clasificacion_penguins.ipynb)
