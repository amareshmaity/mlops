# ML Pipeline with DVC, MLflow, and DagsHub

This folder contains my study material for building an end-to-end machine learning pipeline using `DVC`, `MLflow`, and `DagsHub`.

The project idea is based on the Pima Indians Diabetes dataset and follows a simple but important ML workflow:

`raw data -> preprocessing -> model training -> evaluation -> experiment tracking -> versioning`

## What I Learn In This Module

In this module, I focus on how multiple MLOps tools work together in one project:

- `DVC` for data versioning, model versioning, and pipeline stages
- `MLflow` for experiment tracking
- `DagsHub` as the remote platform for collaboration and tracking
- `scikit-learn` for training a `RandomForestClassifier`

## Project Goal

The main goal is to understand how to structure an ML project so that:

- data changes can be tracked properly
- model artifacts can be versioned
- experiments can be logged and compared
- the pipeline can be reproduced easily

## Pipeline Stages

### 1. Data Preprocessing

The preprocessing step reads the raw dataset and prepares it for downstream stages.

Typical responsibilities:

- read the raw CSV
- create output directories if needed
- save processed data

### 2. Model Training

The training step:

- reads the prepared dataset
- splits features and target
- performs train-test split
- trains a `RandomForestClassifier`
- uses hyperparameter tuning with `GridSearchCV`
- saves the trained model

### 3. Experiment Tracking with MLflow

During training, MLflow is used to log:

- accuracy
- model parameters
- best hyperparameters
- confusion matrix
- classification report
- model artifacts

### 4. Evaluation

The evaluation step loads the saved model and calculates performance metrics on the selected dataset.

### 5. Pipeline Orchestration with DVC

The full workflow is connected through DVC stages so the project can run as a reproducible pipeline.

Main stages:

- `preprocess`
- `train`
- `evaluate`

## Folder Contents

Right now, this folder contains the learning material for the project:

```text
06-ML_Pipeline/
|-- README.md
|-- notes/
|   |-- 00-study-roadmap.md
|   |-- 01-project-overview-and-setup.md
|   |-- 02-params-and-preprocessing.md
|   |-- 03-training-pipeline.md
|   |-- 04-mlflow-experiment-tracking.md
|   |-- 05-evaluation-pipeline.md
|   |-- 06-dvc-pipeline-orchestration.md
|   `-- 07-quick-revision-cheatsheet.md

```

## Notes Structure

I created topic-wise notes for easier revision:

- `00-study-roadmap.md` gives the learning flow
- `01-project-overview-and-setup.md` explains the project setup
- `02-params-and-preprocessing.md` covers config and preprocessing
- `03-training-pipeline.md` explains model training
- `04-mlflow-experiment-tracking.md` covers MLflow logging
- `05-evaluation-pipeline.md` explains model evaluation
- `06-dvc-pipeline-orchestration.md` explains DVC stages
- `07-quick-revision-cheatsheet.md` is a short recap file

## Important Commands From This Module

Initialize DVC:

```bash
dvc init
```

Track raw data:

```bash
dvc add data/raw/data.csv
```

Add preprocessing stage:

```bash
dvc stage add -n preprocess \
    -p preprocess.input,preprocess.output \
    -d src/preprocess.py -d data/raw/data.csv \
    -o data/processed/data.csv \
    python src/preprocess.py
```

Add training stage:

```bash
dvc stage add -n train \
    -p train.data,train.model,train.random_state,train.n_estimators,train.max_depth \
    -d src/train.py -d data/processed/data.csv \
    -o models/model.pkl \
    python src/train.py
```

Add evaluation stage:

```bash
dvc stage add -n evaluate \
    -d src/evaluate.py -d models/model.pkl -d data/processed/data.csv \
    python src/evaluate.py
```

Run the full pipeline:

```bash
dvc repro
```

## Tech Stack

- `Python`
- `Pandas`
- `scikit-learn`
- `DVC`
- `MLflow`
- `DagsHub`

## Final Summary

This module is a practical introduction to building a reproducible ML pipeline with modern MLOps tools.

The biggest takeaway for me is understanding the role of each tool:

- Git tracks code
- DVC tracks data and pipeline outputs
- MLflow tracks experiments
- DagsHub brings everything together remotely


<br/>

Project like in the dagshub: https://dagshub.com/amaresh/mlpipeline