import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
import joblib

# Load California housing dataset
housing = fetch_california_housing()
X, y = housing.data, housing.target

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'regression_model.pkl')
