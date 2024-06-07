import joblib
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the model
def load_model():
    try:
        return joblib.load('regression_model.pkl')
    except Exception as e:
        raise Exception(f"Error loading model: {str(e)}")

model = load_model()

# Prediction function
def predict(data):
    try:
        data = np.array(data)
        if data.ndim != 2 or data.shape[1] != 8:  # California housing dataset has 8 features
            raise ValueError("Input data must be a 2D array with shape (n_samples, 8)")
        predictions = model.predict(data)
        return predictions
    except Exception as e:
        raise ValueError(f"Prediction error: {str(e)}")

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    if not request.is_json:
        return jsonify({'error': 'Request must be in JSON format'}), 400
    
    try:
        data = request.json.get('data')
        if data is None:
            raise ValueError("No data provided in request")
        
        predictions = predict(data)
        return jsonify({'predictions': predictions.tolist()})
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
    except Exception as e:
        return jsonify({'error': f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

