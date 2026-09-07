# Predicting Microsatellite Instability From Tumor Gene Expression

**Problem:** Predict microsatellite instability (MSI) status in tumors from gene expression profiles for cancer diagnosis and treatment planning.

## Data
- **Source:** Cancer genomics challenge dataset
- **Size:** Limited samples with ~33,379 gene expression features
- **Features:** Gene expression values across genome
- **Classes:** 3 MSI status categories
  - **MSI-H:** High microsatellite instability (DNA repair defect, responds to immunotherapy)
  - **MSI-L:** Low instability  
  - **MSS:** Microsatellite stable (majority class)
- **Dataset:** `train_short.csv` (sample), `test.csv` included
  - **Note:** Full `train.csv` (~153MB) excluded from repository due to size

## Approach

**High-dimensional classification** with extreme feature-to-sample ratio challenge (p >> n).

**Technical challenge:**
- ~33,379 gene features with only hundreds of samples
- Requires aggressive dimensionality reduction or feature selection
- Class imbalance (MSS majority class)

**Strategy:**
- Feature selection targeting MSI-relevant genes
- Regularized classification to prevent overfitting
- Careful cross-validation given limited samples

## Results

- **Metric:** Macro F1-score
- **Challenge:** High-dimensional genomic data (33K+ features, few samples)
- **Clinical relevance:** MSI-H detection guides immunotherapy treatment decisions

## Technologies

- Python, Pandas, NumPy
- Scikit-learn (feature selection, classification)
- Dimensionality reduction techniques

## How to Run

```bash
jupyter notebook "Predicting Microsatellite Instability From Tumor Gene Expression.ipynb"
```

**Dataset notes:**
- Uses `train_short.csv` sample file (full training data excluded for size)
- Full `train.csv` is ~153MB and not included in repository
- `test.csv` included for inference

## Applications

- Cancer diagnosis and classification
- Treatment planning (immunotherapy eligibility)
- Genomic biomarker discovery
