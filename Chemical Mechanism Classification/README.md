# Chemical Mechanism Classification

**Problem:** Classify chemical reactions into one of four mechanism types based on reaction strings.

## Data
- **Source:** Synthetic chemical challenge dataset
- **Size:** 3,000+ reactions (train), 1,500+ reactions (test)
- **Features:** Chemical reaction strings (SMILES-like notation)
- **Classes:** 4 mechanism types
  - Alpha transformation
  - Beta displacement
  - Gamma rearrangement
  - Delta elimination

## Approach

**Hybrid architecture combining rule-based and machine learning:**

1. **Deterministic parser** (~89% of cases, 94.3% accuracy)
   - Semantic inline parsing with two-pass fallback
   - Rule-based chemical logic

2. **ML ensemble** (LightGBM + CatBoost)
   - Tiebreaker for ambiguous cases
   - 75.7% out-of-fold accuracy

3. **API fallback** (optional, auto-detected)

**Feature engineering:**
- Text pattern extraction from reaction strings
- Chemical structure indicators
- Mechanism-specific rule features

## Results

- **Out-of-Fold Accuracy:** 92.2%
- **Baseline (AI):** 77.4%
- **Approach:** Deterministic rules handle majority with high accuracy, ML resolves edge cases

## Technologies

- Python, Pandas, NumPy
- LightGBM, CatBoost
- Pattern matching and chemical parsing

## How to Run

```bash
jupyter notebook "Chemical Mechanism Classification.ipynb"
```

Dataset included in repository.
