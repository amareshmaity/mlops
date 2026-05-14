# Introduction To Docker

## What We Are Learning In This Part

Here we are trying to understand the basic idea of `Docker` and why it is such an important tool in modern development.

The main focus is:

- what Docker actually is
- what problem Docker solves
- why developers use containers
- how Docker helps us run applications in a consistent way

So the first goal is not advanced commands or deployment.

The first goal is to clearly understand the **foundation of containerization**.

## What Docker Is

`Docker` is a platform that helps us package an application together with everything it needs to run.

That usually includes:

- application code
- system-level dependencies
- Python libraries or other packages
- runtime configuration

This package can then be run as a `container`.

A container gives us a lightweight and isolated environment where the application behaves the same way everywhere.

## The Main Problem Docker Solves

Before Docker, one very common problem in development was:

`it works on my machine, but not on another machine`

This happens because two systems may differ in:

- operating system
- Python version
- installed packages
- environment configuration
- system libraries

Because of these differences, the same project may run correctly on one machine and fail on another.

Docker solves this by packaging the application and its environment together in a standard format.

## Why Docker Is Used

Docker is used because it makes software easier to:

- build
- share
- run
- test
- deploy

Instead of manually setting up the whole environment on every machine, we can create a Docker image once and run it anywhere Docker is available.

This makes development more reliable and reproducible.

## Simple Real-World Idea

Suppose I build a `Python` project on my laptop.

That project may need:

- `Python 3.11`
- `pandas`
- `scikit-learn`
- `mlflow`
- some system dependencies

If another person wants to run the same project, they may face installation issues.

With Docker, I can package the project in a container so the other person does not need to manually recreate the same setup from scratch.

## What A Container Means

A `container` is a running instance of an application in an isolated environment.

It is designed to contain:

- the application
- its dependencies
- its required runtime

So instead of depending heavily on the host machine, the application runs inside its own controlled setup.

## Containers Vs Virtual Machines

This is one of the most important comparisons to remember.

### Virtual Machines

A `virtual machine` includes:

- a full guest operating system
- virtual hardware
- the application and its dependencies

Because of that, virtual machines are usually:

- heavier
- slower to start
- more resource-intensive

### Containers

Containers do not package a full operating system in the same way.

They share the host system kernel and isolate the application at the process level.

Because of that, containers are usually:

- lighter
- faster to start
- easier to scale
- more efficient for application packaging

## One Simple Comparison

We can think of it like this:

- a `virtual machine` is like renting a full house
- a `container` is like renting a well-organized room inside a building

Both give isolation, but containers do it with much less overhead.

## Important Docker Terms

At the introduction stage, these words are important:

### 1. Docker Image

An `image` is a packaged blueprint for an application.

It contains everything needed to create a container.

### 2. Docker Container

A `container` is the running instance created from an image.

So we can say:

`image -> container`

### 3. Dockerfile

A `Dockerfile` is a text file that contains instructions for building a Docker image.

It describes:

- which base image to use
- which files to copy
- which dependencies to install
- which command to run when the container starts

## Basic Workflow We Need To Remember

The high-level Docker workflow is:

1. write the application code
2. create a `Dockerfile`
3. build a Docker image
4. run the image as a container

So the flow becomes:

`code -> Dockerfile -> image -> container`

## Why Docker Is Important In MLOps

Docker is especially useful in `ML` and `MLOps` because machine learning projects often depend on:

- specific Python versions
- many libraries
- model files
- APIs
- reproducible environments

In ML projects, Docker helps us:

- keep the training or inference environment consistent
- package an app or model-serving API
- avoid dependency conflicts
- move projects more easily from local development to cloud deployment

## Where Docker Helps In Practice

Docker is commonly used in:

- local development
- backend application deployment
- model serving APIs
- data engineering workflows
- CI/CD pipelines
- cloud deployment

This is why Docker is considered a very practical and essential tool.

## What Docker Does Not Automatically Solve

Docker is very useful, but it does not solve everything by itself.

For example, Docker does not automatically handle:

- model monitoring
- experiment tracking
- version control
- orchestration of large distributed systems

That is why Docker is often used together with tools like:

- `Git`
- `MLflow`
- `DVC`
- `Kubernetes`

## Main Goal Of Learning Docker In This Module

In this module, our goal is not just to memorize commands.

The goal is to understand how Docker helps us create reproducible environments for applications and ML projects.

So we want to build a mental model like this:

- application code needs dependencies
- dependencies differ across machines
- Docker packages the environment with the code
- containers make the application portable and consistent

## Key Takeaway

The most important idea to remember is:

`Docker lets us package an application and its dependencies into a portable container so it runs consistently across environments.`

That is the core reason Docker became so popular.

## One-Line Summary

Docker is a containerization platform that helps us package applications and their dependencies so they can run reliably and consistently on different machines.
