# ML Pipeline Notes Roadmap

These are my structured notes for the `06-ML_Pipeline` module.

I organized them topic-wise so revision becomes easy.

## Reading Order

1. `01-project-overview-and-setup.md`
2. `02-params-and-preprocessing.md`
3. `03-training-pipeline.md`
4. `04-mlflow-experiment-tracking.md`
5. `05-evaluation-pipeline.md`
6. `06-dvc-pipeline-orchestration.md`
7. `07-quick-revision-cheatsheet.md`

## Main Goal Of This Module

In this module I am building an end-to-end ML pipeline where:

- DVC is used for data versioning and pipeline stages
- MLflow is used for experiment tracking
- DagsHub is used as the remote platform
- the model is a `RandomForestClassifier`
- the dataset is the Pima Indians Diabetes dataset

## Overall Flow I Need To Remember

`raw data -> preprocess -> train -> evaluate -> track everything`

## Important Personal Reminder

While coding in the transcript, some file paths were adjusted during the explanation.

So in my own implementation, I should keep the paths consistent in:

- `params.yaml`
- `src/preprocess.py`
- `src/train.py`
- `src/evaluate.py`
- `dvc.yaml`

