# MLOps Notes

This repository is a structured learning workspace for understanding `MLOps` from the ground up. The goal of the root notes is to explain the main ideas behind MLOps clearly and connect the different topics covered in the folders of this repo.

These notes focus on:

- definitions
- core concepts
- lifecycle understanding
- practical workflow thinking
- how the main MLOps pieces fit together

They do not go deep into every individual tool because separate notes for topics such as `MLflow`, `DVC`, `DagsHub`, `Docker`, `Airflow`, `AWS`, and `GitHub Actions` already exist in their own folders.

## What Is MLOps?

`MLOps` stands for `Machine Learning Operations`.

It is a set of practices used to build, manage, deploy, monitor, and improve machine learning systems in a reliable and repeatable way.

In simple terms:

- `Machine Learning` helps us create predictive or intelligent models
- `Operations` helps us run those models consistently in real environments
- `MLOps` brings both sides together

MLOps can be thought of as the discipline that turns a machine learning experiment into a maintainable system.

## Why MLOps Is Needed

A machine learning project is rarely just about writing training code once.

Real projects usually involve:

- changing datasets
- multiple experiments
- many hyperparameter combinations
- model comparison
- dependency management
- collaboration across people and teams
- deployment to real environments
- monitoring after deployment
- retraining when performance drops

Without MLOps, teams often face problems such as:

- "works on my machine" issues
- no clear record of which dataset version was used
- no tracking of which parameters produced the best model
- confusion about which model is currently deployed
- manual retraining steps
- deployment inconsistency
- no visibility into failures

MLOps exists to reduce this chaos and make ML systems reproducible, observable, and easier to operate.

## MLOps Is More Than Model Training

A common beginner mistake is to think that machine learning ends after a model achieves good accuracy.

In practice, the model is only one part of a larger system.

An actual ML solution usually includes:

- data collection
- ETL or data ingestion
- preprocessing
- feature engineering
- model training
- evaluation
- experiment tracking
- artifact storage
- deployment
- monitoring
- retraining

So MLOps is not only about building models. It is about managing the entire lifecycle around the model.

## How MLOps Differs From Traditional Software Operations

Traditional software systems mostly focus on:

- source code
- application logic
- testing
- deployment

MLOps includes all of that, but also introduces additional moving parts:

- data versions
- feature changes
- model artifacts
- experiment history
- training pipelines
- performance drift
- retraining triggers

This means ML systems are harder to manage than normal software systems because behavior depends not only on code, but also on data and model state.

## Core Goal of MLOps

The core goal of MLOps is to create a system where machine learning work becomes:

- reproducible
- versioned
- automated
- testable
- deployable
- monitorable
- collaborative

If a team can answer questions like the following, their MLOps maturity is improving:

- Which code version produced this model?
- Which dataset version was used?
- Which parameters were chosen?
- What metrics did the model achieve?
- Where is the model stored?
- How was it deployed?
- How do we know if it is still performing well?
- When should retraining happen?

## End-to-End MLOps Lifecycle

The folders in this repository collectively point to a full MLOps lifecycle like this:

1. Problem understanding
2. Data collection
3. Data preparation
4. Experimentation and model development
5. Model evaluation
6. Versioning and tracking
7. Packaging and environment management
8. Workflow orchestration
9. Deployment
10. Monitoring
11. Retraining and continuous improvement

## 1. Problem Understanding

Every ML project starts with a business or product problem.

Examples:

- predict house prices
- classify flowers
- forecast demand
- detect fraud
- automate a data pipeline

At this stage, the team defines:

- the objective
- the target variable
- the success metric
- the expected business outcome

This stage matters because a model with good technical metrics is still not useful if it does not solve the real problem.

## 2. Data Collection and ETL

Machine learning depends on data.

That data may come from:

- APIs
- databases
- files
- cloud storage
- IoT systems
- third-party sources

This is where `ETL` becomes important.

