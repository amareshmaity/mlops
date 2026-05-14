# Docker Compose For Multi-Service Projects

## What We Are Learning In This Part

In this section, the goal is to understand how to manage applications that require more than one container.

The main focus is:

- what `docker compose` is
- why it is useful
- how to define services in a `compose.yaml` file
- how to start and stop multi-container applications
- the most common Compose commands

This section is important because many real applications are not made of a single container.

They often include multiple services that need to run together.

## Why Docker Compose Is Needed

After learning basic Docker commands, one common problem appears quickly.

If an application needs:

- one web app container
- one database container
- one cache container

then managing each container manually becomes repetitive and error-prone.

Without Compose, we may need to remember many separate commands for:

- networks
- volumes
- port mappings
- environment variables
- container names

This becomes difficult to manage consistently.

That is why `docker compose` is useful.

## What Docker Compose Is

`Docker Compose` is a tool that allows us to define and run multi-container Docker applications using a single configuration file.

Instead of starting each container manually, we describe the whole setup in one file and let Compose manage it.

So Compose helps us move from:

- many manual `docker run` commands

to:

- one structured application definition

## The Core Idea We Need To Remember

The main idea is:

`one application -> multiple services -> one compose file`

So Compose is not a replacement for Docker.

It is a higher-level way to organize and run multiple Docker containers together.

## What A Service Means In Compose

In Compose, a `service` is a container definition for one part of the application.

For example:

- a web app can be one service
- a database can be one service
- Redis can be one service

Each service can define things like:

- which image to use
- how to build the image
- which ports to expose
- which volumes to mount
- which environment variables to set

So a Compose file is basically a collection of service definitions.

## Compose File Name

The common file name is:

```text
compose.yaml
```

Older examples may also use:

```text
docker-compose.yml
```

In modern Docker usage, `compose.yaml` is the more standard naming style.

## Simple Compose Example

A very small example looks like this:

```yaml
services:
  web:
    build: .
    ports:
      - "5000:5000"

  db:
    image: postgres:15
```

This file defines two services:

- `web`
- `db`

Now instead of running each container manually, Compose can start both together.

## Main Benefit Of Docker Compose

The biggest benefit of Compose is that the whole application setup becomes declarative.

That means we define the desired state in a file.

This gives us:

- easier setup
- less repetition
- better readability
- easier sharing with teammates
- simpler local development

This is especially useful for projects that need repeatable environments.

## Common Things Defined In A Compose File

A Compose file often includes:

- services
- images or build instructions
- ports
- volumes
- environment variables
- networks
- restart rules

So one file can describe most of the local multi-container application setup.

## Important Compose Keys To Remember

There are a few keys that beginners should understand first.

### 1. `services`

This is the main section where we define application services.

Example:

```yaml
services:
  web:
    build: .
```

Each entry under `services` describes one containerized part of the app.

### 2. `image`

`image` tells Compose to use an existing image.

Example:

```yaml
image: postgres:15
```

This is useful when we want to use a ready-made container image.

### 3. `build`

`build` tells Compose to build an image from a Dockerfile.

Example:

```yaml
build: .
```

This means Compose should build the image using the Dockerfile in the current directory.

So:

- `image` uses an existing image
- `build` creates an image from local project files

### 4. `ports`

`ports` maps host ports to container ports.

Example:

```yaml
ports:
  - "5000:5000"
```

This works like the `-p` option in `docker run`.

### 5. `volumes`

`volumes` allows persistent data or bind mounts to be attached.

Example:

```yaml
volumes:
  - mydata:/var/lib/postgresql/data
```

This is useful for:

- databases
- app data
- local development mounts

### 6. `environment`

`environment` sets environment variables for a service.

Example:

```yaml
environment:
  POSTGRES_USER: admin
  POSTGRES_PASSWORD: secret
```

This is useful for service configuration.

### 7. `depends_on`

`depends_on` expresses startup dependency order between services.

Example:

```yaml
depends_on:
  - db
```

This means the service should start after the listed dependency service is started.

It is useful, but it is important to remember that startup order is not always the same as application readiness.

## Simple Web App And Database Example

A more realistic Compose file may look like this:

