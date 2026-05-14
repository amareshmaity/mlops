# Writing Dockerfiles

## What We Are Learning In This Part

In this section, the goal is to understand how to create our own Docker images instead of only downloading ready-made images from Docker Hub.

The main focus is:

- what a `Dockerfile` is
- why Dockerfiles are important
- the most common Dockerfile instructions
- how to build an image from a Dockerfile
- how to containerize a simple Python application

This section is important because a Dockerfile is the main way we define how our own application should be packaged.

## What A Dockerfile Is

A `Dockerfile` is a text file that contains step-by-step instructions for building a Docker image.

It tells Docker things like:

- which base image to start from
- where the application files should go
- which dependencies should be installed
- which command should run when the container starts

So a Dockerfile is basically the recipe for creating a Docker image.

## Why Dockerfiles Are Important

Dockerfiles are important because they allow us to describe the application environment in a reproducible way.

Instead of manually setting up:

- Python
- libraries
- folders
- startup commands

we define everything in one file.

That means the image can be rebuilt again and again in the same way.

This is one of the biggest reasons Docker is useful in real projects.

## The Main Idea We Need To Remember

The simple workflow is:

`Dockerfile -> docker build -> image -> docker run -> container`

So the Dockerfile comes before the custom image.

Without a Dockerfile, creating repeatable custom images becomes much harder.

## Basic Structure Of A Dockerfile

A Dockerfile is usually written line by line using Docker instructions.

A very simple example looks like this:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

This small file already defines:

- the base environment
- the working directory
- which files to copy
- which dependencies to install
- which command to run

## Important Common Dockerfile Instructions

There are some instructions we use very often.

These are the first ones to remember.

### 1. `FROM`

`FROM` defines the base image.

Example:

```dockerfile
FROM python:3.11-slim
```

This tells Docker to start from an existing image that already contains Python.

Usually, every Dockerfile starts with `FROM`.

## Why `FROM` Matters

The base image provides the starting environment.

For example:

- `python:3.11-slim` gives a lightweight Python setup
- `ubuntu:22.04` gives an Ubuntu base
- `node:20` gives a Node.js environment

So choosing the base image is one of the first design decisions in a Dockerfile.

### 2. `WORKDIR`

`WORKDIR` sets the working directory inside the container.

Example:

```dockerfile
WORKDIR /app
```

After this, many following instructions run relative to that path.

This helps keep the Dockerfile clean and organized.

### 3. `COPY`

`COPY` copies files from the local machine into the image.

Example:

```dockerfile
COPY . /app
```

This tells Docker to copy the current project files into `/app` inside the image.

This instruction is commonly used to include:

- source code
- configuration files
- dependency files such as `requirements.txt`

### 4. `RUN`

`RUN` executes a command during the image build process.

Example:

```dockerfile
RUN pip install -r requirements.txt
```

This is usually used for:

- installing packages
- creating directories
- running system setup commands

It is important to remember:

- `RUN` happens while building the image
- it does not mean the command runs every time the container starts

### 5. `CMD`

`CMD` defines the default command that runs when the container starts.

Example:

```dockerfile
CMD ["python", "app.py"]
```

This tells Docker what to run when a container is created from the image.

So `CMD` is about container startup behavior.

### 6. `EXPOSE`

`EXPOSE` documents which port the application uses inside the container.

Example:

```dockerfile
EXPOSE 5000
```

This is common for:

- web applications
- APIs
- dashboards

It is important to remember that `EXPOSE` does not automatically publish the port to the host machine.

It only documents the intended container port.

### 7. `ENV`

`ENV` sets environment variables inside the image.

Example:

```dockerfile
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
```

This is useful for configuring application behavior.

### 8. `ENTRYPOINT`

`ENTRYPOINT` is used when we want a container to behave like a fixed executable.

Beginners usually work more with `CMD` first, but it is good to know that `ENTRYPOINT` exists.

In simple learning projects, `CMD` is often enough.

## `RUN` Vs `CMD`

This difference is very important.

### `RUN`

- executes during image build
- used to prepare the image

### `CMD`

- executes when the container starts
- used to define the default runtime command

So the easiest way to remember it is:

- `RUN` builds the environment
- `CMD` starts the application

## Order Matters In A Dockerfile

