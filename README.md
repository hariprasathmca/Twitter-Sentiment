# 🐦 Twitter Sentiment Analysis

This project analyzes Twitter data to classify tweets into **positive, negative, or neutral sentiments** using multiple Machine Learning algorithms.

---

## 📂 Project Structure
TwitterSentiment/
│── pycache/ # Cache files (can be ignored)
│── results/ # Folder to store model results
│── CreateDataset.py # Script to create dataset from raw data
│── data.xlsx # Dataset file (tweets + labels)
│── DTALG.py # Decision Tree Algorithm
│── NBALG.py # Naive Bayes Algorithm
│── RFALG.py # Random Forest Algorithm
│── SVMALG.py # Support Vector Machine Algorithm
│── XGBOOSTALG.py # XGBoost Algorithm
│── Main.py # Main driver script
│── twitter.json # Twitter dataset (JSON format)
---
## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/TwitterSentiment.git
   cd TwitterSentiment
Install dependencies:

bash
Copy code
pip install -r requirements.txt

Run the main script:
python Main.py

📊 Algorithms Implemented
Decision Tree (DT)
Naive Bayes (NB)
Random Forest (RF)
Support Vector Machine (SVM)
XGBoost

🎯 Features
Preprocesses Twitter dataset
Applies multiple ML algorithms
Compares performance between models
Stores results in /results folder

📌 Requirements
Python 3.x
pandas
numpy
scikit-learn
xgboost
scikit-learn

xgboost
