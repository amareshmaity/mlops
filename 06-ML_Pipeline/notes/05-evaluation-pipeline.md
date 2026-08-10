# Evaluation Pipeline Notes

## Purpose Of `evaluate.py`

The evaluation script is used to check model performance after training.

It reads:

- the data
- the saved model

Then it predicts and logs evaluation accuracy.

## Libraries Used

- `pandas`
- `pickle`
- `yaml`
- `os`
- `mlflow`
- `sklearn.metrics.accuracy_score`

## Flow Inside Evaluation

What you will understand:

1. Load params from `params.yaml`
2. Read evaluation data
3. Load saved model from disk
4. Predict on input data
5. Compute accuracy
6. Log evaluation metric to MLflow



