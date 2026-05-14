# Implementing End-to-End MLflow Code

## What We Are Doing In This Part

Here we are completing the main logic inside `app.py`.

In the previous setup, we had already:

- created the project structure
- installed the required libraries
- added imports
- created the `evaluate_metrics()` function
- added the `__main__` block

Now we are filling in the actual machine learning workflow.

The goal here is to:

- read the dataset
- split the data
- train the model
- evaluate predictions
- log parameters and metrics with `MLflow`
- prepare the code for remote tracking on `AWS`

## Main Flow Of The Code

The end-to-end flow in this part looks like this:

`read dataset -> split data -> train ElasticNet -> predict -> evaluate -> log params and metrics -> prepare remote tracking`

## Step 1. Read The Dataset

The first part of the code is data ingestion.

We are using the **Wine Quality** dataset.

This dataset contains multiple input features such as:

- fixed acidity
- volatile acidity
- citric acid
- residual sugar
- chlorides
- free sulfur dioxide
- total sulfur dioxide
- and other chemical properties

The target column is:

- `quality`

So this is a supervised learning problem where we want to predict the wine quality using the given features.

## Why This Dataset Is Useful Here

This dataset is useful because:

- it is simple enough for demonstration
- it has clear tabular input features
- it works well for building a regression example
- it helps us focus more on MLflow tracking than on complex modeling

## Reading The Dataset From A URL

Instead of downloading the CSV manually, we read it directly from a URL.

The code idea is:

```python
csv_url = "..."
data = pd.read_csv(csv_url, sep=";")
```

## Important Detail: Separator

The CSV uses:

```python
sep=";"
```

This is important because the Wine Quality dataset is semicolon-separated, not comma-separated.

If we forget this separator, the dataset will not load correctly.

## Exception Handling While Reading Data

We wrap the dataset-loading logic inside a `try-except` block.

This helps because:

- the URL may be wrong
- the file may not be reachable
- network issues can happen
- data ingestion errors should be logged clearly

The general flow is:

```python
try:
    data = pd.read_csv(csv_url, sep=";")
except Exception as e:
    logger.exception("Unable to download the data")
    raise e
```

## Why Logging The Exception Matters

Using `logger.exception()` is useful because:

- it records the error clearly
- it helps debugging later
- it gives us a better message than failing silently

## Step 2. Split The Data Into Train And Test

After loading the data, the next step is to split it into train and test sets.

For that we use:

```python
train, test = train_test_split(data)
```

Since no explicit split ratio is provided, the default behavior is used.

That means:

- `75%` of the data goes to training
- `25%` of the data goes to testing

## Why We Split The Data

We split the data so that:

- the model learns from one part of the dataset
- evaluation happens on unseen data
- we get a more realistic understanding of performance

## Step 3. Separate Features And Target

Once we have `train` and `test`, we separate the feature columns from the target column.

The target column is:

```python
quality
```

So the feature and label split looks like this:

```python
train_x = train.drop(["quality"], axis=1)
test_x = test.drop(["quality"], axis=1)
train_y = train["quality"]
test_y = test["quality"]
```

## What This Means

At this stage:

- `train_x` contains the input features for training
- `train_y` contains the target values for training
- `test_x` contains the input features for testing
- `test_y` contains the target values for testing

## Step 4. Set Hyperparameters For ElasticNet

The model we are using is:

```python
ElasticNet
```

This model uses important hyperparameters such as:

- `alpha`
- `l1_ratio`

Instead of hardcoding them fully, we allow the values to be passed from the command line using `sys.argv`.

## How The Hyperparameters Are Read

The logic is roughly:

```python
alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
```

## Why This Is Useful

This design is helpful because:

- we can run experiments with different values easily
- the same script becomes reusable
- MLflow can log different runs with different hyperparameter combinations

## Default Values

If no command-line arguments are passed, the default values are:

- `alpha = 0.5`
- `l1_ratio = 0.5`

So the script can still run even if we do not provide manual inputs.

## Step 5. Start An MLflow Run

Before training the model, we start an MLflow run.

The main idea is:

```python
with mlflow.start_run():
    ...
```

Everything inside this block becomes part of one experiment run.

## Why This Step Is Important

Starting the run allows us to track:

- parameters
- metrics
- model artifacts
- metadata related to the training execution

## Step 6. Train The ElasticNet Model

Inside the MLflow run, we create and train the model.

The model initialization looks like this:

```python
lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
```

Then we train it using:

```python
lr.fit(train_x, train_y)
```

## Why `ElasticNet` Is Used

`ElasticNet` combines ideas from both:

- L1 regularization
- L2 regularization

So it is a useful example when we want a regression model with tunable regularization behavior.

## Step 7. Make Predictions

After fitting the model, we generate predictions on the test data.

The prediction step is:

```python
predicted_qualities = lr.predict(test_x)
```

These predictions will be compared with `test_y`.

## Step 8. Evaluate The Predictions

Once the predictions are ready, we call the helper function created earlier:

```python
rmse, mae, r2 = evaluate_metrics(test_y, predicted_qualities)
```

This gives us the three regression metrics:

- `RMSE`
- `MAE`
- `R2`

## Why These Metrics Matter

### RMSE

This tells us how much the predictions differ from the actual values, while penalizing large errors more strongly.

### MAE

This tells us the average absolute prediction error.

### R2

This tells us how well the model explains the variance in the target variable.

## Step 9. Print Basic Training Information

Before logging to MLflow, we also print some information to the console.

This usually includes:

