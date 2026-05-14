# MLflow Experiment Tracking Notes

## Why MLflow Is Added

The project is not only training a model.

It is also tracking experiments so I can answer questions like:

- which run gave better accuracy
- which hyperparameters were used
- which model artifact belongs to which run

## DagsHub + MLflow Connection

MLflow is connected to the DagsHub remote tracking server.

The transcript sets environment variables like:

- `MLFLOW_TRACKING_URI`
- `MLFLOW_TRACKING_USERNAME`
- `MLFLOW_TRACKING_PASSWORD`

The username is the DagsHub username.

The password is usually the DagsHub token or access credential.

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

This is useful because later I can:

- compare model versions
- manage the best model more clearly
- keep deployment-related tracking cleaner

## My Quick Understanding

MLflow handles the experiment side of the story.

DVC handles the data/model versioning side.

Both together make the project much more reproducible.