The order of instructions matters because Docker builds images layer by layer.

Each instruction usually creates a new layer.

That means:

- Docker processes the file from top to bottom
- changing one line may affect the layers after it
- good order can make rebuilds faster

This is why Dockerfile structure is not random.

## A Better Pattern For Python Projects

In Python applications, a common best practice is to copy `requirements.txt` first, install dependencies, and only then copy the rest of the source code.

Example:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

This pattern is useful because dependency installation does not need to rerun every time source code changes, as long as `requirements.txt` stays the same.

## Why Layering Matters

Docker images are built in layers.

This gives an important advantage:

- unchanged layers can be reused

So if dependencies are installed in an earlier stable layer, rebuilds become faster.

This is one of the reasons Dockerfiles are often organized carefully.

## Building An Image From A Dockerfile

Once the Dockerfile is ready, we build an image using:

```bash
docker build -t my-app .
```

Here:

- `docker build` tells Docker to build an image
- `-t my-app` adds a tag or name to the image
- `.` means the current folder is the build context

The build context is important because Docker can only copy files that are inside the provided context.

## What The Build Context Means

When we run:

```bash
docker build -t my-app .
```

the final `.` means:

- send the current directory to Docker as the build context

So if the Dockerfile says:

```dockerfile
COPY . .
```

Docker copies files from that build context into the image.

This is why we usually run `docker build` from the project root.

## Running The Built Image

After building the image, we can run it with:

```bash
docker run my-app
```

If the application is a web app or API, we may also need port mapping, such as:

```bash
docker run -p 5000:5000 my-app
```

This maps:

- host port `5000`
- container port `5000`

That allows us to access the application from the host machine.

## Simple Python Application Example

Suppose we have a small Python file:

```python
print("Hello from Docker")
```

and a Dockerfile like this:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["python", "app.py"]
```

Then the basic flow becomes:

```bash
docker build -t hello-python .
docker run hello-python
```

This is one of the easiest ways to understand how a custom Docker image is created and run.

## Example For A Python API

If the application is an API such as `Flask` or `FastAPI`, the Dockerfile may also include:

```dockerfile
EXPOSE 5000
```

or another port depending on the app.

Then the container may be started using:

```bash
docker run -p 5000:5000 my-api
```

This is how local containerized web applications are commonly tested.

## Why Dockerfiles Matter In ML And MLOps

In `ML` and `MLOps` projects, Dockerfiles are very useful because they help package:

- model-serving APIs
- training environments
- preprocessing pipelines
- experiment apps

Machine learning projects often depend on:

- exact Python versions
- multiple libraries
- system packages
- reproducible environments

A Dockerfile helps define all of this clearly in one place.

That makes ML projects easier to:

- share
- test
- deploy
- reproduce

## Common Beginner Mistakes

At this stage, a few mistakes are very common.

### 1. Confusing `RUN` And `CMD`

Remember:

- `RUN` is for build time
- `CMD` is for container start time

### 2. Forgetting The Build Context

Sometimes files are not copied because the build command was run from the wrong folder.

### 3. Copying Everything Too Early

If we copy the full project before installing dependencies, Docker may rebuild more layers than necessary when source code changes.

### 4. Forgetting Port Mapping

Even if the app works inside the container, it may not be reachable from the host unless ports are mapped correctly with `-p`.

### 5. Using Very Large Base Images Without Need

Heavy base images increase build time and image size.

For many Python apps, lighter images such as `python:3.11-slim` are often a better starting point.

## A Simple Mental Model To Remember

The easiest mental model is:

- `FROM` chooses the starting environment
- `WORKDIR` sets where we work
- `COPY` brings files into the image
- `RUN` prepares the environment
- `CMD` starts the app

So the overall flow becomes:

`choose base -> copy files -> install dependencies -> define startup command`

## Key Takeaway

The most important thing to remember is:

`A Dockerfile is the recipe that defines how a custom Docker image should be built and how the container should start.`

Once the Dockerfile is clear, building and running custom applications in Docker becomes much easier.

## One-Line Summary

This section explains how to write Dockerfiles, use common instructions like `FROM`, `WORKDIR`, `COPY`, `RUN`, and `CMD`, and build custom Docker images for applications such as simple Python projects.
