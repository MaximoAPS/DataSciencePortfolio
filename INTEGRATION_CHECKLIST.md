# Integration Checklist for ML Case Study Projects

This document tracks the integration status of the 7 applied ML case study projects.

## Projects to Integrate

### 1. Chemical Mechanism Classification
- [ ] Notebook added (solution.ipynb → Chemical Mechanism Classification.ipynb)
- [ ] Notebook executed with outputs
- [ ] Data files added (if <10MB) or documented as excluded
- [ ] README updated with actual methods and results
- [ ] Secrets/credentials stripped

### 2. Cold Snap Recovery Burden
- [ ] Notebook added (solution.ipynb → Cold Snap Recovery Burden.ipynb)
- [ ] Notebook executed with outputs
- [ ] Data files added (if <10MB) or documented as excluded
- [ ] README updated with actual methods and results
- [ ] Secrets/credentials stripped

### 3. Diabetic Patient Hospital Length-of-Stay Prediction
- [ ] Notebook added (solution.ipynb → Diabetic Patient Hospital Length-of-Stay Prediction.ipynb)
- [ ] Notebook executed with outputs
- [ ] Data files added (if <10MB) or documented as excluded
- [ ] README updated with actual methods and results
- [ ] Secrets/credentials stripped

### 4. Plasma Etching Spatial Uniformity Prediction
- [ ] Code added (may be main.py instead of notebook)
- [ ] If notebook: executed with outputs
- [ ] Data files added (if <10MB) or documented as excluded
- [ ] README updated with actual methods and results
- [ ] Secrets/credentials stripped

### 5. Predicting Microsatellite Instability From Tumor Gene Expression
- [ ] Notebook added (solution.ipynb → Predicting Microsatellite Instability From Tumor Gene Expression.ipynb)
- [ ] Notebook executed with outputs (if runtime reasonable)
- [ ] Data handling: train.csv likely >90MB - use train_short.csv or exclude
- [ ] README updated with dataset exclusion note if needed
- [ ] README updated with actual methods and results
- [ ] Secrets/credentials stripped

### 6. Smart Grid Oscillation Risk Challenge
- [ ] Notebook added (solution.ipynb → Smart Grid Oscillation Risk Challenge.ipynb)
- [ ] Notebook executed with outputs
- [ ] Data files added (if <10MB) or documented as excluded
- [ ] README updated with actual methods and results
- [ ] Secrets/credentials stripped

### 7. Spatiotemporal Mobility Energy Load Modeling
- [ ] Notebook added (solution.ipynb → Spatiotemporal Mobility Energy Load Modeling.ipynb)
- [ ] Notebook executed with outputs
- [ ] Data files added (if <10MB) or documented as excluded
- [ ] README updated with actual methods and results
- [ ] Secrets/credentials stripped

## Integration Guidelines

### Notebook Execution
Execute notebooks with output cells saved:
```bash
jupyter nbconvert --execute --inplace --to notebook "path/to/notebook.ipynb"
```

Or execute with timeout for long-running notebooks:
```bash
jupyter nbconvert --execute --inplace --ExecutePreprocessor.timeout=900 --to notebook "path/to/notebook.ipynb"
```

### Dataset Size Guidelines
- **< 10MB**: Include in repository
- **10-90MB**: Consider including if essential, document size
- **> 90MB**: Exclude and document in README (follow NFL/Guitar pattern)

For excluded datasets:
- Add to .gitignore
- Update project README with note: "Dataset not included due to size"
- Optionally provide download instructions or mention availability

### Renaming Convention
Rename notebooks from generic names to project-specific:
- `solution.ipynb` → `[Project Name].ipynb` (Title Case)
- Example: `solution.ipynb` → `Chemical Mechanism Classification.ipynb`

### README Updates
Once notebooks are executed, update each project README with:
- Actual features and data size
- Specific methods used (model types, algorithms)
- Real results (accuracy, RMSE, R², etc.) - DO NOT fabricate
- Technology stack (actual libraries used)
- Remove "⚠️ Integration in progress" status line
- Update "How to Run" section with actual command

### Main README Updates
After completing integration:
- Update project 7-13 entries with real methods and results
- Remove "Status: ⚠️ Integration in progress" from entries
- Change "*To be documented after integration*" to actual information

### Credentials Check
Before committing, verify no Kaggle credentials or API keys:
```bash
grep -r "kaggle" . --include="*.ipynb" --include="*.py"
grep -r "api_key" . --include="*.ipynb" --include="*.py"
```

## Post-Integration Tasks
- [ ] All notebooks executed successfully
- [ ] All READMEs updated with real information
- [ ] Main README updated with actual project details
- [ ] Large datasets handled appropriately
- [ ] No secrets committed
- [ ] PR updated with completion status
- [ ] PR marked ready for review (draft: false)
