# Add Math Calculation DAG

## Goal of This Example

This lesson shows how to build a simple Airflow DAG where each task depends on the result of the previous task.

The example uses a sequence of mathematical operations:

- start with `10`
- add `5`
- multiply the result by `2`
- subtract `3`
- compute the square of the final result

The main purpose is not the math itself. The real goal is to understand:

- how to create multiple dependent tasks
- how to pass values from one task to another
- how `XCom` works in Airflow
- how to inspect task outputs in the Airflow UI

## New DAG File

Inside the `dags/` folder, a new file is created:

```bash
dags/maths_operation.py
```

This file defines a separate DAG for the math sequence pipeline.

## Problem Flow

The task order in this example is:

1. start with number `10`
2. add `5`
3. multiply by `2`
4. subtract `3`
5. square the result

This creates a pipeline where one step depends on the output of the previous step.

## Imports Used

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
```

### Why These Imports Matter

- `DAG`
  Used to define the workflow
- `PythonOperator`
  Used to convert Python functions into Airflow tasks
- `datetime`
  Used to provide the DAG start date

## Main Idea Behind `XCom`

This transcript introduces `XCom` in a more practical way.

`XCom` is used to pass small pieces of information from one task to another.

In this example:

- one task calculates a value
- that value is stored in `XCom`
- the next task pulls that value and continues the calculation

Two important methods are mentioned:

- `xcom_push()`
  Used to store a value
- `xcom_pull()`
  Used to retrieve a value

## Defining the Task Functions

Each mathematical step is written as a separate Python function.

Example task functions:

- `start_number()`
- `add_five()`
- `multiply_by_two()`
- `subtract_three()`
- `square_number()`

Each function takes `**context` so that task information and `XCom` values can be accessed.

## Starting Task

The first task sets the initial number.

Example idea:

```python
def start_number(**context):
    context["ti"].xcom_push(key="current_value", value=10)
    print("Starting number = 10")
```

### What This Does

- stores `10` in `XCom`
- uses the key `current_value`
- makes that value available to later tasks

## Pulling Values in the Next Task

The second task pulls the previous value, adds `5`, and pushes the new result.

Example idea:

```python
def add_five(**context):
    current_value = context["ti"].xcom_pull(
        key="current_value",
        task_ids="start_task",
    )
    new_value = current_value + 5
    context["ti"].xcom_push(key="current_value", value=new_value)
    print(f"Add 5: {current_value} + 5 = {new_value}")
```

### Important Things to Notice

- `task_ids` tells Airflow which earlier task to read from
- the same key `current_value` is reused
- after each operation, the updated value is stored again

## Same Pattern for the Remaining Tasks

The remaining functions follow the same idea:

- pull the latest `current_value`
- perform one math operation
- push the updated value back to `XCom`
- print the result for logs

### Example Sequence

- `multiply_by_two()` uses the result of `add_five()`
- `subtract_three()` uses the result of `multiply_by_two()`
- `square_number()` uses the result of `subtract_three()`

## Defining the DAG

The DAG is created using a standard `with DAG(...) as dag:` block.

Example structure:

```python
with DAG(
    dag_id="maths_sequence_dag",
    start_date=datetime(2023, 1, 1),
    schedule="@once",
    catchup=False,
) as dag:
```

### Important Parameters

- `dag_id="maths_sequence_dag"`
  The DAG name shown in Airflow
- `start_date=datetime(2023, 1, 1)`
  The date from which the DAG is valid
- `schedule_interval="@once"`
  Used for one-time style execution
- `catchup=False`
  Prevents Airflow from backfilling old runs automatically

## Creating Tasks with `PythonOperator`

Each function is wrapped inside a `PythonOperator`.

Example pattern:

```python
start_task = PythonOperator(
    task_id="start_task",
    python_callable=start_number,
    provide_context=True,
)
```

The same pattern is followed for:

- `add_five_task`
- `multiply_by_two_task`
- `subtract_three_task`
- `square_number_task`

### Why `provide_context=True` Is Used

This allows the function to access Airflow runtime context, including:

- task instance information
- `XCom`
- metadata passed between tasks

## Setting Dependencies

Dependencies control the execution order.

Example:

```python
start_task >> add_five_task >> multiply_by_two_task >> subtract_three_task >> square_number_task
```

This means:

1. start task runs first
2. then add five
3. then multiply by two
4. then subtract three
5. finally square the result

## Expected Calculation

If the pipeline begins with `10`, then:

1. `10 + 5 = 15`
2. `15 * 2 = 30`
3. `30 - 3 = 27`
4. `27 * 27 = 729`

So the final result is:

```text
729
```

## What to Check in the Airflow UI

After running `astro dev start`, the DAG appears in the Airflow UI.

The transcript highlights these areas:

- DAG list
- Graph view
- Logs
- XCom

## Graph View

The graph shows the order of tasks clearly:

```text
start_task -> add_five_task -> multiply_by_two_task -> subtract_three_task -> square_number_task
```

This confirms the sequence is working as a pipeline.

## Logs

The logs help confirm each operation.

Examples mentioned in the transcript:

- `Starting number = 10`
- `10 + 5 = 15`
- `15 * 2 = 30`
- `30 - 3 = 27`
- `27 square = 729`

These log messages are useful for understanding task execution step by step.

## XCom in the UI

The transcript also shows that `XCom` values can be inspected from the Airflow UI.

That means you can verify:

- the current value after each task
- whether the right value was passed forward
- how task outputs move through the pipeline

For this example:

- after `start_task`, `current_value = 10`
- after `add_five_task`, `current_value = 15`
- after `multiply_by_two_task`, `current_value = 30`
- after `subtract_three_task`, `current_value = 27`

## Useful Commands

### Start Airflow

```bash
astro dev start
```

### Stop Airflow

```bash
astro dev stop
```

## Key Learning from This Transcript

- A DAG can model even a simple sequence of dependent operations
- `PythonOperator` lets Python functions run as Airflow tasks
- `XCom` is used to pass values from one task to the next
- `task_ids` help identify which task output should be pulled
- logs and `XCom` together make debugging easier
- Airflow pipelines are built step by step through task dependencies

## Summary

This example is a simple math pipeline, but it teaches an important Airflow concept: passing results between dependent tasks.

The key workflow is:

- define task functions
- store outputs using `xcom_push()`
- retrieve them using `xcom_pull()`
- wrap each function in `PythonOperator`
- set dependencies in sequence
- inspect execution in the Airflow UI

This is a foundational pattern that becomes very useful later in larger ML and data pipelines.
