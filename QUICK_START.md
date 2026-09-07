# Quick Start Guide for Content Integration

This guide helps you quickly add the Proyecto Eris notebooks and data to complete the integration.

## 1. Quick Method: Copy Raw Content

If you have the raw project folders locally:

```bash
# Navigate to repository
cd /workspace  # or your local clone path

# Ensure you're on the correct branch
git checkout cursor/add-ml-case-studies-cd48
git pull origin cursor/add-ml-case-studies-cd48

# Copy/move each project folder content
# For each of the 7 projects, copy notebooks and data into the corresponding folder:
# - Chemical Mechanism Classification/
# - Cold Snap Recovery Burden/
# - Diabetic Patient Hospital Length-of-Stay Prediction/
# - Plasma Etching Spatial Uniformity Prediction/
# - Predicting Microsatellite Instability From Tumor Gene Expression/
# - Smart Grid Oscillation Risk Challenge/
# - Spatiotemporal Mobility Energy Load Modeling/

# Example:
# cp ~/local-eris-projects/"Chemical Mechanism Classification"/*.ipynb "Chemical Mechanism Classification/"
# cp ~/local-eris-projects/"Chemical Mechanism Classification"/*.csv "Chemical Mechanism Classification/"
```

## 2. Run Automated Integration Script

```bash
# Run the integration script to:
# - Rename notebooks (solution.ipynb → Project Name.ipynb)
# - Check for credentials
# - Optionally execute notebooks
# - Validate data file sizes

python3 integrate_projects.py
```

## 3. Manual Steps (if preferred)

### For Each Project:

1. **Copy files** into project folder
2. **Rename notebook**: `solution.ipynb` → `[Project Name].ipynb` (Title Case)
3. **Execute notebook**:
   ```bash
   jupyter nbconvert --execute --inplace --to notebook "path/to/notebook.ipynb"
   ```
4. **Check data sizes**:
   ```bash
   ls -lh *.csv
   # If any file >90MB, ensure it's in .gitignore and add note to README
   ```
5. **Check for secrets**:
   ```bash
   grep -i "kaggle\|api_key\|password" *.ipynb
   ```
6. **Update README.md**:
   - Replace "*To be documented*" with actual info
   - Add real results from executed notebook
   - Remove "⚠️ Integration in progress" line

### Example for One Project:

```bash
# Chemical Mechanism Classification example
cd "Chemical Mechanism Classification/"

# Copy files
cp ~/eris-projects/chem/solution.ipynb .
cp ~/eris-projects/chem/*.csv .

# Rename
mv solution.ipynb "Chemical Mechanism Classification.ipynb"

# Execute (with 15-minute timeout)
jupyter nbconvert --execute --inplace --ExecutePreprocessor.timeout=900 \
  --to notebook "Chemical Mechanism Classification.ipynb"

# Check size
ls -lh *.csv

# Edit README.md to add real results
# ...

cd ..
```

## 4. Update Main README

Edit `/workspace/README.md`:
- For each of projects 7-13, replace placeholder text with actual:
  - Method description
  - Results (accuracy, RMSE, etc.)
  - Stack (specific libraries used)
- Remove "Status: ⚠️ Integration in progress" lines
- Change "*To be documented after integration*" to real info

## 5. Final Checks

```bash
# Verify no secrets committed
grep -r "kaggle\|api.*key" . --include="*.ipynb" --include="*.py"

# Check git status
git status

# Verify large files aren't staged
git status | grep -E "(train\.csv|test\.csv)" && echo "⚠ Check large files!"

# Review changes
git diff README.md | head -50
```

## 6. Commit and Update PR

```bash
# Stage changes
git add -A

# Commit
git commit -m "Integrate ML case study notebooks and data

- Add executed notebooks with outputs for 7 projects
- Include datasets <10MB, document exclusions for large data
- Update all READMEs with actual results and methods
- Strip credentials and secrets"

# Push
git push origin cursor/add-ml-case-studies-cd48

# PR will automatically update
# Then mark PR as ready for review (set draft: false)
```

## 7. Mark PR Ready

Once everything is integrated:
```bash
# Use GitHub UI or gh CLI to mark PR ready:
gh pr ready 3  # PR #3

# Or update via the PR interface to set draft=false
```

## Project-Specific Notes

### Plasma Etching Spatial Uniformity Prediction
- May use `main.py` instead of notebook
- If so, document how to run it in README

### Predicting Microsatellite Instability From Tumor Gene Expression
- `train.csv` likely >90MB - DO NOT commit raw train.csv
- Use `train_short.csv` if available, or document dataset as excluded
- Already configured in .gitignore

## Quick Checklist

- [ ] All 7 project folders have notebooks/code
- [ ] Notebooks renamed to Title Case matching project name
- [ ] Notebooks executed with output cells saved
- [ ] Data files <10MB included, >90MB excluded and documented
- [ ] No Kaggle credentials or API keys in code
- [ ] Individual project READMEs updated with real info
- [ ] Main README projects 7-13 updated with real methods/results
- [ ] "Integration in progress" status removed
- [ ] Changes committed and pushed
- [ ] PR marked ready for review

## Need Help?

See detailed instructions in [`INTEGRATION_CHECKLIST.md`](./INTEGRATION_CHECKLIST.md)
