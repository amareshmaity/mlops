# Practical: Implementing GitHub Actions for Python Unit Tests

## Goal of This Practical

In this practical, the objective is to create a simple Python project and use **GitHub Actions** to automatically run **unit test cases** whenever code is pushed to GitHub or a pull request is created.

This is a basic **CI pipeline** because the workflow automatically validates the code after repository activity.

## What We Will Build

We will create:

- a GitHub repository
- a simple Python project
- a `requirements.txt` file
- a `src` folder for source code
- a `tests` folder for unit tests
- a GitHub Actions workflow YAML file

At the end, GitHub Actions will automatically run `pytest` in a GitHub-hosted environment.

## Final Project Structure

```text
project-root/
|-- .github/
|   |-- workflows/
|   |   `-- unit-test.yml
|-- src/
|   |-- __init__.py
|   `-- math_operations.py
|-- tests/
|   |-- __init__.py
|   `-- test_operation.py
|-- README.md
`-- requirements.txt
```

## Step 1: Create a New GitHub Repository

Go to `github.com` and create a new repository.

Example repository name from the transcript:

- `app-github-action`
- or any name you prefer for your Python app

At creation time:

- do not initialize with a README
- do not add a license initially

This gives you a clean repository that you can connect from your local system.

## Step 2: Open the Project in VS Code

Create or open your project folder in VS Code.

Create a simple `README.md`.

Example:

```md
## This is the python app 1
```

This is not technically required for GitHub Actions, but it is a good first file for the initial commit.

## Step 3: Initialize Git Locally

Open the terminal in VS Code and initialize the Git repository.

```bash
git init
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin <your-repository-url>
git push -u origin main
```

### What These Commands Do

- `git init` initializes a local Git repository
- `git add .` stages all current files
- `git commit -m "initial commit"` creates the first commit
- `git branch -M main` renames the branch to `main`
- `git remote add origin ...` connects your local repo to GitHub
- `git push -u origin main` pushes your local code to GitHub

After this step, your repository should be visible on GitHub.

## Step 4: Create `requirements.txt`

Create a `requirements.txt` file in the project root.

Example from the transcript:

```txt
pytest
```

### Why These Dependencies Are Added

- `pytest` is needed to run unit tests


In a real project, this file should contain all libraries required by the application and tests.

## Step 5: Create the Source Code Folder

Create a folder named `src`.

Inside it, create:

- `__init__.py`
- `math_operations.py`

### `src/__init__.py`

This file can be empty. It helps Python treat the folder like a package.

### `src/math_operations.py`

Add simple functions like addition and subtraction.

```python
def add(a, b):
    return a + b


def sub(a, b):
    return a - b
```

This keeps the practical small and lets us focus on the GitHub Actions workflow itself.

## Step 6: Create the Test Folder

Create a folder named `tests`.

Inside it, create:

- `__init__.py`
- `test_operation.py`

### Why the `tests` Folder Matters

`pytest` automatically looks for test files in locations that follow its naming conventions.

This is why we use:

- a folder named `tests`
- a file name beginning with `test_`

That makes test discovery simple and automatic.

## Step 7: Write Unit Tests

Inside `tests/test_operation.py`, import the source functions and write test cases.

```python
from src.math_operations import add, sub


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_sub():
    assert sub(5, 3) == 2
    assert sub(4, 3) == 1
    assert sub(3, 3) == 0
    assert sub(2, 3) == -1
```

### What `assert` Does

Each `assert` checks whether the function returns the expected result.

If the result is correct:

- the test passes

If the result is wrong:

- the test fails

This is the logic GitHub Actions will run automatically.

## Step 8: Commit and Push the Python Project

Once the code and tests are ready, commit and push them.

```bash
git add .
git commit -m "unit test cases updated"
git push origin main
```

At this stage the project exists on GitHub, but no automation is running yet because we have not created the workflow file.

## Step 9: Create the GitHub Actions Workflow Folder

Now create the special GitHub Actions path:

```text
.github/workflows/
```

This path is important because GitHub looks here for workflow definitions.

Inside that folder, create a YAML file such as:

- `unit-test.yml`

