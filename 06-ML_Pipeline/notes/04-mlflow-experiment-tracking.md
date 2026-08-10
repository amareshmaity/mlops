# MLflow Experiment Tracking Notes

## Why MLflow Is Added

The project is not only training a model.

It is also tracking experiments so I can answer questions like:

- which run gave better accuracy
- which hyperparameters were used
- which model artifact belongs to which run

## DagsHub + MLflow Connection

MLflow is connected to the DagsHub remote tracking server.

You should use environment variables like:

- `MLFLOW_TRACKING_URI`
- `MLFLOW_TRACKING_USERNAME`
- `MLFLOW_TRACKING_PASSWORD`

Example: `MLFLOW_TRACKING_URI=https://dagshub.com/username/mlpipeline.mlflow`

* The username is the DagsHub username.
* The password is usually the DagsHub token or access credential.

## What Gets Logged

During training, the following are logged:

- accuracy metric
- best hyperparameters
- confusion matrix
- classification report
- trained model artifact

## Common MLflow Functions Used

- `mlflow.set_tracking_uri(...)`
- `mlflow.start_run()`
- `mlflow.log_metric(...)`
- `mlflow.log_param(...)`
- `mlflow.log_text(...)`
- `mlflow.sklearn.log_model(...)`

## Signature Logging

The code also uses model signature inference.

That means MLflow can understand:

- input schema
- output schema

This helps in better model tracking and registration.

## Model Registry Idea

The trained model is also registered in MLflow.

This is useful because later you can:

- compare model versions
- manage the best model more clearly
- keep deployment-related tracking cleaner


