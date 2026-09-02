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
