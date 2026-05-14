# End-to-End Machine Learning Experiment Tracking Using MLflow

### Project Overview

This project demonstrates an **end-to-end machine learning workflow** integrated with **MLflow** to track experiments, parameters, metrics, and model artifacts. The objective is to showcase how **MLOps practices** can be applied to manage, compare, and reproduce machine learning experiments efficiently.

The project uses the **Iris dataset** and trains a **Logistic Regression** model using **scikit-learn**, while MLflow is used as the experiment tracking and model management framework.

<br/>

### Key Objectives

* Build and train a machine learning model
* Track hyperparameters, metrics, and metadata using MLflow
* Log trained models and artifacts
* Compare multiple experiments to select the best-performing model
* Understand MLflow tracking, runs, experiments, and artifacts

<br/>

### Tech Stack

* Python
* scikit-learn
* pandas, NumPy
* MLflow
* Jupyter Notebook

<br/>

### Dataset

* **Iris Dataset** (available via `sklearn.datasets`)
* Features:

  * Sepal Length
  * Sepal Width
  * Petal Length
  * Petal Width
* Target:

  * Flower class (3 classes)

<br/>

### Workflow

1. Load the Iris dataset
2. Split data into training and test sets
3. Train a Logistic Regression model
4. Evaluate model performance using accuracy
5. Configure MLflow tracking server (local)
6. Log:

   * Hyperparameters
   * Metrics
   * Tags
   * Model artifacts
7. Run multiple experiments with different hyperparameters
8. Compare experiments using MLflow UI

<br/>

### MLflow Features Demonstrated

* Experiment creation and management
* Parameter logging (`log_param`)
* Metric logging (`log_metric`)
* Tagging experiments
* Model signature inference
* Model and artifact logging
* Experiment comparison via MLflow UI

<br/>

### Experiment Tracking

Each experiment logs:

* Model hyperparameters (solver, penalty, random state, etc.)
* Accuracy metric
* Model artifacts (pickle file, environment files, dependencies)
* Metadata and tags for easy identification

Multiple runs can be compared in the MLflow UI to select the best-performing configuration.

<br/>

### Model Management

* Models are logged using `mlflow.sklearn.log_model`
* Input–output schema is captured using `infer_signature`
* Artifacts include:

  * Serialized model (`model.pkl`)
  * Environment configuration
  * Dependency files

<br/>

### Running the Project

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start MLflow tracking server:

   ```bash
   mlflow ui
   ```

3. Run the Jupyter Notebook to train models and log experiments.

4. Open MLflow UI in browser:

   ```
   http://127.0.0.1:5000
   ```

<br/>

### Use Cases

* Learning MLflow and MLOps fundamentals
* Experiment tracking and reproducibility
* Hyperparameter comparison
* Model versioning and artifact management

<br/>

### Conclusion

This project provides a practical introduction to **MLflow-based experiment tracking** and **MLOps workflows**, demonstrating how machine learning experiments can be systematically managed, compared, and reproduced. It serves as a strong foundation for scaling ML systems toward production environments.


