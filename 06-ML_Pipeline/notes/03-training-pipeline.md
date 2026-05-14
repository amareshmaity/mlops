# Training Pipeline Notes

## Main Goal Of `train.py`

The training script does much more than just fit a model.

It is responsible for:

- reading training data
- splitting features and target
- doing train-test split
- performing hyperparameter tuning
- selecting the best model
- calculating metrics
- saving the model
- logging everything to MLflow

## Libraries Used

- `pandas`
- `pickle`
- `yaml`
- `os`
- `mlflow`
- `sklearn.ensemble.RandomForestClassifier`
- `sklearn.model_selection.train_test_split`
- `sklearn.model_selection.GridSearchCV`
- `sklearn.metrics`

## Model Used

The model used is:

```python
RandomForestClassifier()
```

## Main Training Flow

This is the sequence I should remember:

1. Load parameters from `params.yaml`
2. Read the dataset
3. Separate input and target
4. Split data into train and test
5. Define hyperparameter grid
6. Run `GridSearchCV`
7. Get best estimator
8. Predict on test data
9. Calculate accuracy
10. Save the trained model as pickle

## Hyperparameters Tried

The transcript experiments with a grid similar to:

- `n_estimators`: `100`, `200`
- `max_depth`: `5`, `10`, `None`
- `min_samples_split`: `2`, `5`
- `min_samples_leaf`: `1`, `2`

## Why `GridSearchCV` Is Used

This is done to test multiple parameter combinations automatically.

So instead of guessing one configuration, the model selection becomes more systematic.

## Metrics Mentioned

The training step calculates:

- accuracy
- confusion matrix
- classification report

## Model Saving

After training, the best model is saved using `pickle`.

Example target path:

```text
models/model.pkl
```

## Important Practical Note

One thing I noticed in the transcript:

Sometimes the training script reads the raw file, and sometimes the processed file is intended.

So in my version, I should keep one consistent design:

- either train from processed data
- or keep preprocessing lightweight but still use its output

Otherwise the pipeline logic becomes confusing.

