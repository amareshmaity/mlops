import pandas
import numpy
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

import mlflow
from mlflow.models import infer_signature

## Set the tracking server
mlflow.set_tracking_uri("http://127.0.0.1:5000")
print(mlflow.get_tracking_uri())

## Set the experiement
mlflow.set_experiment("ML_Experiment")
print(mlflow.get_experiment_by_name("ML_Experiment"))

## Data loading and splitting
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

params = {
    'C': 1.0,
    'solver': 'lbfgs',
    'l1_ratio': 0,
    'max_iter': 500,
    'random_state': 42   
}

## Tracking the experiment
# mlflow.sklearn.autolog()
model = LogisticRegression(**params)
model.fit(X_train, y_train)
accuracy = accuracy_score(y_test, model.predict(X_test))

## Run the experiment
# with mlflow.start_run():

#     # add demo metric
#     mlflow.log_metric("demo_r2", 0.89)

#     # add second metric
#     mlflow.log_metric("accuracy", 0.98)

## Start an MLFlow run
with mlflow.start_run():
    # log the hyperparameter
    mlflow.log_params(params)

    # Log the accuracy metrics
    mlflow.log_metric("accuracy", accuracy)

    # Set a tag that we can use to remind ourselvs what this run was for
    mlflow.set_tag("Tracking Info", "Basic LR model for iris dataset")

    # Infer the model signature
    # Setting sample input and output for signature (Schema)
    signature = infer_signature(X_train, model.predict(X_train))

    # Log the model
    model_info = mlflow.sklearn.log_model(
        sk_model = model,
        name = "logistic-regression-model",
        signature = signature,
        input_example = X_train[0:5],
        registered_model_name = "Iris-LogisticRegression-Model"
    )