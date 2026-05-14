"""
Apache Airflow introduced the TaskFlow API which allows you to create tasks using Python decorators like @task. This is a cleaner and more intuitive way of writing tasks without needing to manually use operators like PythonOperator. Let me show you how to modify the previous code to use the @task decorator.

"""

from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from datetime import datetime

## Define the DAG
with DAG(
    dag_id = 'math_sequence_dag_with_taskflow',
    start_date = datetime(2026,1,1),
    schedule="@once",
    catchup=False,
) as dag:

    # Task 1: Start with the initial number
    @task
    def start_number():
        initial_value=10
        print(f"Starting number: {initial_value}")
        return initial_value
    
    @task
    def add_five(number):
        new_value = number + 5
        print(f"Add 5: {number} + 5 = {new_value}")
        return new_value

    @task
    def multiply_by_two(number):
        new_value = number * 2
        print(f"Multiply by 2: {number} * 2 = {new_value}")
        return new_value
    
    @task
    def subtract_by_three(number):
        new_value = number - 3
        print(f"Subtract three: {number} - 3 = {new_value}")
        return new_value
    
    @task
    def sqauare(number):
        new_value = number ** 2
        print(f"Square number: {number} ^ 2 = {new_value}")
        return new_value


    ## Define dependencies
    start_value = start_number()
    added_value = add_five(start_value)
    multiplied_value = multiply_by_two(added_value)
    subtracted_value = subtract_by_three(multiplied_value)
    squared_value = sqauare(subtracted_value)