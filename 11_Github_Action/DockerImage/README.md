# Dockerized Flask App with GitHub Actions

This project shows how to create a simple Flask application, test it with `pytest`, package it with Docker, and automate the process with GitHub Actions.

The project is useful as a beginner-friendly example of:

- building a Flask app
- writing a simple test
- creating a Docker image
- running CI on every push and pull request
- pushing a Docker image to DockerHub from GitHub Actions

## Project Structure

```text
DockerImage/
|-- .github/
|   `-- workflows/
|       `-- cicd.yml
|-- .gitignore
|-- app.py
|-- DockerFile
|-- README.md
|-- requirements.txt
`-- test_app.py
```

## Files Used in This Project

### `app.py`

This is the Flask application. It creates one route, `/`, which returns `Hello World!`.

```python
from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
```

### `test_app.py`

This file contains a simple unit test. It checks that the home route returns:

- status code `200`
- response body `Hello World!`

```python
from app import app

def test_home():
    response=app.test_client().get("/")

    assert response.status_code==200
    assert response.data== b"Hello World!"
```

### `requirements.txt`

This file lists the Python dependencies used in the project.

```text
Flask
pytest
```

### `DockerFile`

This file defines how to build the Docker image for the Flask app.

```dockerfile
# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install flask

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
```

### `.gitignore`

This ignores the local virtual environment folder:

```text
venv
```

### `.github/workflows/cicd.yml`

This is the GitHub Actions workflow file. It defines the CI/CD pipeline for the project.

## Step-by-Step Guide to Create This Project

### 1. Create the project folder

Create a folder for the project, for example:

```powershell
mkdir DockerImage
cd DockerImage
```

### 2. Create the Flask app

Create `app.py` and add a simple Flask application with one route:

```python
from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
```

Why this is needed:

- `Flask(__name__)` creates the Flask app
- `@app.route("/")` maps the home URL
- `app.run(host="0.0.0.0", port=5000)` makes the app accessible from inside Docker

### 3. Add dependencies

Create `requirements.txt`:

```text
Flask
pytest
```

Why this is needed:

- `Flask` runs the web application
- `pytest` is used to test the app

### 4. Write a test

Create `test_app.py`:

```python
from app import app

def test_home():
    response=app.test_client().get("/")

    assert response.status_code==200
    assert response.data== b"Hello World!"
```

Why this is needed:

- it confirms that the Flask route works correctly
- GitHub Actions can run this test automatically on each push

### 5. Add `.gitignore`

Create `.gitignore`:

```text
venv
```

Why this is needed:

- it prevents your local virtual environment from being committed to GitHub

### 6. Create the Docker file

Create `DockerFile`:

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]
```

What each instruction does:

- `FROM python:3.9-slim` uses a lightweight Python image
- `WORKDIR /app` sets the container working directory
- `COPY . /app` copies the project files into the container
- `RUN pip install flask` installs Flask inside the image
- `EXPOSE 5000` documents the app port
- `CMD ["python", "app.py"]` starts the Flask app when the container runs

### 7. Run the project locally without Docker

Install dependencies and test the app:

```powershell
pip install -r requirements.txt
pytest
python app.py
```

Then open:

```text
http://localhost:5000
```

You should see:

```text
Hello World!
```

### 8. Build and run the Docker container

Build the Docker image:

```powershell
docker build -f DockerFile -t flasktest-app .
```

Run the container:

```powershell
docker run -p 5000:5000 flasktest-app
```

Now open:

```text
http://localhost:5000
```

### 9. Create the GitHub Actions workflow

Create the folder:

```powershell
mkdir .github
mkdir .github\workflows
```

Create `.github/workflows/cicd.yml` and add:

```yaml
name: CI/CD for Dockerized Flask App

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  dockerbuild:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Build The Docker Image
      run: docker build . --file DockerFile --tag workflow-test:$(date +%s)

  build-and-test:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flask
        pip install pytest

    - name: Run tests
      run: |
        pytest

  build-and-publish:
    needs: build-and-test
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2

    - name: Login to DockerHub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}

    - name: Build and push Docker image
      uses: docker/build-push-action@v4
      with:
        context: .
        file: ./DockerFile
        push: true
        tags: ${{ secrets.DOCKER_USERNAME }}/flasktest-app:latest

    - name: Image digest
      run: echo ${{ steps.build-and-publish.outputs.digest }}
```

### 10. Understand the workflow jobs

This workflow runs on:

- every push to `main`
- every pull request to `main`

It has three jobs:

#### `dockerbuild`

This job checks whether the Docker image can be built successfully.

#### `build-and-test`

This job:

- checks out the code
- installs Python
- installs Flask and pytest
- runs `pytest`

This ensures the Flask app works before publishing an image.

#### `build-and-publish`

This job runs only after `build-and-test` succeeds.

It:

- logs in to DockerHub
- builds the Docker image
- pushes the image to DockerHub

### 11. Add GitHub repository secrets

To push the image to DockerHub, add these secrets in your GitHub repository:

- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

Steps:

1. Open your GitHub repository.
2. Go to `Settings`.
3. Open `Secrets and variables` > `Actions`.
4. Add both secrets.

### 12. Push the project to GitHub

Use the following commands:

```powershell
git init
git add .
git commit -m "Add Flask app with Docker and GitHub Actions"
git branch -M main
git remote add origin <your-repository-url>
git push -u origin main
```

After pushing:

- open the `Actions` tab in GitHub
- watch the workflow run
- confirm tests pass
- confirm the Docker image is pushed to DockerHub

## How This Project Works End to End

The complete flow is:

1. You push code to the `main` branch.
2. GitHub Actions starts automatically.
3. The workflow builds the Docker image.
4. The workflow runs the Flask test with `pytest`.
5. If the test passes, GitHub Actions logs in to DockerHub.
6. The Docker image is built again and pushed to DockerHub.

## Notes About the Current Version

This project is good for learning, but there are a few things to notice:

- `DockerFile` installs only `flask` directly and does not use `requirements.txt`
- the GitHub Actions workflow also installs `flask` and `pytest` directly instead of using `requirements.txt`
- the final `Image digest` step references `steps.build-and-publish.outputs.digest`, but the build step does not currently have an `id`, so that output will not work as written

For a more maintainable version, you could later update the Docker and workflow steps to use:

```text
pip install -r requirements.txt
```

## Conclusion

This project demonstrates a complete beginner workflow for:

- Flask application development
- Docker image creation
- automated testing with GitHub Actions
- DockerHub image publishing

It is a simple but practical starting point for understanding CI/CD with Flask and Docker.
