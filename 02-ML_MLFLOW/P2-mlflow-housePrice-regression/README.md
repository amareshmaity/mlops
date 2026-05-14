# MLflow-Based Experiment Tracking for House Price Prediction

<br/>

### Project Overview
This project focuses on building a **machine learning experimentation workflow** using **MLflow** for systematic tracking of models, hyperparameters, and evaluation metrics. The use case is a **house price prediction problem**, where multiple experiments will be conducted and compared to identify the best-performing model.

The primary objective is to apply **MLOps best practices** such as experiment tracking, reproducibility, and model management while working on a real-world regression dataset.

<br/>

### Problem Statement
Predict the **median house value** based on several numerical features related to housing, population, and location.  
The challenge is not only to build a model, but also to **track and compare multiple training runs** efficiently.

<br/>

### Dataset
The project uses the **California Housing Dataset**, available through `sklearn.datasets`.

#### Input Features
- Housing median age  
- Average number of rooms  
- Average number of bedrooms  
- Population  
- Average occupancy  
- Latitude  
- Longitude  

#### Target Variable
- Median house value (used as house price)

<br/>


### Tech Stack
- Python  
- Jupyter Notebook  
- pandas  
- scikit-learn  
- MLflow  

<br/>


### Project Goals
- Prepare a clean and structured dataset for modeling
- Perform **hyperparameter tuning** using GridSearchCV
- Log all experiments, parameters, and metrics using MLflow
- Compare multiple runs using the MLflow UI
- Identify and register the best-performing model

<br/>


### Data Preparation
1. Load the California Housing dataset
2. Convert the dataset into a pandas DataFrame
3. Assign feature names to columns
4. Add the target variable (`price`) to the DataFrame
5. Validate the dataset structure using exploratory inspection

After preparation, the dataset contains:
- Multiple numerical input features
- One target column representing house price

<br/>


### Modeling Approach (Planned)
- Algorithm: **Random Forest Regressor**
- Data split: Train–test split
- Hyperparameter tuning: GridSearchCV
- Evaluation metric: Mean Squared Error (MSE)

<br/>


### MLflow Usage
MLflow is used to:
- Track hyperparameters for each experiment
- Log evaluation metrics for comparison
- Store trained models as artifacts
- Compare multiple runs visually
- Register the best validated model

This ensures full **experiment reproducibility** and **model traceability**.

