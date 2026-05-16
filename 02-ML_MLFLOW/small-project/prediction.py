from app import model_info, X_test
import mlflow

# Load model 
model_uri = model_info.model_uri
try:
    loaded_model = mlflow.pyfunc.load_model(model_uri=model_uri)
    print("Model loaded successfully.")
except Exception as e:
    print(e)

## Prediction
y_pred = loaded_model.predict(X_test)
print(y_pred[0])