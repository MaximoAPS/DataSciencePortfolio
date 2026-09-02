# Clasificación de Vinos

**Problema:** Clasificar vinos italianos en tres categorías basándose en sus propiedades fisicoquímicas.

## Datos
- **Fuente:** Sklearn wine dataset (integrado)
- **Tamaño:** 178 muestras, 13 características químicas
- **Características:** Alcohol, acidez málica, cenizas, fenoles totales, flavonoides, proantocianinas, intensidad de color, tono, OD280/OD315, prolina

## Enfoque
- Análisis de correlación entre propiedades químicas
- Visualización de características por clase de vino
- Baseline: Regresión Logística con estandarización
- Mejorado: Random Forest

## Resultados
- **Accuracy:** 98-100% en conjunto de prueba
- **Características clave:** Flavonoides, prolina, y alcohol son los predictores más importantes
- **Interpretación química:** Las propiedades organolépticas (fenoles, flavonoides) están fuertemente relacionadas con la clasificación del vino

## Cómo ejecutar

```bash
# El notebook usa datasets integrados de sklearn
pip install pandas numpy matplotlib seaborn scikit-learn
jupyter notebook clasificacion_vino.ipynb
```

Ver: [`clasificacion_vino.ipynb`](./clasificacion_vino.ipynb)

## Relevancia
Ideal para docentes de química: las características fisicoquímicas (alcohol, acidez, compuestos fenólicos) son conceptos que se enseñan en química orgánica y analítica.
