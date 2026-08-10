# Implementing End-to-End MLflow Code

## Main Flow Of The Code

The end-to-end flow in this part looks like this:

`read dataset -> split data -> train ElasticNet -> predict -> evaluate -> log params and metrics -> prepare remote tracking`

<br/>

## Steps:

### Step 1. Read The Dataset

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

So this is a supervised learning problem where we want to predict the **wine quality** using the given features.

#### Code:

```python
csv_url = "..."
try:
    data = pd.read_csv(csv_url, sep=";")
except Exception as e:
    logger.exception("Unable to download the data")
    raise e
```

We wrap the dataset-loading logic inside a `try-except` block.

This helps because:

- the URL may be wrong
- the file may not be reachable
- network issues can happen
- data ingestion errors should be logged clearly

### Step 2. Split The Data Into Train And Test

After loading the data, the next step is to split it into train and test sets.

For that we use:

```python
train, test = train_test_split(data)
```

Since no explicit split ratio is provided, the default behavior is used.

That means:

- `75%` of the data goes to training
- `25%` of the data goes to testing

### Step 3. Separate Features And Target

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

### Step 4. Set Hyperparameters For ElasticNet

The model we are using is:

```python
ElasticNet
```

This model uses important hyperparameters such as:

- `alpha`
- `l1_ratio`

Instead of hardcoding them fully, we allow the values to be passed from the command line using `sys.argv`.

The logic is roughly:

```python
alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
```

#### Why This Is Useful?

This design is helpful because:

- we can run experiments with different values easily
- the same script becomes reusable
- MLflow can log different runs with different hyperparameter combinations

#### Default Values

If no command-line arguments are passed, the default values are:

- `alpha = 0.5`
- `l1_ratio = 0.5`

So the script can still run even if we do not provide manual inputs.

### Step 5. Start An MLflow Run

Before training the model, we start an MLflow run.

```python
with mlflow.start_run():
    ...
```

### Step 6. Train The ElasticNet Model

Inside the MLflow run, we create and train the model.

The model initialization looks like this:

```python
lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
```

Then we train it using:

```python
lr.fit(train_x, train_y)
```

### Step 7. Make Predictions

After fitting the model, we generate predictions on the test data.

The prediction step is:

```python
predicted_qualities = lr.predict(test_x)
```

### Step 8. Evaluate The Predictions

Once the predictions are ready, we call the helper function created earlier:

```python
rmse, mae, r2 = evaluate_metrics(test_y, predicted_qualities)
```

## Step 9. Log Parameters In MLflow

Now we start logging the hyperparameters.

The parameter logging looks like:

```python
mlflow.log_param("alpha", alpha)
mlflow.log_param("l1_ratio", l1_ratio)
```

### Step 10. Log Metrics In MLflow

After logging parameters, we log the evaluation metrics.

The metric logging looks like:

```python
mlflow.log_metric("rmse", rmse)
mlflow.log_metric("r2", r2)
mlflow.log_metric("mae", mae)
```

### Step 11. Prepare The Remote Tracking URI

This is one of the most important parts of the code.

We create a variable for the remote MLflow tracking server:

```python
remote_server_uri = ""
```

At this stage, it is kept blank because the AWS setup is not finished yet.

Later, this variable will store the public tracking URI of the MLflow server running on `AWS EC2`.

#### Set The Tracking URI

Once the remote server exists, we will connect MLflow to it using:

```python
mlflow.set_tracking_uri(remote_server_uri)
```

This tells MLflow where the run information should be sent.

### Step 12. Check The Tracking Store Type

After setting the tracking URI, we inspect the URI type using `urlparse`.

The general idea is:

```python
tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
```

### Step 13. Log The Model

Now we log the trained model using:

```python
mlflow.sklearn.log_model(...)
```

<br/>

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

<br/>

## One-Line Summary

Here we complete the end-to-end ML training script by reading the dataset, training an `ElasticNet` model, evaluating it, logging everything with `MLflow`, and preparing the code for AWS-based remote tracking.