`ETL` means:

- `Extract`: collect data from source systems
- `Transform`: clean, validate, reshape, and combine data
- `Load`: store prepared data in a usable destination

ETL is a foundational concept because good ML systems depend on reliable and repeatable data preparation.

## 3. Data Preparation and Feature Work

Once data is available, it usually must be prepared for modeling.

Typical activities include:

- handling missing values
- encoding categories
- scaling numeric data
- selecting useful columns
- splitting features and target
- creating training and testing datasets

This stage is important because model quality is heavily influenced by data quality and feature design.

## 4. Experimentation and Model Development

This is the part many people associate most strongly with machine learning.

Typical activities include:

- training different algorithms
- testing parameter combinations
- comparing results
- measuring model performance
- selecting the best candidate

This stage is not just about finding a high score. It is about building a traceable path from idea to result.

## 5. Evaluation

A trained model should not be accepted only because training completed successfully.

It should be evaluated using appropriate metrics such as:

- accuracy
- precision
- recall
- F1 score
- RMSE
- MAE
- R2

Evaluation helps answer:

- Is the model good enough?
- Is it better than the previous version?
- Is it stable enough for deployment?

## 6. Versioning and Tracking

One of the strongest ideas in MLOps is that code alone is not enough to reproduce a result.

A result often depends on:

- code version
- data version
- parameter values
- model artifact
- environment and dependencies

This is why versioning and tracking are central to MLOps.

At a concept level, a strong MLOps workflow should track:

- source code
- datasets
- model files
- pipeline configuration
- experiment metadata
- performance metrics

## 7. Packaging and Environment Consistency

A project that works only on one machine is not production-ready.

ML projects often depend on:

- specific Python versions
- libraries
- system packages
- runtime configuration

Environment consistency is important because the same model or pipeline should behave as predictably as possible across:

- local development
- testing
- staging
- production

This is why packaging and container-based thinking are important parts of MLOps.

## 8. Workflow Orchestration

As projects grow, ML and data workflows stop being single scripts.

Instead, they become multi-step pipelines such as:

`ingestion -> preprocessing -> training -> evaluation -> deployment`

Or:

`extract -> transform -> load -> validate -> trigger downstream job`

Workflow orchestration is the concept of:

- defining the order of tasks
- handling dependencies
- scheduling runs
- monitoring execution
- retrying failed steps

This becomes especially useful when pipelines must run repeatedly and reliably.

## 9. Deployment

A machine learning model creates value only when it is used in a real workflow.

Deployment can mean:

- exposing a prediction API
- running a batch scoring job
- serving a model inside an application
- pushing outputs into another system

The exact deployment style may differ, but the concept is the same: move the validated model into an environment where it can produce real outcomes.

## 10. Monitoring

Deployment is not the end of the lifecycle.

A deployed model must be observed over time.

Monitoring can involve:

- service health
- prediction latency
- error rate
- input data changes
- output quality
- performance degradation

This matters because real-world conditions change.

A model that was good during training may become weaker later because:

- data distributions shift
- user behavior changes
- the business process changes
- the environment changes

## 11. Retraining and Continuous Improvement

MLOps treats models as living assets rather than one-time deliverables.

That means teams should be prepared to:

- refresh data
- retrain models
- re-evaluate performance
- compare old and new versions
- redeploy only when improvement is confirmed

This makes MLOps a continuous loop rather than a one-time project.

## Core Concepts to Remember

### Reproducibility

If the same code, same data, and same configuration are used, the result should be reproducible.

### Versioning

Different versions of code, data, and models should be identifiable and restorable.

### Experiment Tracking

Every important run should capture enough metadata to understand what was tried and what outcome it produced.

### Pipeline Thinking

An ML project should be viewed as a sequence of connected stages, not a single notebook.

### Automation

Repeated manual steps should gradually become automated to reduce errors and save time.

### Observability

