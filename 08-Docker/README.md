# Docker for MLOps and Application Deployment

This folder contains my structured notes for learning `Docker` from basics to practical usage in `ML` and `MLOps` projects.

The goal of this module is to understand how to package applications, create reproducible environments, and run projects consistently across different systems.

## What I Learn In This Module

In this module, I focus on the core Docker concepts that are most useful in real development work:

- what `Docker` is and why it is used
- the difference between `images` and `containers`
- how to run containers using common Docker commands
- how to write a `Dockerfile`
- how to manage dependencies inside a container
- how `volumes` and `networks` work
- how to use `docker compose` for multi-service applications
- how Docker fits into `ML`, `MLflow`, and `MLOps` workflows

## Project Goal

The main goal is to build a strong practical understanding of containerization so that:

- local development becomes more reproducible
- application setup becomes easier
- dependencies stay isolated from the host machine
- ML projects can be packaged and shared cleanly
- deployment and experimentation become more consistent

## Course Content

### 1. Introduction to Docker

In this section, I will understand:

- what problem Docker solves
- why containerization is important
- the difference between traditional setup and container-based setup
- the basic Docker workflow

### 2. Docker Installation and Setup

In this section, I will cover:

- installing Docker on the local machine
- checking Docker version and basic setup
- understanding Docker Desktop and Docker Engine
- verifying the installation with a test container

### 3. Images, Containers, and Basic Commands

In this section, I will learn:

- what Docker images are
- what containers are
- how to pull an image from Docker Hub
- how to run, stop, start, and remove containers
- how to inspect logs and running containers

### 4. Writing Dockerfiles

In this section, I will learn:

- the structure of a `Dockerfile`
- common instructions like `FROM`, `WORKDIR`, `COPY`, `RUN`, `CMD`, and `EXPOSE`
- how to build a custom Docker image
- how to containerize a simple Python application

### 5. Volumes and Networking

In this section, I will cover:

- why data inside containers is temporary by default
- how `volumes` help persist data
- how to mount local files into containers
- how container networking works
- how services communicate with each other

### 6. Docker Compose for Multi-Service Projects

In this section, I will learn:

- what `docker compose` is
- why it is useful for multi-container applications
- how to define services in `compose.yaml`
- how to start and stop all services together
- how Compose helps in real project workflows

### 7. Docker in ML and MLOps Projects

In this section, I will focus on:

- containerizing a machine learning project
- packaging dependencies for training or inference
- using Docker with `MLflow` or APIs
- improving reproducibility in ML experiments
- preparing projects for deployment

### 8. Quick Revision and Commands Cheat Sheet

In this section, I will keep:

- important Docker commands
- common `Dockerfile` instructions
- Compose commands
- personal revision notes

## Folder Contents

```text
08-Docker/
|-- README.md
`-- notes/
    |-- README.md
    |-- 01-introduction-to-docker.md
    |-- 02-docker-installation-and-setup.md
    |-- 03-images-containers-and-basic-commands.md
    |-- 04-writing-dockerfiles.md
    |-- 05-docker-volumes-and-networking.md
    |-- 06-docker-compose-for-multi-service-projects.md
    |-- 07-docker-in-ml-and-mlops-projects.md
    `-- 08-docker-quick-revision-cheatsheet.md
```

## Notes Structure

I created topic-wise files so that each Docker concept can be studied separately and revised quickly.

- `README.md` gives the complete module overview
- `notes/README.md` gives the learning roadmap
- `01-introduction-to-docker.md` explains the basic idea of Docker
- `02-docker-installation-and-setup.md` covers installation and verification
- `03-images-containers-and-basic-commands.md` covers everyday Docker commands
- `04-writing-dockerfiles.md` explains image creation
- `05-docker-volumes-and-networking.md` explains persistence and communication
- `06-docker-compose-for-multi-service-projects.md` explains multi-container setup
- `07-docker-in-ml-and-mlops-projects.md` connects Docker to ML workflows
- `08-docker-quick-revision-cheatsheet.md` is for revision

## Final Summary

This module is meant to build a strong Docker foundation that will support later work in:

- reproducible development
- ML project packaging
- local testing
- deployment preparation
- MLOps workflows

By the end of this section, I should be comfortable creating and running containers for both simple applications and ML projects.
