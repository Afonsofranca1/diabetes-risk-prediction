# Diabetes Risk Prediction

A machine learning project that predicts the likelihood of diabetes using patient health indicators from the Pima Indians Diabetes dataset.

---

## Table of Contents

- [Project Motivation](#-project-motivation)
- [Dataset Source](#-dataset-source)
- [Models Used & Rationale](#-models-used--rationale)
- [Model Performance Summary](#-model-performance-summary)
- [Project Structure](#-project-structure)
- [How to Run the Project](#️-how-to-run-the-project)
- [Requirements](#-requirements)
- [Future Work](#-future-work)

---

## Project Motivation

Diabetes is a growing global health concern, affecting over 400 million people worldwide. Early detection plays a crucial role in preventing severe complications such as heart disease, kidney failure, and vision loss.

This project aims to leverage machine learning to build a predictive model that can assess the risk of diabetes based on patient health metrics. The goal is to support healthcare providers and researchers in identifying high-risk individuals and improving early intervention strategies.

---

## Dataset Source

The dataset used in this project is the **Pima Indians Diabetes Database**, originally sourced from the **UCI Machine Learning Repository**, and also commonly available on [Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database).

Features include:
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age
- Outcome (Target: 0 or 1)

---

## Models Used & Rationale

### 1. Logistic Regression
- A simple and interpretable baseline model for binary classification.
- Useful for understanding feature influence through coefficients.

### 2. Random Forest Classifier
- Robust ensemble method that captures feature interactions.
- Offers high performance and feature importance scores.

---

## Model Performance Summary

| Metric            | Logistic Regression | Random Forest |
|------------------|---------------------|---------------|
| Accuracy          | **77%**              | **81%**        |
| Precision         | 75%                  | 80%            |
| Recall            | 68%                  | 76%            |
| F1 Score          | 71%                  | 78%            |
| ROC-AUC Score     | 0.83                 | 0.87           |

*Random Forest outperformed Logistic Regression in all key metrics.*

---

## Key Insights

- Glucose and BMI are among the strongest predictors
- Class imbalance is handled via stratified sampling
- Model interpretation is done using feature importance and confusion matrix


## 📌 Requirements


- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- plotly


---

## 🧪 Future Work

- Hyperparameter tuning (GridSearch, RandomSearch)
- Include SHAP or LIME for model explainability
- Build a web app with Streamlit or Dash
- Use a real-world dataset (e.g., hospital patient data)

---

⭐️ *If you found this project helpful, feel free to give it a star on GitHub!*

## Author

**Afonso França**  
Biomedical Engineer | Aspiring Data Scientist  
[afonsomanuelfranca@gmail.com]  
[www.linkedin.com/in/afonso-frança]  


