# E-Commerce Notebook and Model Usage

This document provides guidance on using the E-Commerce Jupyter Notebook for data analysis and machine learning, as well as instructions for utilizing the exported model saved as a .pkl file.

# Overview

The notebook is designed for:

* Analyzing e-commerce data stored in an SQLite database (ecommerce.db).

* Performing feature engineering and exploratory data analysis (EDA).

* Training a machine learning model for predictive tasks.

* Saving the trained model for reuse.

The model can predict outcomes based on features derived from the e-commerce dataset.

# Files Provided

1. Notebook File: E_Commerce (1).ipynb

Contains the complete workflow for data loading, analysis, and model training.

2. Saved Model: model.pkl

A serialized version of the trained machine learning model.

3. E-Commerce Database: ecommerce.db (ensure it exists in the same directory).

Contains the dataset used in the notebook.

# Prerequisites

Ensure the following are installed:

* Python 3.6+

* Jupyter Notebook

* Libraries: pandas, numpy, matplotlib, seaborn, sklearn, sqlite3, pickle, tensorflow

Install libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow
```

Using the notebook
1. Open the notebook in your working directory or in a IDE
2. Load the Dataset (you will need to connect the dabaset ecommerce.db )
3. Execute cells
   * Execute each cell sequentially to:
      > Load and preprocess data.
      > Perform exploratory data analysis
      > Train the machine learning model
4. Exported Model
  * The trained model is saved as model.pkl in the working directory

# Run the prediction Model 
```bash
python prediction_model.py

```
