# MLflow Project Setup

## What We Are Doing In This Part

Here we are setting up a simple local machine learning project that we will later connect to `MLflow` running on `AWS EC2`.

At this stage, our focus is on the local project setup only.

The main tasks are:

- create the project folder
- create the Python environment
- install required libraries
- create the starter files
- prepare the basic `app.py` structure

## Main Idea Of The Setup

Our project will run locally, but we want its experiment tracking to point to a remote `MLflow` server hosted on `AWS`.

So the setup flow is:

`local project setup -> environment setup -> install dependencies -> create app.py -> prepare code for remote MLflow tracking`

## Step 1. Create The Project Folder

We first need a new folder for the project.

Important things to remember:

- we can create the project anywhere we want
- there is no strict naming rule
- we should open the folder in the terminal and then in `VS Code`

After opening the folder, the next step is to launch the editor using:

```bash
code .
```

This opens the current project in `VS Code`.

## Step 2. Create A Virtual Environment

We create an isolated Python environment using:

```bash
conda create -p venv python==3.10 -y
```

## Why This Command Is Important

### `-p venv`

This creates the environment inside our project folder in a local `venv` directory.

That is useful because the environment stays tied to the project.

### `python==3.10`

This fixes the Python version to `3.10`.

That helps us avoid dependency and compatibility issues later.

### `-y`

This automatically approves the installation and avoids manual confirmation steps.

## Step 3. Create `requirements.txt`

After creating the environment, we add a `requirements.txt` file.

The libraries we need at this stage are:

```txt
mlflow
scikit-learn
boto3
```

## Why We Need These Libraries

### `mlflow`

We need `mlflow` for:

- experiment tracking
- logging parameters
- logging metrics
- logging models
- later connecting to a remote tracking server

### `scikit-learn`

We need `scikit-learn` because we will train a machine learning model in this project.

### `boto3`

We need `boto3` because later we will work with `AWS S3`.

In this setup, the experiment artifacts will eventually be stored in an `S3 bucket`, so Python needs a way to interact with AWS services.

## Step 4. Install The Dependencies

After creating the environment, we activate it and install the dependencies using:

```bash
pip install -r requirements.txt
```

This installs everything listed in `requirements.txt`.

## Why `requirements.txt` Is Important

This file helps us:

- reproduce the project setup easily
- install the same packages again later
- share the project with a consistent dependency list
- keep the environment setup clean and manageable

## Step 5. Create Starter Files

While the installation is happening, we create these two files:

- `app.py`
- `README.md`

## Why We Create `app.py`

`app.py` will contain the actual machine learning and MLflow code.

Instead of using notebooks, we are writing the logic in a Python script because that is closer to real project structure.

This is useful because:

- it is easier to organize
- it is easier to maintain
- it supports modular coding later

## Why We Create `README.md`

We use the project `README.md` to keep steps and setup instructions in one place.

That becomes useful later when the AWS setup gets longer and includes multiple commands.

## Basic Project Structure At This Stage

The project is still simple.

At this point it roughly looks like:

```text
project-folder/
|-- venv/
|-- requirements.txt
|-- app.py
`-- README.md
```

## Step 6. Start Writing `app.py`

Once the dependencies are installed, we start adding the basic imports to `app.py`.

This sets up the base structure for the full code that we will complete later.

## Libraries We Need In `app.py`

### Standard Python Libraries

```python
import os
import warnings
import sys
import logging
```

We use these for:

- environment-related operations
- warning management
- command-line arguments
- application logging

### Data Handling Libraries

```python
import pandas as pd
import numpy as np
```

We use these for:

- reading tabular data
- handling arrays and numeric calculations

`pandas` and `numpy` may sometimes get installed indirectly through other packages, but we are still using them explicitly in the script.

### Scikit-Learn Imports

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
```

These imports tell us that:

- we are dealing with a regression problem
- we will split the data into train and test sets
- we will use `ElasticNet` as the model

### Utility Import

```python
from urllib.parse import urlparse
```

We need this later for handling the tracking URI.

### MLflow Imports

```python
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature
```

We need these for:

- starting MLflow runs
- logging scikit-learn models
- inferring model input/output signature

## Step 7. Set Up Logging

We also add a basic logging configuration.

This helps us because:

- logs are better than only using print statements
- debugging becomes easier
- exceptions are easier to trace

We do not need anything fancy here. A simple logging setup is enough for now.

## Step 8. Create `evaluate_metrics()` Function

We create a helper function:

```python
evaluate_metrics(actual, pred)
```

This function is used to calculate regression metrics.

## Metrics Calculated In This Function

### 1. RMSE

Root Mean Squared Error is calculated using:

```python
np.sqrt(mean_squared_error(actual, pred))
```

This measures how far predictions are from the true values, while penalizing larger errors more.

### 2. MAE

Mean Absolute Error is calculated using:

```python
mean_absolute_error(actual, pred)
```

This gives the average absolute difference between actual and predicted values.

### 3. R2 Score

R-squared is calculated using:

```python
r2_score(actual, pred)
```

This tells us how well the regression model explains the variance in the target variable.

## What The Function Returns

The function returns:

```python
rmse, mae, r2
```

This is useful because we can directly use these values for:

- model evaluation
- printing results
- MLflow metric logging

## Why We Add This Function Early

Even before writing the full training flow, it makes sense to create this helper function because:

- it keeps metric logic in one place
- it avoids repeated code
- it prepares the script for later MLflow logging

## Step 9. Add The Main Entry Point

We also add the standard Python entry point:

```python
if __name__ == "__main__":
```

This is where we will place the executable part of the script.

Later, this block will contain:

- reading the dataset
- train-test split
- model training
- evaluation
- MLflow tracking

## Why This Is Good Practice

Using the main block helps because:

- it clearly separates helper definitions from executable logic
- the script is easier to read
- the code structure becomes cleaner
- future modularization becomes easier

## What We Complete At This Stage

By the end of this setup, we have:

- created the local project folder
- opened the project in `VS Code`
- created a Python environment with `conda`
- listed the required libraries in `requirements.txt`
- installed the packages
- created `app.py`
- created `README.md`
- added the imports
- initialized logging
- written `evaluate_metrics()`
- added the `__main__` block as a placeholder for the next step

## What Comes Next

After this setup, the next step is to complete the machine learning workflow inside `app.py`.

That includes:

- loading the dataset
- splitting data
- training the `ElasticNet` model
- calculating metrics
- connecting the code to MLflow tracking

## Commands We Want To Remember

### Open VS Code

```bash
code .
```

### Create The Environment

```bash
conda create -p venv python==3.10 -y
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## One-Line Summary

Here we set up the local Python project for MLflow on AWS by preparing the environment, dependencies, starter files, logging, and metric helper code.
