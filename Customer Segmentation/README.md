# Segmentación de Clientes con K-Means

**Problema:** Identificar segmentos de clientes con comportamientos de compra similares para estrategias de marketing personalizadas.

## Datos
- **Fuente:** Dataset Mall Customers (incluido: `mall_customers.csv`)
- **Tamaño:** 200 clientes, 5 variables
- **Características:** Edad, género, ingresos anuales, puntuación de gasto

## Enfoque
- Análisis exploratorio de patrones de gasto e ingresos
- Método del codo para determinar número óptimo de clusters
- Baseline: K-means con k=3
- Mejorado: K-means con k=5 (óptimo según silhouette score)

## Resultados
- **Clusters identificados:** 5 segmentos distintos
- **Silhouette Score:** ~0.50
- **Segmentos típicos:** Clientes de alto/bajo ingreso con alto/bajo gasto, permitiendo estrategias diferenciadas

## Cómo ejecutar

```bash
# Dataset incluido en el repositorio
pip install pandas numpy matplotlib seaborn scikit-learn
jupyter notebook segmentacion_kmeans.ipynb
```

Ver: [`segmentacion_kmeans.ipynb`](./segmentacion_kmeans.ipynb)
