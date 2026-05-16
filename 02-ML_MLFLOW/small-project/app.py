import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, r2_score, confusion_matrix

import mlflow
from mlflow.models import infer_signature


## Set experiment tracking server uri
print("Setting mlflow tracking server url...")
mlflow.set_tracking_uri("http://127.0.0.1:5000/")
print("\nMLFLOW tracking uri has been succussful. The uri is: {mlflow.get_tracking_uri()}")

## Set Experiment
print("\nSetting Experiment...")
mlflow.set_experiment("ml-model-test-v2")
print("Experiment has been successfully set.")

## Run experiment
with mlflow.start_run():

    ## Load data
    X, y = load_iris(return_X_y=True)

    ## split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    ## model training
    model_parameters = {
        'C': 1.0,
        'solver': 'lbfgs',
        'l1_ratio': 0,
        'max_iter': 500,
        'random_state': 42   
    }
    
    model = LogisticRegression(**model_parameters)
    model.fit(X_train, y_train)

    ## Prediction
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    ## Evaluation
    # Training metrics
    training_accuracy = accuracy_score(y_train, y_train_pred)
    training_r2_score = r2_score(y_train, y_train_pred)

    # Testing metrics
    testing_accuracy = accuracy_score(y_test, y_test_pred)
    testing_r2_score = r2_score(y_test, y_test_pred)

    ## Experimenting Tracking
    # Set a tag for experiment
    mlflow.set_tag("Tracking info", "Basic LR model for iris dataset")

    # Log model's hyperparameters
    mlflow.log_params(params=model_parameters)

    # Log metrices 
    mlflow.log_metrics({
        'training_accuracy':training_accuracy,
        'testing_accuracy': testing_accuracy,
        'training_r2_score': training_r2_score,
        'testing_r2_score': testing_r2_score
    })

    # Log the model
    # Setting sample input and output signature (schema)
    signature = infer_signature(X_train, model.predict(X_train))
    model_info = mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="logistic-regression-model",
        signature=signature,
        input_example=X_train[0:5],
        registered_model_name="Iris-LogisticRegression-Model"
    )

  