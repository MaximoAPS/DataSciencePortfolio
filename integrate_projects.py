#!/usr/bin/env python3
"""
Integration automation script for ML case study projects.
Handles notebook renaming, execution, and README preparation.
"""

import os
import subprocess
import json
from pathlib import Path

# Project definitions
PROJECTS = [
    "Chemical Mechanism Classification",
    "Cold Snap Recovery Burden",
    "Diabetic Patient Hospital Length-of-Stay Prediction",
    "Plasma Etching Spatial Uniformity Prediction",
    "Predicting Microsatellite Instability From Tumor Gene Expression",
    "Smart Grid Oscillation Risk Challenge",
    "Spatiotemporal Mobility Energy Load Modeling",
]

def find_notebooks(project_dir):
    """Find notebook files in project directory."""
    notebooks = []
    for file in Path(project_dir).glob("*.ipynb"):
        if ".ipynb_checkpoints" not in str(file):
            notebooks.append(file)
    return notebooks

def find_python_files(project_dir):
    """Find Python script files in project directory."""
    return list(Path(project_dir).glob("*.py"))

def rename_notebook(old_path, new_name):
    """Rename notebook to match project naming convention."""
    new_path = old_path.parent / f"{new_name}.ipynb"
    if old_path != new_path:
        print(f"  Renaming: {old_path.name} -> {new_path.name}")
        old_path.rename(new_path)
    return new_path

def check_for_credentials(notebook_path):
    """Check notebook for potential credentials/secrets."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        content = f.read().lower()
    
    warnings = []
    if 'kaggle' in content and ('username' in content or 'key' in content):
        warnings.append("Potential Kaggle credentials found")
    if 'api_key' in content or 'api-key' in content:
        warnings.append("Potential API key found")
    if 'password' in content and '=' in content:
        warnings.append("Potential password found")
    
    return warnings

def get_file_size_mb(file_path):
    """Get file size in MB."""
    return os.path.getsize(file_path) / (1024 * 1024)

def execute_notebook(notebook_path, timeout=900):
    """Execute notebook and save with outputs."""
    print(f"  Executing notebook (timeout: {timeout}s)...")
    try:
        cmd = [
            "jupyter", "nbconvert",
            "--execute",
            "--inplace",
            "--to", "notebook",
            f"--ExecutePreprocessor.timeout={timeout}",
            str(notebook_path)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 60)
        
        if result.returncode == 0:
            print(f"  ✓ Execution successful")
            return True, None
        else:
            error = result.stderr or result.stdout
            print(f"  ✗ Execution failed: {error[:200]}")
            return False, error
    except subprocess.TimeoutExpired:
        print(f"  ✗ Execution timed out after {timeout}s")
        return False, "Timeout"
    except Exception as e:
        print(f"  ✗ Execution error: {str(e)}")
        return False, str(e)

def check_data_files(project_dir):
    """Check for data files and their sizes."""
    data_files = []
    for ext in ['*.csv', '*.parquet', '*.pkl', '*.json', '*.zip']:
        for file in Path(project_dir).glob(ext):
            size_mb = get_file_size_mb(file)
            data_files.append({
                'name': file.name,
                'size_mb': size_mb,
                'should_include': size_mb < 10,
                'path': file
            })
    return data_files

def process_project(project_name):
    """Process a single project: rename, check, execute."""
    print(f"\n{'='*60}")
    print(f"Processing: {project_name}")
    print(f"{'='*60}")
    
    project_dir = Path(project_name)
    if not project_dir.exists():
        print(f"  ⚠ Project directory not found")
        return
    
    # Check for notebooks
    notebooks = find_notebooks(project_dir)
    python_files = find_python_files(project_dir)
    
    if not notebooks and not python_files:
        print(f"  ⚠ No notebooks or Python files found")
        return
    
    # Process notebooks
    if notebooks:
        for nb in notebooks:
            print(f"\n  Found notebook: {nb.name}")
            
            # Rename if needed
            if nb.stem.lower() in ['solution', 'notebook', 'main']:
                nb = rename_notebook(nb, project_name)
            
            # Check for credentials
            warnings = check_for_credentials(nb)
            if warnings:
                print(f"  ⚠ SECURITY WARNINGS:")
                for warning in warnings:
                    print(f"    - {warning}")
                print(f"  → Manual review required before commit!")
            
            # Ask about execution
            print(f"\n  Execute notebook? (y/n/custom-timeout): ", end='')
            # For automation, we'll skip interactive input
            # In manual use, uncomment the line below
            # response = input().strip().lower()
            response = "n"  # Default to no for safety
            
            if response == 'y':
                success, error = execute_notebook(nb, timeout=900)
            elif response.isdigit():
                success, error = execute_notebook(nb, timeout=int(response))
            else:
                print(f"  → Skipped execution (run manually)")
    
    # Check Python files
    if python_files:
        for py_file in python_files:
            print(f"\n  Found Python script: {py_file.name}")
            print(f"  → Python scripts not auto-executed (run manually)")
    
    # Check data files
    data_files = check_data_files(project_dir)
    if data_files:
        print(f"\n  Data files found:")
        for df in data_files:
            status = "✓ INCLUDE" if df['should_include'] else "✗ EXCLUDE (>10MB)"
            print(f"    {status}: {df['name']} ({df['size_mb']:.2f} MB)")
            
            if not df['should_include']:
                print(f"      → Add to .gitignore if not already excluded")
                print(f"      → Document in README as 'dataset not included'")
    
    # README check
    readme_path = project_dir / "README.md"
    if readme_path.exists():
        with open(readme_path, 'r') as f:
            content = f.read()
        if "⚠️ **Integration in progress**" in content:
            print(f"\n  ⚠ README still has 'Integration in progress' status")
            print(f"    → Update with actual methods and results after execution")

def main():
    """Main integration workflow."""
    print("="*60)
    print("ML Case Study Integration Script")
    print("="*60)
    
    print("\nThis script will:")
    print("1. Find and rename notebooks (solution.ipynb → Project Name.ipynb)")
    print("2. Check for credentials/secrets")
    print("3. Optionally execute notebooks with outputs")
    print("4. Check data file sizes")
    print("5. Report integration status")
    
    print("\n" + "="*60)
    input("Press Enter to start, or Ctrl+C to cancel...")
    
    for project in PROJECTS:
        process_project(project)
    
    print("\n" + "="*60)
    print("Integration scan complete!")
    print("="*60)
    print("\nNext steps:")
    print("1. Review any security warnings about credentials")
    print("2. Execute notebooks manually if skipped")
    print("3. Update project READMEs with actual results")
    print("4. Update main README.md to remove 'Integration in progress'")
    print("5. Verify large data files are in .gitignore")
    print("6. Run: git status")
    print("7. Run: git add <files>")
    print("8. Run: git commit -m 'Add executed notebooks and data'")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled by user")
    except Exception as e:
        print(f"\nError: {e}")
