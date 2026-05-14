# MLflow 
## What is MLflow?

MLflow is an **open-source MLOps platform** designed to manage the **end-to-end lifecycle of machine learning projects**. It provides tooling to track experiments, manage models, handle dependencies, and support deployment and monitoring across the entire data science workflow.

![alt text](Images/ml-workflow.png)

<br/>

## Data Science Project Lifecycle (Context for MLflow)

A typical data science project follows the below lifecycle:

1. **Data Preparation**

   * Data collection via APIs, databases, paid data sources
   * ETL pipelines created by Data Engineers
   * Data stored in databases (e.g., MongoDB)

2. **Exploratory Data Analysis (EDA)**

   * Statistical analysis
   * Hypothesis testing
   * Understanding data distributions and relationships

3. **Feature Engineering**

   * Handling missing values
   * Encoding categorical variables
   * Dealing with imbalanced datasets
   * Feature transformations

4. **Model Training**

   * Training multiple models
   * Hyperparameter tuning
   * Comparing algorithms

5. **Model Validation**

   * Evaluating models using performance metrics
   * Overlap of responsibilities between Data Scientists and ML Engineers

6. **Deployment**

   * Deploying models to cloud platforms (AWS, GCP, Azure)
   * Ensuring scalability and reliability

7. **Monitoring**

   * Monitoring model performance
   * Detecting data drift
   * Deciding when retraining is required

<br/>

## Roles Across the Lifecycle

| Role                             | Key Responsibilities                                       |
| -------------------------------- | ---------------------------------------------------------- |
| Data Engineer                    | Data preparation, ETL pipelines                            |
| Data Scientist                   | EDA, Feature Engineering, Model Training, Model Validation |
| ML Engineer / MLOps Professional | Model Validation, Deployment, Monitoring                   |
| Data Governance Officer          | Involved across all stages                                 |

<br/>

## 4. Why MLflow is Needed

In real-world projects:

* Multiple experiments are conducted
* Multiple models and hyperparameter combinations are tested
* Results must be reproducible, versioned, and comparable
* Collaboration across teams is required

MLflow acts as a **central system of record** for all these activities.

<br/>

## How Data Scientists Leverage MLflow

### 1. Experiment Tracking and Hypothesis Testing

* Tracks experiments across:

  * EDA
  * Feature engineering
  * Model training
  * Model validation
* Logs:

  * Parameters
  * Metrics
  * Results of statistical tests
* Supports versioning and reproducibility

Use case example:

* Tracking multiple statistical analyses during EDA
* Comparing results of different feature engineering strategies

<br/>

### 2. Code Structuring and Pipeline Creation

* Encourages structured pipelines for:

  * EDA
  * Feature Engineering
  * Model Training
  * Model Validation
* Improves maintainability compared to ad-hoc scripts

<br/>

### 3. Model Packaging and Dependency Management

* Packages models along with dependencies
* Manages environments more efficiently than traditional setup.py-based workflows
* Ensures reproducibility across systems

<br/>

### 4. Hyperparameter Tuning and Evaluation (Strongest Feature)

* Tracks hyperparameter tuning experiments automatically
* Logs:

  * Each hyperparameter combination
  * Corresponding metrics
* Integrates with techniques like GridSearchCV
* Provides visualizations for comparison

Benefits:

* Easy comparison of models
* Selection of optimal model for deployment
* Tracking model performance over time

<br/>

## How MLOps Professionals / ML Engineers Use MLflow

### 1. Model Lifecycle Management

* Manage trained models **pre- and post-deployment**
* Handle:

  * Model versioning
  * Promotion from staging to production
  * Model Registry

<br/>

### 2. Secure Model Deployment

* Deploy models to production environments
* Ensure scalability and reliability

<br/>

### 3. Deployment Dependency Management

* Manage runtime dependencies
* Ensure consistency between training and production environments

<br/>

## MLflow and Generative AI (Recent Extension)

MLflow now supports **Generative AI workflows**, including:

* Experiment tracking for Large Language Models (LLMs)
* Prompt engineering experimentation
* Comparing:

  * Different prompts
  * Different base LLMs
* Selecting best base model
* Supporting fine-tuning based on project requirements

<br/>

## Core Use Cases of MLflow

### 1. Experiment Tracking

* Tracks:

  * Parameters
  * Metrics (log loss, R², accuracy, etc.)
* Centralized tracking via **MLflow UI**

<br/>

### 2.  Model Selection and Deployment

* MLOps engineers use MLflow UI to:

  * Compare experiments
  * Identify top-performing models
  * Deploy selected models

<br/>

### 3. Model Performance Monitoring

* Monitor deployed model performance
* Track degradation and drift

<br/>

### 4. Team Collaboration

* Shared UI for all experiments
* Enables collaboration among:

  * Data Scientists
  * ML Engineers
  * Other stakeholders

<br/>

## MLflow in Practice (High-Level Flow)

1. During Model Training:

   * Track accuracy, error, train/test metrics

2. During Model Validation:

   * Identify best-performing model

3. Using MLflow UI:

   * Visualize all experiments

4. MLOps Engineer:

   * Reviews UI
   * Selects best model
   * Deploys to production

<br/>

## Summary

MLflow provides:

* End-to-end lifecycle management
* Strong experiment tracking
* Robust hyperparameter evaluation
* Model registry and deployment support
* Collaboration-friendly UI
* Support for both traditional ML and Generative AI workflows

It serves as a foundational MLOps platform for production-grade machine learning systems.

