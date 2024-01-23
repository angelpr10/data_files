import sys
import subprocess

def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except Exception as e:
        print(f"Error installing {package}: {e}")

# List of common packages in Machine Learning
packages = [
    'numpy',
    'scipy',
    'pandas',
    'matplotlib',
    'seaborn',
    'scikit-learn',
    'tensorflow',
    'keras',
    'pytorch',
    'xgboost',
    'lightgbm',
    'catboost',
    'statsmodels',
    'nltk',
    'spacy',
    'gensim',
    'opencv-python',
    'imbalanced-learn',
    'eli5',
    'shap',
    'lime',
    'yellowbrick',
    'plotly',
    'bokeh',
    'jupyter',
    'ipython'
]

for package in packages:
    install(package)
