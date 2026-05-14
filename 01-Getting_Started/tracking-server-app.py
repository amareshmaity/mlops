import mlflow

## Set mlflow tracking server
mlflow.set_tracking_uri("http://127.0.0.1:5000/")

## Set experiment
mlflow.set_experiment("experiment-demo-app")

## Fetch the current experiments
print(mlflow.get_experiment_by_name("expriment-demo-app"))