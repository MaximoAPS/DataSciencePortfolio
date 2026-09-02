# Predicción de Trayectorias de Jugadores NFL

**Problema:** Predecir posiciones futuras de jugadores en el campo durante jugadas de fútbol americano para análisis estratégico y visualización.

## Datos
- **Fuente:** NFL Big Data Bowl 2026 (tracking data oficial de la NFL)
- **Tamaño:** Millones de registros de tracking de 18 semanas de la temporada 2023
- **Características:** Posición (x, y), velocidad, aceleración, dirección, orientación, rol del jugador, contexto de la jugada
- **Nota:** Dataset multi-GB, **NO incluido en este repositorio**

## Enfoque

**Arquitectura de dos etapas:**

1. **Predictor de Punto Final (Stage 1)**
   - Predice posición final desde el estado inicial (frame 0)
   - CatBoost con 123 características ingenieradas
   - GroupKFold cross-validation para evitar data leakage entre jugadas

2. **Corrector de Trayectoria (Stage 2)**
   - Refina predicciones de movimiento rectilíneo uniforme (MRU)
   - Correcciones frame-by-frame basadas en residuales
   - Asegura trayectorias físicamente plausibles

**Feature Engineering:**
- Dinámicas temporales: lag features, cambios de velocidad
- Relaciones espaciales: distancias a jugadores cercanos, velocidades relativas
- Contexto de juego: receptor objetivo, posición en el campo

## Resultados

- **RMSE:** 0.98 yardas
- **MAE:** 0.56 yardas
- **Error mediano:** 0.29 yardas
- **85% de predicciones** dentro de 1 yarda de la posición real

**Rendimiento por frame:**
- Frame 1: Error medio 0.14 yardas
- Frame 5: Error medio 0.23 yardas
- Frame 10: Error medio 0.63 yardas

## Tecnologías

- Python, Pandas, NumPy
- CatBoost (gradient boosting)
- Procesamiento paralelo (ThreadPoolExecutor)
- Plotly para visualización

## Cómo ejecutar

⚠️ **Requiere dataset de NFL Big Data Bowl 2026** (varios GB, no incluido)

```bash
# 1. Descargar datos desde Kaggle NFL Big Data Bowl 2026
# 2. Colocar CSVs en carpeta data/
# 3. Instalar dependencias
pip install pandas numpy catboost plotly scikit-learn

# 4. Abrir y ejecutar notebook
jupyter notebook "NFL Big Data Bowl.ipynb"
```

Ver: [`NFL Big Data Bowl.ipynb`](./NFL%20Big%20Data%20Bowl.ipynb)

## Limitaciones

- Modelo predice basado en estado inicial; no captura cambios dinámicos durante la jugada
- Contexto adicional (down, distancia, tiempo restante) podría mejorar predicciones
- No modela características específicas de jugadores individuales