You may also see examples such as `python-app.yml`. The exact filename is flexible, but it must be inside `.github/workflows/`.

## Step 10: Add the GitHub Actions Workflow YAML

Add the following workflow configuration to `.github/workflows/unit-test.yml`.

```yaml
name: Python CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.8"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: pytest
```

## Step 11: Understand the Workflow File

This YAML file is the heart of the GitHub Action.

### `name`

```yaml
name: Python CI
```

This is the workflow name displayed in the GitHub Actions tab.

### `on`

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
```

This defines the events that trigger the workflow.

In this practical, the workflow runs when:

- code is pushed to `main`
- a pull request targets `main`

### `jobs`

```yaml
jobs:
  test:
```

This defines a job named `test`.

A workflow can have one job or many jobs. In this example, one job is enough.

### `runs-on`

```yaml
runs-on: ubuntu-latest
```

This tells GitHub to run the job in a GitHub-hosted Ubuntu environment.

GitHub can also run jobs on:

- Windows
- macOS

But the transcript uses `ubuntu-latest`.

### `steps`

The `steps` section defines the sequence of actions inside the job.

#### Step 1: Checkout code

```yaml
- name: Checkout code
  uses: actions/checkout@v2
```

This downloads your repository code into the runner environment so the workflow can use it.

#### Step 2: Set up Python

```yaml
- name: Set up Python
  uses: actions/setup-python@v2
  with:
    python-version: "3.8"
```

This creates a Python environment inside the GitHub runner.

You can change the version to `3.9`, `3.10`, or another supported version based on your project.

#### Step 3: Install dependencies

```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
```

This installs the libraries required by the project and test suite.

#### Step 4: Run tests

```yaml
- name: Run tests
  run: pytest
```

This executes all discovered test cases.

Because the project uses the `tests` folder and `test_*.py` naming style, `pytest` can detect the tests automatically.

## Step 12: Commit and Push the Workflow File

After creating the YAML file, commit and push again.

```bash
git add .
git commit -m "add github actions workflow"
git push origin main
```

This push triggers the workflow automatically because the YAML file listens to `push` events on `main`.

## Step 13: Verify the Workflow in the GitHub Actions Tab

Go to the repository on GitHub and open the **Actions** tab.

You should see the workflow running.

The transcript shows the typical stages:

- setup job
- checkout code
- set up Python
- install dependencies
- run tests
- post-job cleanup

If everything is correct, the job should pass successfully.

## Step 14: Understand What Happens During Execution

When the workflow starts, GitHub does the following:

1. creates a temporary runner machine
2. checks out your code into that machine
3. installs Python
4. installs dependencies from `requirements.txt`
5. runs `pytest`
6. reports pass or fail in the Actions tab

This is why GitHub Actions is useful: it gives the team automatic feedback without requiring each developer to run every validation manually.

## Step 15: What Happens on Future Commits

After this setup, every new push or pull request to `main` will automatically trigger the same validation pipeline.

That means:

- if tests pass, confidence in the code increases
- if tests fail, the issue is visible immediately

This is the foundation of continuous integration.

## Common Practical Notes

### 1. Why `pytest` Is Important

Without `pytest`, the workflow has nothing to execute for automated unit testing.

### 2. Why the `.github/workflows/` Path Is Mandatory

GitHub only recognizes workflow YAML files when they are placed in that directory.

### 3. Why the Workflow Is Triggered Automatically

The `on` block listens for repository events like `push` and `pull_request`.

### 4. Why This Is CI

This setup automatically checks code changes before the team trusts them. That is exactly the role of continuous integration.

### 5. Why This Matters in Real Projects

In real teams, many developers push code frequently. Automated testing helps ensure that a new change does not silently break existing functionality.

## Short Summary

This practical shows how to create a simple Python project, write unit tests with `pytest`, and connect the project to GitHub Actions using a workflow YAML file. Once configured, every push or pull request automatically runs the test suite in a GitHub-hosted environment. That gives fast feedback and forms the first building block of a CI pipeline.



Resources:
* [github docs](https://docs.github.com/en/actions)
* [practical example](https://github.com/amareshmaity/github-action-app)