- model name
- alpha value
- l1 ratio value
- RMSE
- MAE
- R2

## Why Printing Is Still Useful

Even though MLflow will store the run details, printing is still helpful because:

- we can quickly inspect the run output
- local debugging becomes easier
- we get instant feedback while testing the script

## Step 10. Log Parameters In MLflow

Now we start logging the hyperparameters.

The parameter logging looks like:

```python
mlflow.log_param("alpha", alpha)
mlflow.log_param("l1_ratio", l1_ratio)
```

## Why Log Parameters

Logging parameters is important because:

- every run may use different settings
- MLflow helps us compare runs later
- we can reproduce a run more easily if we know the exact inputs

## Step 11. Log Metrics In MLflow

After logging parameters, we log the evaluation metrics.

The metric logging looks like:

```python
mlflow.log_metric("rmse", rmse)
mlflow.log_metric("r2", r2)
mlflow.log_metric("mae", mae)
```

## Why Log Metrics

Logging metrics is important because:

- it lets us compare model performance across runs
- we can identify better hyperparameter combinations
- it gives us a clean experiment history inside MLflow

## Step 12. Prepare The Remote Tracking URI

This is one of the most important parts of the code.

We create a variable for the remote MLflow tracking server:

```python
remote_server_uri = ""
```

At this stage, it is kept blank because the AWS setup is not finished yet.

Later, this variable will store the public tracking URI of the MLflow server running on `AWS EC2`.

## Set The Tracking URI

Once the remote server exists, we will connect MLflow to it using:

```python
mlflow.set_tracking_uri(remote_server_uri)
```

This tells MLflow where the run information should be sent.

## Why This Step Matters

Without setting the tracking URI:

- runs stay local by default
- they do not go to the AWS-hosted MLflow server
- remote experiment tracking will not work

## Step 13. Check The Tracking Store Type

After setting the tracking URI, we inspect the URI type using `urlparse`.

The general idea is:

```python
tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
```

## Why We Check The Scheme

This helps us understand the type of backend store being used.

For example:

- `file` means a local file-based store
- another scheme can indicate a remote backend

This check is used to decide how the model should be logged.

## Step 14. Log The Model

Now we log the trained model using:

```python
mlflow.sklearn.log_model(...)
```

There are two cases here.

### Case 1. Tracking Store Is Not `file`

If the tracking backend is not file-based, we can log the model with a registered model name.

The idea is:

```python
mlflow.sklearn.log_model(
    lr,
    "model",
    registered_model_name="ElasticnetWineModel"
)
```

This is useful when we are working with a remote MLflow server that supports model registration.

### Case 2. Tracking Store Is `file`

If the tracking backend is local and file-based, we log the model without registering it:

```python
mlflow.sklearn.log_model(lr, "model")
```

## Why This Conditional Logging Is Useful

This makes the script more flexible because:

- it can work with local MLflow tracking
- it can also work with remote MLflow tracking
- the code does not need to be rewritten for both cases

## High-Level Code Structure

The full structure inside `app.py` now looks like this:

```python
if __name__ == "__main__":
    # 1. Read dataset
    # 2. Split dataset
    # 3. Separate features and target
    # 4. Read alpha and l1_ratio
    # 5. Start MLflow run
    # 6. Train ElasticNet
    # 7. Predict
    # 8. Evaluate metrics
    # 9. Log params
    # 10. Log metrics
    # 11. Set tracking URI
    # 12. Log model
```

## What We Complete At This Stage

By the end of this part, we have:

- finished the core training logic inside `app.py`
- connected model training with MLflow logging
- prepared the script to accept hyperparameters from the command line
- added support for both local and remote tracking behavior
- kept a placeholder for the AWS tracking URI

## Why This Part Is Important

This part is the bridge between:

- simple ML model training
- and real experiment tracking with MLflow

Without this logic:

- there would be no structured experiment run
- parameters and metrics would not be stored properly
- the AWS MLflow setup in the next step would have nothing useful to track

## Step 15. Update The Project README For AWS Steps

After the code is completed, we also start documenting the upcoming AWS setup steps inside the project `README.md`.

This is useful because:

- the AWS process has multiple steps
- keeping them written down helps us follow them in order
- the project becomes easier to revisit later

The README at this point starts acting like a checklist for:

- AWS login
- IAM user creation
- EC2 setup
- S3 setup
- commands that must run inside the EC2 machine

## Commands And Functions We Want To Remember

### Read CSV With Separator

```python
pd.read_csv(csv_url, sep=";")
```

### Train-Test Split

```python
train, test = train_test_split(data)
```

### Feature / Target Split

```python
train_x = train.drop(["quality"], axis=1)
test_x = test.drop(["quality"], axis=1)
train_y = train["quality"]
test_y = test["quality"]
```

### Default Hyperparameters

```python
alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
```

### Start MLflow Run

```python
with mlflow.start_run():
```

### Log Parameters

```python
mlflow.log_param("alpha", alpha)
mlflow.log_param("l1_ratio", l1_ratio)
```

### Log Metrics

```python
mlflow.log_metric("rmse", rmse)
mlflow.log_metric("r2", r2)
mlflow.log_metric("mae", mae)
```

### Set Remote Tracking URI

```python
mlflow.set_tracking_uri(remote_server_uri)
```

### Log Model

```python
mlflow.sklearn.log_model(lr, "model")
```

## One-Line Summary

Here we complete the end-to-end ML training script by reading the dataset, training an `ElasticNet` model, evaluating it, logging everything with `MLflow`, and preparing the code for AWS-based remote tracking.
