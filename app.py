from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import pickle

app = Flask(__name__)

# Load the model and scaler
try:
    with open('model_scaler_iris.pkl', 'rb') as file:
        model, scaler = pickle.load(file)
    print("Model and scaler loaded successfully.")
except Exception as e:
    print("Error occurred while loading the model and scaler:", e)
    # Consider adding a fallback mechanism or error message to the user

@app.route('/')
def home():
    return render_template('index.html')  # Assuming you have an index.html template

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        # Preprocess the input data
        input_data = pd.DataFrame(data, index=[0])

        # Rename columns to match scaler's expectations (adjust as needed)
        input_data.rename(columns={'petalLength': 'petal_length',
                                   'petalWidth': 'petal_width',
                                   'sepalLength': 'sepal_length',
                                   'sepalWidth': 'sepal_width'}, inplace=True)

        # Transform data using scaler
        input_scaled = scaler.transform(input_data)

        # Predict the class
        prediction = model.predict(input_scaled)[0]

        return jsonify({'prediction': prediction})
    except Exception as e:  # Catch any unexpected errors
        return jsonify({'error': str(e)}), 400  # Return a 400 Bad Request status code

if __name__ == '__main__':
    app.run(debug=True)
