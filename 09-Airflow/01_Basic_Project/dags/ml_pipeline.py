from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


## Define task 1
def preprocess_data():
    print("Preprocessed data")

## Define task 2
def train_model():
    print("Training model")

## Define task 3
def evaluate_model():
    print("Evaluate model")


## Define the DAG
with DAG(
    "ml_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@weekly",
) as dag:

    ## Assign tasks
    preprocess = PythonOperator(
        task_id="preprocess_task",
        python_callable=preprocess_data,
    )

    train = PythonOperator(
        task_id="train_task",
        python_callable=train_model,
    )

    evaluate = PythonOperator(
        task_id="evaluate_task",
        python_callable=evaluate_model,
    )

    ## Set dependencies
    preprocess >> train >> evaluate