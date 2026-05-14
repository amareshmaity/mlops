## Import libraries
import mlflow

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

## Set mlflow tracking uri and experiment
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("load-diabities-regression")

## Start mlflow autolog
mlflow.autolog()

## Load the data sets
db = load_diabetes()

## Split into training and testing set
X_train, X_test, y_train, y_test = train_test_split(db.data, db.target, random_state=42)

model = RandomForestRegressor(
    n_estimators=100,
    max_depth=6, max_features=3
)

model.fit(X_train, y_train)


## Run the code 
# python app.py

## View the result in the MLflow UI
# mlflow server--port 8000