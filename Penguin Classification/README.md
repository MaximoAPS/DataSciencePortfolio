# Clasificación de Especies de Pingüinos

**Problema:** Clasificar tres especies de pingüinos (Adelie, Chinstrap, Gentoo) basándose en medidas físicas.

## Datos
- **Fuente:** Palmer Penguins dataset (integrado en seaborn)
- **Tamaño:** 344 observaciones, 4 características físicas
- **Características:** Largo y profundidad del pico, largo de aleta, masa corporal

## Enfoque
- EDA con visualizaciones por especie
- Modelo baseline: Regresión Logística
- Modelo mejorado: Random Forest

## Resultados
- **Accuracy:** ~98% en conjunto de prueba
- **Características clave:** Largo de aleta y largo de pico son los predictores más importantes

## Cómo ejecutar

```bash
# El notebook usa datasets integrados, no requiere descarga de datos
pip install pandas numpy seaborn matplotlib scikit-learn
jupyter notebook clasificacion_penguins.ipynb
```

Ver: [`clasificacion_penguins.ipynb`](./clasificacion_penguins.ipynb)
