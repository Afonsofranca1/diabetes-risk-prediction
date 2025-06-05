# diabetes-risk-prediction


---

## Features

| Feature | Description |
|---------|-------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | 2-Hour serum insulin |
| BMI | Body mass index |
| DiabetesPedigreeFunction | Genetic risk factor |
| Age | Patient age |
| Outcome | 0 = non-diabetic, 1 = diabetic |

---

## Models Used

- Logistic Regression
- Random Forest Classifier
- XGBoost (optional)
- Performance evaluated using accuracy, precision, recall, and ROC-AUC

---

## Key Insights

- Glucose and BMI are among the strongest predictors
- Class imbalance is handled via stratified sampling
- Model interpretation is done using feature importance and confusion matrix

---

## Future Improvements

- Deploy model using Streamlit
- Handle missing values with imputation
- Hyperparameter tuning using GridSearchCV

---

## Author

**Afonso França**  
Biomedical Engineer | Aspiring Data Scientist  
[afonsomanuelfranca@gmail.com]  
[www.linkedin.com/in/afonso-frança]  