Teams should be able to see what happened, what failed, and what changed.

### Collaboration

MLOps should help data scientists, ML engineers, and platform teams work from a shared, understandable system.

## Main Artifacts in an MLOps Project

A mature ML workflow usually manages several artifact types:

- code
- data
- notebooks
- configuration files
- trained model files
- metrics
- plots
- logs
- workflow definitions
- deployment specifications

Each artifact tells part of the story of how the ML system was built and operated.

## Roles in an MLOps-Oriented Workflow

Different teams may participate at different stages:

- `Data Engineers` build and maintain data pipelines
- `Data Scientists` explore data and develop models
- `ML Engineers / MLOps Engineers` operationalize training, deployment, and monitoring
- `QA / Platform / DevOps teams` help with testing, environments, automation, and reliability

The exact boundaries change by company, but MLOps usually sits at the intersection of these roles.

## Practical Mental Model

A simple way to remember MLOps is to think in terms of controlled movement:

- move data from sources into usable form
- move experiments from ideas into measurable results
- move models from local files into managed artifacts
- move validated models into deployment environments
- move operational feedback back into retraining decisions

In that sense, MLOps is about managing flow with discipline.

## Common Problems MLOps Tries to Solve

- inconsistent environments
- missing experiment history
- confusion around dataset versions
- hard-to-repeat training runs
- manual pipeline execution
- fragile deployments
- lack of monitoring after release
- weak collaboration between data and engineering teams

## Relationship Between the Main Building Blocks

The folders in this repository cover a practical set of building blocks that commonly appear together:

- `Git` helps version source code and collaboration history
- `DVC` helps version data and large model artifacts
- `MLflow` helps track experiments and model metadata
- `DagsHub` helps organize collaboration around code, data, and experiments
- `Docker` helps package environments consistently
- `Airflow` helps orchestrate ETL and ML workflows
- `AWS` helps provide cloud infrastructure for storage and tracking
- `GitHub Actions` helps automate testing and workflow execution

The important idea is not to memorize tools separately, but to understand the role each category plays in the larger system.

## High-Level Workflow Across This Repository

The learning path across this repo can be summarized like this:

`MLOps basics -> experiment tracking -> data versioning -> pipeline design -> cloud tracking -> containerization -> orchestration -> ETL automation -> CI/CD automation`

That sequence reflects how ML projects evolve from local experimentation toward more production-oriented systems.

## How This Repository Is Organized

This repo is arranged as topic-wise study modules:

- [01-MLFLOW_Intro](./01-MLFLOW_Intro) for MLflow fundamentals and tracking concepts
- [02-ML_MLFLOW](./02-ML_MLFLOW) for practical MLflow-based ML experiments
- [03-DL_MLFLOW](./03-DL_MLFLOW) for deep learning work with MLflow notebooks
- [04-DVC](./04-DVC) for data versioning concepts and workflows
- [05-Dagshub](./05-Dagshub) for collaboration-oriented MLOps workflow ideas
- [06-ML_Pipeline](./06-ML_Pipeline) for pipeline structure and reproducible training flow
- [07-AWS_MLFLOW_Tracking](./07-AWS_MLFLOW_Tracking) for cloud-based experiment tracking
- [08-Docker](./08-Docker) for environment packaging and container-based workflows
- [09-Airflow](./09-Airflow) for orchestration concepts in ML systems
- [10-Airflow_ETL_Pipeline](./10-Airflow_ETL_Pipeline) for ETL workflow thinking and implementation
- [11_Github_Action](./11_Github_Action) for CI/CD and workflow automation concepts

## Final Understanding

MLOps is best understood as the operating system around machine learning work.

It brings structure to the full ML lifecycle by making data, experiments, models, environments, pipelines, and deployments easier to manage together.

If machine learning answers the question "how do we build a model?", MLOps answers the larger question:

"How do we build, run, improve, and trust the full system around that model over time?"
