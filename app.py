import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("models/model.pkl", "rb"))

# Start Dash app
app = dash.Dash(__name__)
server = app.server  # for deployment

# App layout
app.layout = html.Div([
    html.H1("Diabetes Risk Predictor", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Glucose:"),
        dcc.Input(id='glucose', type='number', value=100, required=True),

        html.Label("BMI:"),
        dcc.Input(id='bmi', type='number', value=25.0, required=True),

        html.Label("Age:"),
        dcc.Input(id='age', type='number', value=30, required=True),

        html.Button("Predict", id='predict-btn', n_clicks=0),

        html.Div(id='prediction-output', style={'marginTop': '20px'})
    ], style={'width': '50%', 'margin': 'auto'})
])

# Callback for prediction
@app.callback(
    Output('prediction-output', 'children'),
    Input('predict-btn', 'n_clicks'),
    State('glucose', 'value'),
    State('bmi', 'value'),
    State('age', 'value')
)
def predict(n_clicks, glucose, bmi, age):
    if n_clicks > 0:
        features = np.array([[glucose, bmi, age]])
        prediction = model.predict(features)[0]
        return f"Prediction: {'Diabetic' if prediction == 1 else 'Not Diabetic'}"

if __name__ == '__main__':
    app.run(debug=True)
