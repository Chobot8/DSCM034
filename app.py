import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class PredictRequest(BaseModel):
    data: List[List[float]]

# Load the model
def load_model():
    try:
        return joblib.load('regression_model.pkl')
    except Exception as e:
        raise Exception(f"Error loading model: {str(e)}")

model = load_model()

@app.post("/predict")
def predict(request: PredictRequest):
    data = np.array(request.data)
    if data.ndim != 2 or data.shape[1] != 8:  # Assuming the model expects 8 features
        raise HTTPException(status_code=400, detail="Input data must be a 2D array with shape (n_samples, 8)")
    try:
        predictions = model.predict(data)
        return {"predictions": predictions.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)
