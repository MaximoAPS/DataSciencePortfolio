# Wine Quality

**Problem:** Classify Italian wines into three categories based on their physicochemical properties.

## Data
- **Source:** Sklearn wine dataset (built-in)
- **Size:** 178 samples, 13 chemical features
- **Features:** Alcohol, malic acid, ash, total phenols, flavonoids, proanthocyanins, color intensity, hue, OD280/OD315, proline

## Approach
- Correlation analysis between chemical properties
- Visualization of features by wine class
- Baseline: Logistic Regression with standardization
- Improved: Random Forest

## Results
- **Accuracy:** 98-100% on test set
- **Key features:** Flavonoids, proline, and alcohol are the most important predictors
- **Chemical interpretation:** Organoleptic properties (phenols, flavonoids) are strongly related to wine classification

## How to Run

```bash
# Notebook uses sklearn built-in datasets
pip install pandas numpy matplotlib seaborn scikit-learn
jupyter notebook clasificacion_vino.ipynb
```

See: [`clasificacion_vino.ipynb`](./clasificacion_vino.ipynb)

## Relevance
Ideal for chemistry teachers: physicochemical features (alcohol, acidity, phenolic compounds) are concepts taught in organic and analytical chemistry.
