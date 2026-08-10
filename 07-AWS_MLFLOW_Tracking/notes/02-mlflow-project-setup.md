# MLflow Project Setup

## What We Are Doing In This Part

Here we are setting up a simple local machine learning project that we will later connect to `MLflow` running on `AWS EC2`.

At this stage, our focus is on the local project setup only.

The main tasks are:

- create the project folder
- create the Python environment
- install required libraries
- create the starter files
- prepare the basic `app.py` structure

<br/>

## Main Idea Of The Setup

Our project will run locally, but we want its experiment tracking to point to a remote `MLflow` server hosted on `AWS`.

So the setup flow is:

`local project setup -> environment setup -> install dependencies -> create app.py -> prepare code for remote MLflow tracking`

<br/>

## Steps:
### Step 1. Create The Project Folder

We first need a new folder for the project.

Important things to remember:

- we can create the project anywhere we want
- there is no strict naming rule
- we should open the folder in the terminal and then in `VS Code`

After opening the folder, the next step is to launch the editor using:

```bash
code .
```

This opens the current project in `VS Code`.

### Step 2. Create A Virtual Environment

We create an isolated Python environment using:

```bash
conda create -p venv python==3.10 -y
```


### Step 3. Create `requirements.txt`

After creating the environment, we add a `requirements.txt` file.

The libraries we need at this stage are:

```txt
mlflow
scikit-learn
boto3
```
**Notes:**

We need `boto3` because later we will work with `AWS S3`.

In this setup, the experiment artifacts will eventually be stored in an `S3 bucket`, so Python needs a way to interact with AWS services.

### Step 4. Install The Dependencies

After creating the environment, we activate it and install the dependencies using:

```bash
pip install -r requirements.txt
```

This installs everything listed in `requirements.txt`.

### Step 5. Write app.py
Inside `app.py ` file write the actual logic of the project.

<br/>

## Basic Project Structure At This Stage

The project is still simple.

At this point it roughly looks like:

```text
project-folder/
|-- venv/
|-- requirements.txt
|-- app.py
`-- README.md
```

