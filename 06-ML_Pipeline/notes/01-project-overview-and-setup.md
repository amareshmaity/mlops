# Project Overview And Setup

## What This Project Is About

This project is a simple end-to-end machine learning pipeline.

The main idea is:

- take raw data
- preprocess it
- train a model
- evaluate the model
- version data and models with DVC
- track experiments with MLflow

## Tools Used

- `Python`
- `scikit-learn`
- `DVC`
- `MLflow`
- `DagsHub`

## Problem Statement

The dataset used is the Pima Indians Diabetes dataset.

The input features are things like:

- pregnancies
- glucose
- blood pressure
- skin thickness
- insulin
- BMI
- diabetes pedigree function
- age

The target column is:

- `Outcome`

This is a binary classification problem.

My model has to predict whether a person is likely to have diabetes or not.

## Why This Project Is Important

This project is not only about training a model.

It is mainly about learning how to manage an ML workflow properly.

What I understood:

- Git tracks code
- DVC tracks data and model artifacts
- MLflow tracks runs, metrics, parameters, and artifacts
- DagsHub gives one place to connect all of them

## Initial Project Setup

The flow shown in the module is:

1. Create a new DagsHub repository `mlpipeline`
2. Clone it locally
3. Open it in VS Code
4. Add `README.md`
5. Commit and push initial code

## Basic Folder Structure

The project structure becomes something like this:

```text
mlpipeline/
├── README.md
├── requirements.txt
├── .gitignore
├── params.yaml
├── data/
│   ├── raw/
│   │   └── data.csv
│   └── processed/ or preprocessed/
├── models/
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
└── dvc.yaml
```

## Environment Setup I Need To Remember

Create environment:

```bash
conda create -p venv python==3.12 -y
```

Install requirements:

```bash
pip install -r requirements.txt
```

Important packages mentioned:

- `dvc`
- `dvc[s3]` or `dvc-s3`
- `dagshub`
- `mlflow`
- `scikit-learn`

## My Understanding Of The Full Workflow

This module starts from project setup, then moves to code, then to tracking, and finally to pipeline automation.

So the real learning sequence is:

`setup -> script creation -> model logging -> DVC pipeline -> remote sync`

