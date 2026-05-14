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

What I understood:

1. Load params from `params.yaml`
2. Read evaluation data
3. Load saved model from disk
4. Predict on input data
5. Compute accuracy
6. Log evaluation metric to MLflow

## Why Separate Evaluation Is Useful

Keeping evaluation in a different script is helpful because:

- the pipeline becomes modular
- each step has one responsibility
- DVC can run each stage clearly
- later I can swap evaluation logic without changing training

## Important Concept

Evaluation can also be done on new data.

So this stage is not only for training-time checking.

It can also represent:

- post-training validation
- batch evaluation
- performance checking on fresh data

## My Practical Reminder

If I use new data for evaluation later, I should make sure:

- feature columns match training input
- target column naming stays consistent
- the same preprocessing assumptions are followed

