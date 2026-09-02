# Predicción de Precios de Viviendas en California

**Problema:** Predecir precios de viviendas en California basándose en características del vecindario y ubicación.

## Datos
- **Fuente:** Censo de California 1990
- **Tamaño:** 56,244 observaciones, 10 variables
- **Dataset incluido:** `housing.csv` (~1.4 MB)
- **Características:** 
  - Geográficas: longitud, latitud, proximidad al océano
  - Del vecindario: edad mediana de viviendas, población, hogares
  - Económicas: ingreso mediano del hogar
  - Estructurales: total de habitaciones, dormitorios

## Enfoque

**Feature Engineering clave:**
- Normalización por hogar: habitaciones/hogar, dormitorios/hogar, población/hogar
- Ingreso mediano identificado como predictor más fuerte (R² = 0.6)
- Proximidad al océano codificada como variable categórica

**Modelos evaluados:**
1. Decision Tree Regressor
2. Random Forest Regressor (mejor desempeño)
3. GridSearchCV para optimización de hiperparámetros

## Resultados

**Random Forest (modelo final):**
- **R² Score:** 75.7% de varianza explicada
- **Mean Absolute Error:** 16.9% del valor promedio de vivienda
- **Predictores principales:** Ingreso mediano, proximidad al océano, ubicación geográfica

**Insight clave:** La normalización por hogar fue crítica. Los totales brutos (habitaciones, población) eran engañosos debido a tamaños de bloque variables.

## Tecnologías

- Python, Pandas, NumPy
- Scikit-learn (Random Forest, GridSearchCV)
- Matplotlib, Seaborn (visualización)

## Cómo ejecutar

```bash
# Dataset incluido en el repositorio
pip install pandas numpy scikit-learn matplotlib seaborn

jupyter notebook "California House Price Prediction.ipynb"
```

Ver: [`California House Price Prediction.ipynb`](./California%20House%20Price%20Prediction.ipynb)

## Aplicaciones

- Valuación de propiedades para mercado inmobiliario
- Análisis de mercado para inversionistas
- Planificación urbana basada en patrones de precios
