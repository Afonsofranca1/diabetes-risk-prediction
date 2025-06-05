import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import numpy as np
import joblib

# Load the trained model (choose the one you prefer)
model = joblib.load('models/logistic_regression_model.pkl')  # or 'random_forest_model.pkl'

# Feature list based on your dataset (customize this!)
features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 
            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Diabetes Risk Predictor"

# App Layout
app.layout = html.Div([
    html.H1("Diabetes Risk Prediction", style={'textAlign': 'center', 'color': '#003366'}),

    html.Div([
        html.Div([
            html.Label(f"{feature}:"),
            dcc.Input(id=feature, type='number', required=True, step=0.1),
        ], style={'margin': '10px'}) for feature in features
    ]),

    html.Button("Predict Risk", id='submit-button', n_clicks=0, style={'margin': '20px'}),

    html.Div(id='prediction-output', style={'fontSize': '24px', 'marginTop': '20px'})
])

# Callback to predict diabetes risk
@app.callback(
    Output('prediction-output', 'children'),
    Input('submit-button', 'n_clicks'),
    [State(feature, 'value') for feature in features]
)
def predict(n_clicks, *values):
    if None in values:
        return "❗ Please fill in all input fields."
    
    input_data = pd.DataFrame([values], columns=features)
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]  # probability of positive class

    if prediction == 1:
        return f"⚠️ High risk of diabetes ({proba:.2%} probability)"
    else:
        return f"✅ Low risk of diabetes ({proba:.2%} probability)"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

