# AWS MLflow Tracking Notes

These are our notes for learning how to track ML experiments with `MLflow` on `AWS` using an `EC2` instance and an `S3 bucket`.

## Course Structure

### 1. Introduction to MLflow in AWS

What we want to understand here:

- why we may want to move MLflow tracking from `DagsHub` to `AWS`
- how `EC2` fits into MLflow tracking
- what the overall AWS-based tracking architecture looks like
- what problem this setup solves in real projects

### 2. MLflow Project Setup

What we want to cover here:

- creating the local project folder
- setting up a virtual environment with `conda`
- creating `requirements.txt`
- installing core libraries like `mlflow`, `scikit-learn`, and `boto3`
- creating starter files like `app.py` and `README.md`
- adding imports, logging, and metric helper functions

### 3. Implementing End-to-End MLflow Code

What we want to cover here:

- reading the Wine Quality dataset from a remote CSV URL
- splitting the dataset into train and test sets
- preparing features and target
- training an `ElasticNet` model
- taking `alpha` and `l1_ratio` from command-line arguments
- logging parameters, metrics, and the trained model with `MLflow`
- preparing the code for a remote tracking server

### 4. AWS Cloud Setup for MLflow Tracking

What we want to cover here:

- creating an `IAM` user
- generating access keys
- configuring local credentials with `aws configure`
- creating an `S3 bucket` for MLflow artifacts
- launching an `EC2` instance
- opening port `5000` for the MLflow UI
- preparing the EC2 environment for MLflow

### 5. Tracking Experiments from EC2 with S3

What we want to cover here:

- connecting to the `EC2` instance
- installing required tools on the server
- configuring AWS credentials on the machine
- starting the MLflow tracking server
- setting the default artifact location to `S3`
- opening the MLflow UI through the public IP and port `5000`
- updating the local application with the remote tracking URI
- sending experiment logs from `app.py` to AWS
- checking artifacts in both `MLflow UI` and `S3`
- cleaning up AWS resources after practice

## Planned Notes Layout

- `01-introduction-to-mlflow-in-aws.md`
- `02-mlflow-project-setup.md`
- `03-implementing-end-to-end-mlflow.md`
- `04-aws-cloud-setup-for-mlflow-tracking.md`
- `05-ec2-instance-tracking-with-s3.md`
- `06-quick-revision.md`
