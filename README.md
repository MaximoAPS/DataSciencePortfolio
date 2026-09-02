# Data Science Portfolio

> **Work in progress** — selected notebooks, not a finished product.

This repository contains selected data science projects demonstrating practical applications of machine learning and data analysis.

## Projects

### 1. [California House Price Prediction](./California%20House%20Price%20Predictions)
Predicts house prices in California using 1990 census data with feature engineering and machine learning.

- **Technologies:** Python, Pandas, Scikit-learn, Matplotlib, Seaborn, Random Forest, GridSearchCV
- **Results:** Random Forest achieved 75.7% R² score with 16.9% Mean Absolute Error
- **Dataset:** 1.4 MB CSV included in repository

### 2. [NFL Big Data Bowl 2026 - Player Trajectory Prediction](./Second%20Proyect)
Player trajectory prediction for NFL games using a two-stage machine learning pipeline.

- **Technologies:** Python, Pandas, NumPy, CatBoost, Plotly, GroupKFold Cross-Validation
- **Results:** RMSE of 0.98 yards and MAE of 0.56 yards, with 85% of predictions within 1 yard of actual positions
- **Note:** Dataset is multi-GB, not included in repository

### 3. [Clasificación de Pingüinos](./penguins_clasificacion)
Species classification using physical measurements (bill, flipper, body mass) from Palmer Penguins dataset.

- **Technologies:** Python, Seaborn, Scikit-learn, Logistic Regression, Random Forest
- **Results:** 98% accuracy distinguishing three penguin species
- **Dataset:** Built-in seaborn dataset (344 observations)

### 4. [Segmentación de Clientes con K-Means](./segmentacion_clientes)
Customer segmentation using K-means clustering on income and spending patterns.

- **Technologies:** Python, Scikit-learn, K-Means, Silhouette Analysis
- **Results:** 5 distinct customer segments identified (Silhouette Score ~0.50)
- **Dataset:** 200-row CSV included in repository

### 5. [Clasificación de Calidad de Vino](./vino_calidad)
Wine classification based on physicochemical properties (alcohol, phenols, flavonoids, acidity).

- **Technologies:** Python, Scikit-learn, Random Forest, Logistic Regression
- **Results:** 98-100% accuracy on three wine classes
- **Dataset:** Sklearn wine dataset (178 samples, 13 chemical features)

## License

This project is licensed under the [MIT License](LICENSE).