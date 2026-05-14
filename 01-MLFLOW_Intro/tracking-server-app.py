import mlflow

## Set mlflow tracking server
mlflow.set_tracking_uri("http://127.0.0.1:5000/")

## Set experiment (this creates it if it doesn't exist)
mlflow.set_experiment("experiment-demo-app")

## Fetch the current experiment (ensure the spelling matches!)
experiment = mlflow.get_experiment_by_name("experiment-demo-app")

print(experiment)