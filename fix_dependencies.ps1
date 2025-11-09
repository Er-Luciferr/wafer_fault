# Fix NumPy and scikit-learn compatibility issue
# This script will reinstall scikit-learn to match your current NumPy version

Write-Host "Checking current versions..." -ForegroundColor Cyan
python -c "import numpy; print(f'NumPy: {numpy.__version__}')"
python -c "import sklearn; print(f'scikit-learn: {sklearn.__version__}')" 2>&1

Write-Host "`nReinstalling scikit-learn to fix binary compatibility..." -ForegroundColor Yellow
pip uninstall scikit-learn -y
pip install --no-cache-dir "scikit-learn>=1.5.0"

Write-Host "`nVerifying installation..." -ForegroundColor Cyan
python -c "import numpy; import sklearn; print('✓ NumPy and scikit-learn are now compatible!')"

Write-Host "`nDone! You can now run: python .\src\pipeline\train_pipeline.py" -ForegroundColor Green

