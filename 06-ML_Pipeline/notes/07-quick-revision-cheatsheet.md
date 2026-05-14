# Quick Revision Cheatsheet

## One-Line Summary

This module shows how to build an end-to-end ML pipeline using `DVC + MLflow + DagsHub`.

## Core Pipeline

```text
raw data -> preprocess -> train -> evaluate
```

## Main Files

- `README.md`
- `params.yaml`
- `src/preprocess.py`
- `src/train.py`
- `src/evaluate.py`
- `dvc.yaml`

## Main Responsibilities

- `preprocess.py` prepares data
- `train.py` trains and logs the best model
- `evaluate.py` checks model performance
- `params.yaml` stores config values
- `dvc.yaml` defines the pipeline stages

## What DVC Does Here

- tracks raw data
- tracks model artifacts
- creates pipeline stages
- helps rerun stages only when needed

## What MLflow Does Here

- logs metrics
- logs parameters
- logs artifacts
- registers the trained model

## Important Commands To Remember

Initialize DVC:

```bash
dvc init
```

Track data:

```bash
dvc add data/raw/data.csv
```

Run pipeline:

```bash
dvc repro
```

Push DVC artifacts:

```bash
dvc push -r origin
```

Push code:

```bash
git push origin main
```

## Most Important Interview / Revision Points

- DVC is used for data and model versioning
- MLflow is used for experiment tracking
- DagsHub can act as remote storage plus experiment UI
- `params.yaml` makes config easier to manage
- DVC stages convert scripts into a reproducible pipeline
- `dvc repro` runs the workflow in dependency order

## My Final Understanding

This module is a very good beginner-friendly example of how MLOps tools fit together in one practical project.

