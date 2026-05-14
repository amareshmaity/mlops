# Add Files to DAG

## Goal of This Step

In this lesson, the main idea is to create a new DAG file inside the `dags/` folder and understand the basic skeleton of an Airflow pipeline.

Instead of building a full ML workflow, the focus is on learning:

- how to create a new DAG file
- how to define tasks as Python functions
- how to connect tasks in sequence
- how to view the DAG and logs in the Airflow UI

## Creating a New DAG File

Inside the Astro project, a new Python file is created in the `dags/` folder.

Example:

```bash
dags/ml_pipeline.py
```

This file becomes a separate DAG in Airflow.

That means:

- `example_astronauts.py` creates one DAG
- `ml_pipeline.py` creates another DAG

## Basic Imports Used

The transcript uses three important imports:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
```

### Why These Imports Matter

- `DAG`
  Used to define the workflow itself
- `PythonOperator`
  Used to create tasks from Python functions
- `datetime`
  Used to set the DAG start date

## Defining the Tasks

Three simple Python functions are created:

- `preprocess_data()`
- `train_model()`
- `evaluate_model()`

Each function only prints a message for now. The purpose is not the ML logic yet, but understanding how task execution works.

Example:

```python
def preprocess_data():
    print("Preprocessed data")

def train_model():
    print("Training model")

def evaluate_model():
    print("Evaluate model")
```

## Defining the DAG

The DAG is created using a `with DAG(...) as dag:` block.

Example structure:

```python
with DAG(
    "ml_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@weekly",
) as dag:
```

### Important Parameters

- `ml_pipeline`
  The DAG name visible in the Airflow UI
- `start_date=datetime(2024, 1, 1)`
  The date from which the DAG becomes valid
- `schedule_interval="@weekly"`
  Runs the DAG on a weekly schedule

## Creating Tasks with `PythonOperator`

Each task is connected to one Python function through `PythonOperator`.

Example:

```python
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
```

### Important Points

- `task_id` must be unique
- `python_callable` should contain the function name only
- do not use brackets like `preprocess_data()`
- `PythonOperator` executes the Python function as an Airflow task

## Setting Task Dependencies

Dependencies decide the order in which tasks run.

Example:

```python
preprocess >> train >> evaluate
```

This means:

1. run preprocessing first
2. then run training
3. then run evaluation

This is how Airflow represents a pipeline as a directed graph.

## Full Basic Example

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def preprocess_data():
    print("Preprocessed data")


def train_model():
    print("Training model")


def evaluate_model():
    print("Evaluate model")


with DAG(
    "ml_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@weekly",
) as dag:

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

    preprocess >> train >> evaluate
```

## Running the DAG Locally

After creating the file, start Airflow with:

```bash
astro dev start
```

Once the services start:

- open the Airflow UI
- sign in if required
- check whether the new DAG appears in the list

The new file `ml_pipeline.py` should create a DAG named `ml_pipeline`.

## What Becomes Visible in the Airflow UI

After the DAG is loaded, Airflow shows:

- the DAG name
- all tasks inside the DAG
- graph view
- logs
- event history
- code view
- XCom entries

## Graph View

In graph view, the task flow appears visually:

```text
preprocess_task -> train_task -> evaluate_task
```

This helps verify that dependencies are defined correctly.

## Logs

Each task has logs that show what happened during execution.

For example:

- `preprocess_task` log shows the preprocessing message
- `train_task` log shows the training message
- `evaluate_task` log shows the evaluation message

This confirms that the Python functions were executed.

## XCom

The transcript briefly introduces `XCom`.

XCom is used when one task needs to pass some small value or information to another task.

At this stage, it is enough to remember:

- XCom stores task-to-task data
- it becomes useful when tasks need to share outputs

## Useful Astro Commands

### Start the Local Environment

```bash
astro dev start
```

### Stop the Local Environment

```bash
astro dev stop
```

### Restart After Code Changes

```bash
astro dev restart
```

This is helpful when containers are already running and DAG code has been updated.

## Key Learning from This Transcript

- A new DAG is created by adding a Python file inside `dags/`
- Tasks can be written as normal Python functions
- `PythonOperator` turns Python functions into Airflow tasks
- Dependencies define execution order
- The Airflow UI helps inspect tasks, logs, graph view, and code
- `astro dev restart` is useful after modifying DAG code

## Summary

This transcript introduces the basic structure of an Airflow DAG through a simple ML pipeline example.

The main takeaway is not the ML logic itself, but the workflow pattern:

- define Python functions
- wrap them as Airflow tasks
- connect them with dependencies
- run the DAG through Astro
- inspect execution in the Airflow UI
