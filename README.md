# Portfolio de Ciencia de Datos

> **English:** Data Science & Machine Learning portfolio by Maximo Pere. Python-focused projects spanning regression, clustering, classification, and deep learning with audio. Buenos Aires, Argentina.

**Máximo Pere** • Analista de Datos & Machine Learning • Buenos Aires, Argentina

Proyectos de ciencia de datos aplicada: desde machine learning clásico (regresión, clustering, clasificación) hasta deep learning con audio. Python, scikit-learn, PyTorch.

📫 **Contacto:** [LinkedIn](https://linkedin.com/in/maximopere) • [GitHub](https://github.com/MaximoAPS)

---

## 🚀 Featured Projects

### 1. [Guitar Sound Classifier](./Guitar%20Sound%20Classifier)
Clasificador binario que distingue entre guitarras acústicas y eléctricas mediante procesamiento de audio y redes neuronales convolucionales.

- **Problema:** Clasificar clips de audio de guitarra por tipo de instrumento
- **Método:** Extracción de espectrogramas (STFT, Mel, MFCC) → imagen 3 canales → CNN de 2 capas
- **Stack:** PyTorch, torchaudio, CNN
- **Dataset:** 12,600 clips de audio (~0.29s cada uno, **no incluido**: varios GB)
- **Nota:** Primer proyecto de deep learning con PyTorch

[Ver código →](./Guitar%20Sound%20Classifier)

---

### 2. [Wine Quality](./Wine%20Quality)
Clasificación de vinos italianos basándose en análisis fisicoquímico.

- **Problema:** Clasificar 3 tipos de vino según características químicas
- **Método:** Análisis de 13 propiedades (alcohol, fenoles, flavonoides, acidez) → Random Forest
- **Resultado:** 98-100% accuracy
- **Dataset:** 178 muestras (sklearn integrado)
- **Relevancia:** Ideal para docencia en química — propiedades organolépticas y analíticas

[Ver notebook →](./Wine%20Quality)

---

### 3. [Customer Segmentation](./Customer%20Segmentation)
Identificación de segmentos de clientes para estrategias de marketing personalizadas.

- **Problema:** Agrupar clientes según patrones de ingreso y gasto
- **Método:** K-means con método del codo y análisis silhouette
- **Resultado:** 5 segmentos identificados (Silhouette Score ~0.50)
- **Dataset:** 200 clientes (CSV incluido)

[Ver notebook →](./Customer%20Segmentation)

---

### 4. [California House Price Predictions](./California%20House%20Price%20Predictions)
Predicción de precios inmobiliarios en California mediante feature engineering y Random Forest.

- **Problema:** Predecir precio de viviendas según ubicación y características del vecindario
- **Método:** Feature engineering (normalización por hogar) → Random Forest con GridSearchCV
- **Resultado:** R² = 75.7%, MAE = 16.9%
- **Dataset:** Censo California 1990 (56K observaciones, CSV incluido ~1.4 MB)

[Ver notebook →](./California%20House%20Price%20Predictions)

---

### 5. [NFL Player Trajectory](./NFL%20Player%20Trajectory)
Predicción de movimiento de jugadores en fútbol americano mediante pipeline de dos etapas.

- **Problema:** Predecir posiciones futuras de jugadores durante jugadas
- **Método:** Pipeline de 2 etapas (CatBoost endpoint predictor + corrector de trayectoria) con 123 características
- **Resultado:** RMSE = 0.98 yardas, 85% de predicciones dentro de 1 yarda
- **Dataset:** NFL Big Data Bowl 2026 (**no incluido**: varios GB de tracking data)

[Ver notebook →](./NFL%20Player%20Trajectory)

---

### 6. [Penguin Classification](./Penguin%20Classification)
Clasificación de especies de pingüinos — proyecto educativo con dataset pequeño.

- **Método:** Regresión Logística + Random Forest
- **Resultado:** ~98% accuracy
- **Dataset:** Palmer Penguins (344 obs, seaborn integrado)

[Ver notebook →](./Penguin%20Classification)

---

## 🛠️ Tecnologías

**Lenguajes:** Python

**Machine Learning:** scikit-learn, CatBoost, PyTorch

**Procesamiento de datos:** Pandas, NumPy

**Visualización:** Matplotlib, Seaborn, Plotly

**Audio:** torchaudio, STFT, Mel Spectrograms, MFCC

**Técnicas:** Regresión, Clustering (K-Means), Clasificación (Random Forest, Logistic Regression), CNN, Feature Engineering, Cross-Validation

---

## 📦 Instalación y Uso

### Opción 1: Instalar todas las dependencias
```bash
pip install -r requirements.txt
```

### Opción 2: Por proyecto individual
Cada carpeta de proyecto tiene su propio README con instrucciones específicas.

### Notebooks ejecutables
La mayoría de notebooks se pueden ejecutar sin descarga adicional (usan datasets integrados o incluidos). Excepciones:
- **NFL Player Trajectory:** Requiere descargar dataset multi-GB de Kaggle NFL Big Data Bowl 2026
- **Guitar Sound Classifier:** Requiere proporcionar archivos .wav propios

---

## ⚠️ Datasets NO Incluidos

Por tamaño, los siguientes datasets **no están en este repositorio**:

- **NFL Player Trajectory:** Tracking data de NFL (~varios GB) — disponible en Kaggle NFL Big Data Bowl 2026
- **Guitar Sound Classifier:** 12,600 clips de audio .wav (~varios GB)
- **CAFA (Protein Function Prediction):** Proyecto separado en Google Colab, no migrado aquí por tamaño de datasets (UniProt, GO ontology)

---

## 📝 Estado del Portfolio

> **Trabajo en progreso** — colección de proyectos seleccionados, no un producto terminado.

Este portfolio muestra proyectos de complejidad incremental:
- Proyectos educativos pequeños (Penguin Classification, Wine Quality, Customer Segmentation)
- Proyectos de análisis sustancial (California House Price Predictions, NFL Player Trajectory)
- Incursión en deep learning (Guitar Sound Classifier con PyTorch)

**Limitaciones conocidas:**
- Algunos proyectos usan datasets históricos (ej: censo 1990)
- Modelos enfocados en demostración de técnicas, no optimización exhaustiva
- Guitar Sound Classifier: primer proyecto de DL, tiene espacio para mejoras arquitecturales

---

## 📬 Contacto

**Máximo Pere**
- LinkedIn: [linkedin.com/in/maximopere](https://linkedin.com/in/maximopere)
- GitHub: [github.com/MaximoAPS](https://github.com/MaximoAPS)
- Ubicación: Buenos Aires, Argentina

---

## 📄 Licencia

Este proyecto está licenciado bajo [MIT License](LICENSE).