```yaml
services:
  app:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

This example shows:

- one application service
- one database service
- one named volume for database persistence

This is a very common real-world Compose pattern.

## How Service Communication Works In Compose

Compose automatically helps services communicate through a shared network.

That means one service can often reach another using the service name.

In the previous example:

- app service can connect to database host `db`

This is very important.

Inside the app container:

- use `db`
- not `localhost`

This is one of the biggest practical benefits of Compose.

## Starting A Compose Application

To start all services defined in the Compose file, we use:

```bash
docker compose up
```

This reads the Compose file and starts the services together.

If images need to be built, Compose can also build them.

## Running In Detached Mode

To start services in the background, we use:

```bash
docker compose up -d
```

This is one of the most common Compose commands in everyday work.

It allows the application stack to run without keeping the terminal occupied.

## Stopping The Compose Application

To stop the running services, we use:

```bash
docker compose down
```

This stops and removes the containers created by Compose.

It is one of the cleanest ways to stop a multi-service setup.

## Building Services With Compose

If the Compose file includes `build`, we can explicitly build images using:

```bash
docker compose build
```

This is useful when source code or Dockerfile changes need to be rebuilt.

## Viewing Running Services

To see the status of services managed by Compose, we use:

```bash
docker compose ps
```

This shows which services are up and how they are mapped.

## Viewing Logs

To see logs from the Compose application, we use:

```bash
docker compose logs
```

To follow logs continuously:

```bash
docker compose logs -f
```

This is very useful when debugging application startup or service communication issues.

## Restarting Services

To restart services in a Compose project, we use:

```bash
docker compose restart
```

This is useful when we need to refresh running services after configuration or code changes.

## Common Practical Flow With Compose

A common practical workflow looks like this:

1. write the `compose.yaml` file
2. define services, ports, volumes, and environment variables
3. run `docker compose up -d`
4. inspect status with `docker compose ps`
5. inspect logs with `docker compose logs`
6. stop everything with `docker compose down`

So the full flow becomes:

`define -> up -> check -> debug -> down`

## Why Compose Is Better Than Manual Commands

Without Compose, we may need long `docker run` commands for each service.

Those commands can become difficult to:

- remember
- share
- debug
- repeat

Compose solves this by storing the setup in version-controlled configuration.

That makes the application easier to reproduce on another machine.

## Volumes And Networks In Compose

Compose works very naturally with:

- volumes
- service networking

For example:

- services can share the same Compose-managed network
- named volumes can be declared once and reused cleanly

This makes Compose a natural next step after learning Docker volumes and networking.

## Why Compose Matters In ML And MLOps

In `ML` and `MLOps` projects, Compose is very useful when a project has multiple parts.

For example:

- an API service
- an `MLflow` service
- a database service
- a frontend or dashboard

Compose helps us run this local ecosystem with one consistent configuration.

This is useful for:

- local development
- demos
- reproducible project environments
- testing multi-service behavior

## Common Beginner Mistakes

At this stage, a few mistakes are very common.

### 1. Using `localhost` Between Services

Inside one service, `localhost` usually means that same container.

To reach another service, use the service name, such as `db`.

### 2. Forgetting That `depends_on` Does Not Guarantee Full Readiness

It helps with startup order, but the dependent service may still need time before it is truly ready to accept connections.

### 3. Forgetting Port Mapping

Even if the service runs inside Compose, it may not be reachable from the host without proper port mapping.

### 4. Not Persisting Important Data

Services like databases usually need volumes, otherwise data may not survive container replacement.

### 5. Treating Compose As A Different Technology From Docker

Compose is built on top of Docker concepts.

It still uses:

- images
- containers
- networks
- volumes

It simply manages them in a more organized way.

## A Simple Mental Model To Remember

The easiest mental model is:

- Docker runs containers
- Compose organizes multiple related containers
- services describe parts of the application
- `up` starts everything
- `down` stops and removes the Compose-managed containers

If this model is clear, Compose becomes much less intimidating.

## Key Takeaway

The most important thing to remember is:

`Docker Compose lets us define and run a multi-container application in one structured configuration file.`

This makes setup, sharing, and local development much easier.

## One-Line Summary

This section explains how Docker Compose uses a `compose.yaml` file to define services, ports, volumes, and environment variables so multi-container applications can be started and managed with simple commands like `docker compose up` and `docker compose down`.
