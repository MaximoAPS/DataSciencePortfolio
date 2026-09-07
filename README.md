# Data Science Portfolio

**Máximo Pere** • Data Analyst & Machine Learning • Buenos Aires, Argentina

Applied data science projects spanning traditional machine learning (regression, clustering, classification) to deep learning with audio processing. Python, scikit-learn, PyTorch.

📫 **Contact:** [LinkedIn](https://linkedin.com/in/maximopere) • [GitHub](https://github.com/MaximoAPS)

---

## 🚀 Featured Projects

### 1. [Guitar Sound Classifier](./Guitar%20Sound%20Classifier)
Binary classifier that distinguishes acoustic vs electric guitar sounds using audio processing and convolutional neural networks.

- **Problem:** Classify guitar audio clips by instrument type
- **Method:** Extract spectrograms (STFT, Mel, MFCC) → stack as 3-channel image → 2-layer CNN
- **Stack:** PyTorch, torchaudio, CNN
- **Dataset:** 12,600 audio clips (~0.29s each, **not included**: several GB)
- **Note:** First deep learning project with PyTorch

[View code →](./Guitar%20Sound%20Classifier)

---

### 2. [Wine Quality](./Wine%20Quality)
Classification of Italian wines based on physicochemical analysis.

- **Problem:** Classify 3 wine types using chemical properties
- **Method:** Analysis of 13 properties (alcohol, phenols, flavonoids, acidity) → Random Forest
- **Result:** 98-100% accuracy
- **Dataset:** 178 samples (sklearn built-in)
- **Relevance:** Ideal for chemistry teaching — organoleptic and analytical properties

[View notebook →](./Wine%20Quality)

---

### 3. [Customer Segmentation](./Customer%20Segmentation)
Customer segment identification for personalized marketing strategies.

- **Problem:** Group customers by income and spending patterns
- **Method:** K-means with elbow method and silhouette analysis
- **Result:** 5 distinct segments identified (Silhouette Score ~0.50)
- **Dataset:** 200 customers (CSV included)

[View notebook →](./Customer%20Segmentation)

---

### 4. [California House Price Predictions](./California%20House%20Price%20Predictions)
Real estate price prediction in California using feature engineering and Random Forest.

- **Problem:** Predict house prices based on location and neighborhood characteristics
- **Method:** Feature engineering (per-household normalization) → Random Forest with GridSearchCV
- **Result:** R² = 75.7%, MAE = 16.9%
- **Dataset:** California Census 1990 (56K observations, CSV included ~1.4 MB)

[View notebook →](./California%20House%20Price%20Predictions)

---

### 5. [NFL Player Trajectory](./NFL%20Player%20Trajectory)
Player movement prediction in American football using a two-stage machine learning pipeline.

- **Problem:** Predict future player positions during plays
- **Method:** 2-stage pipeline (CatBoost endpoint predictor + trajectory corrector) with 123 engineered features
- **Result:** RMSE = 0.98 yards, 85% of predictions within 1 yard
- **Dataset:** NFL Big Data Bowl 2026 (**not included**: several GB of tracking data)

[View notebook →](./NFL%20Player%20Trajectory)

---

### 6. [Penguin Classification](./Penguin%20Classification)
Penguin species classification — educational project with small dataset.

- **Method:** Logistic Regression + Random Forest
- **Result:** ~98% accuracy
- **Dataset:** Palmer Penguins (344 obs, seaborn built-in)

[View notebook →](./Penguin%20Classification)

---

### 7. [Chemical Mechanism Classification](./Chemical%20Mechanism%20Classification)
Classification of chemical reactions into mechanism types using hybrid rule-based and machine learning approach.

- **Problem:** Classify chemical reactions into 4 mechanism categories from reaction strings
- **Method:** Hybrid architecture combining deterministic parser (89% coverage, 94.3% accuracy) with ML ensemble (LightGBM + CatBoost tiebreaker)
- **Result:** 92.2% out-of-fold accuracy
- **Stack:** Python, LightGBM, CatBoost, pattern matching
- **Dataset:** 3,000+ reactions (CSV included ~7 MB)

[View notebook →](./Chemical%20Mechanism%20Classification)

---

### 8. [Cold Snap Recovery Burden](./Cold%20Snap%20Recovery%20Burden)
Predicting infrastructure recovery burden after extreme cold weather events.

- **Problem:** Predict recovery resource requirements from weather data (fully OOD test cities)
- **Method:** LightGBM with weather-based features (relhum_min, dew_dry_spread, prefix_hours)
- **Stack:** Python, LightGBM, scikit-learn
- **Dataset:** 538 samples (CSV included ~1 MB)
- **Challenge:** Test locations have zero overlap with training data

[View notebook →](./Cold%20Snap%20Recovery%20Burden)

---

### 9. [Diabetic Patient Hospital Length-of-Stay Prediction](./Diabetic%20Patient%20Hospital%20Length-of-Stay%20Prediction)
Clinical resource optimization through length-of-stay prediction for diabetic patients.

- **Problem:** Predict hospital stay duration from clinical data
- **Method:** XGBoost with clinical feature engineering (num_medications × lab_procedures interaction)
- **Stack:** Python, XGBoost, scikit-learn
- **Dataset:** 14,304 patient records (CSV included ~10 MB)
- **Note:** Notebook outputs require refresh due to XGBoost API change

[View notebook →](./Diabetic%20Patient%20Hospital%20Length-of-Stay%20Prediction)

---

### 10. [Plasma Etching Spatial Uniformity Prediction](./Plasma%20Etching%20Spatial%20Uniformity%20Prediction)
Semiconductor manufacturing quality control through spatial uniformity prediction.

- **Problem:** Predict etching uniformity across 49 wafer zones from 8 process parameters
- **Method:** PyTorch neural network with custom ZWUE loss (zone-weighted, asymmetric penalty)
- **Stack:** Python, PyTorch, physics-motivated feature engineering
- **Dataset:** 12,000 samples (CSV included ~18 MB)
- **Note:** Python script (solution.py) rather than notebook

[View project →](./Plasma%20Etching%20Spatial%20Uniformity%20Prediction)

---

### 11. [Predicting Microsatellite Instability From Tumor Gene Expression](./Predicting%20Microsatellite%20Instability%20From%20Tumor%20Gene%20Expression)
Cancer diagnostics: MSI status prediction from high-dimensional gene expression for treatment planning.

- **Problem:** Classify MSI status (MSI-H / MSI-L / MSS) from ~33,379 gene expression features
- **Method:** High-dimensional classification with feature selection (extreme p >> n challenge)
- **Stack:** Python, scikit-learn, dimensionality reduction
- **Dataset:** Gene expression profiles (**full train excluded**: ~153MB; train_short.csv sample included)
- **Clinical relevance:** MSI-H detection guides immunotherapy eligibility

[View notebook →](./Predicting%20Microsatellite%20Instability%20From%20Tumor%20Gene%20Expression)

---

### 12. [Smart Grid Oscillation Risk Challenge](./Smart%20Grid%20Oscillation%20Risk%20Challenge)
Power grid stability prediction with asymmetric risk-weighted loss for critical infrastructure.

- **Problem:** Predict oscillation risk across 6 grid buses with custom GRWE metric
- **Method:** CatBoost per bus with asymmetric bias correction + multi-output neural network
- **Stack:** Python, CatBoost, custom loss (6.25× penalty for under-predicting high-risk events)
- **Dataset:** 30,000 samples (CSV included ~30 MB)

[View notebook →](./Smart%20Grid%20Oscillation%20Risk%20Challenge)

---

### 13. [Spatiotemporal Mobility Energy Load Modeling](./Spatiotemporal%20Mobility%20Energy%20Load%20Modeling)
Urban energy demand forecasting from mobility patterns with out-of-distribution regime handling.

- **Problem:** Model energy load from spatiotemporal mobility data (OOD seasonal regime in test)
- **Method:** Regression with PCA (PC1 explains 98.8% continuous variance) and robust OOD handling
- **Stack:** Python, scikit-learn, PCA
- **Dataset:** 2,184 samples (CSV included ~6 MB)
- **Challenge:** Test contains unseen seasonal_regime_code=3

[View notebook →](./Spatiotemporal%20Mobility%20Energy%20Load%20Modeling)

---

## 🛠️ Technologies

**Languages:** Python

**Machine Learning:** scikit-learn, CatBoost, PyTorch

**Data Processing:** Pandas, NumPy

**Visualization:** Matplotlib, Seaborn, Plotly

**Audio:** torchaudio, STFT, Mel Spectrograms, MFCC

**Techniques:** Regression, Clustering (K-Means), Classification (Random Forest, Logistic Regression), CNN, Feature Engineering, Cross-Validation

---

## 📦 Installation and Usage

### Option 1: Install all dependencies
```bash
pip install -r requirements.txt
```

### Option 2: By individual project
Each project folder has its own README with specific instructions.

### Runnable notebooks
Most notebooks can be executed without additional downloads (use built-in or included datasets). Exceptions:
- **NFL Player Trajectory:** Requires downloading multi-GB dataset from Kaggle NFL Big Data Bowl 2026
- **Guitar Sound Classifier:** Requires providing your own .wav files

---

## ⚠️ Datasets NOT Included

Due to size, the following datasets are **not in this repository**:

- **NFL Player Trajectory:** NFL tracking data (~several GB) — available on Kaggle NFL Big Data Bowl 2026
- **Guitar Sound Classifier:** 12,600 audio clips .wav (~several GB)
- **CAFA (Protein Function Prediction):** Separate project in Google Colab, not migrated here due to dataset size (UniProt, GO ontology)

---

## 📝 Portfolio Status

> **Work in progress** — curated collection of selected projects, not a finished product.

This portfolio demonstrates projects of increasing complexity:
- Small educational projects (Penguin Classification, Wine Quality, Customer Segmentation)
- Substantial analysis projects (California House Price Predictions, NFL Player Trajectory)
- Deep learning exploration (Guitar Sound Classifier with PyTorch)

**Known limitations:**
- Some projects use historical datasets (e.g., 1990 census)
- Models focus on demonstrating techniques, not exhaustive optimization
- Guitar Sound Classifier: first DL project, room for architectural improvements

---

## 📬 Contact

**Máximo Pere**
- LinkedIn: [linkedin.com/in/maximopere](https://linkedin.com/in/maximopere)
- GitHub: [github.com/MaximoAPS](https://github.com/MaximoAPS)
- Location: Buenos Aires, Argentina

---

## 📄 License

This project is licensed under [MIT License](LICENSE).
