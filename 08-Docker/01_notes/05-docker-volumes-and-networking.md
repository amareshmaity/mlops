# Docker Volumes And Networking

## What We Are Learning In This Part

In this section, the goal is to understand two very important practical topics in Docker:

- how Docker handles data
- how Docker containers communicate with each other

The main focus is:

- why container data is temporary by default
- what `volumes` are
- what `bind mounts` are
- how networking works in Docker
- how multiple containers connect and communicate

This section is important because real applications usually need both:

- persistent data
- communication across services

Without these two ideas, Docker usage remains very limited.

## Why This Topic Matters

When we first start containers, it may seem like everything is working fine.

But in real projects, we quickly face two practical questions:

1. what happens to data when the container stops or is removed
2. how does one container talk to another container

These two questions lead directly to:

- volumes and mounts
- Docker networking

## Container Data Is Temporary By Default

This is one of the most important ideas in Docker.

By default, data created inside a container is tied to that container's writable layer.

That means:

- if the container is removed, the data can be lost
- container-local data is not automatically safe for long-term use

This behavior is fine for temporary tasks, but it becomes a problem for applications that need persistence.

Examples include:

- databases
- uploaded files
- model artifacts
- logs
- cache directories

## Why Persistence Is Needed

Many real applications need data to survive even if the container is restarted or replaced.

For example:

- a database must keep records
- an ML app may need saved models
- an API may need uploaded files
- a dashboard may need configuration or logs

If all of this stays only inside the container, it may disappear when that container goes away.

That is why Docker provides storage mechanisms like volumes and bind mounts.

## What A Docker Volume Is

A `Docker volume` is a Docker-managed storage location that exists outside the normal lifecycle of a specific container.

This means:

- the volume can continue to exist even if the container is removed
- the same volume can be attached to another container
- Docker manages the storage location for us

So a volume is the preferred way to store persistent container data in many cases.

## Main Benefit Of Volumes

The biggest benefit of volumes is persistence.

A volume allows data to survive independently from the container that uses it.

This is very useful for:

- databases
- application data
- logs
- shared service data

## Creating A Volume

Docker allows us to create a named volume using:

```bash
docker volume create mydata
```

This creates a Docker-managed volume called `mydata`.

We can then attach it to a container.

## Using A Volume In A Container

A volume is commonly attached using the `-v` option.

Example:

```bash
docker run -d -v mydata:/app/data my-app
```

This means:

- `mydata` is the Docker volume
- `/app/data` is the path inside the container

So anything written inside `/app/data` can persist through the volume.

## Named Volume Mental Model

The easiest way to think about a named volume is:

- the container uses the storage
- Docker manages where the storage actually lives

So the application writes to a container path, but Docker keeps the data outside the container's disposable writable layer.

## Listing Volumes

To see available Docker volumes, we use:

```bash
docker volume ls
```

This helps us inspect what persistent storage objects exist in Docker.

## Inspecting A Volume

To inspect details about a specific volume, we use:

```bash
docker volume inspect mydata
```

This gives information such as:

- volume name
- driver
- mountpoint

It helps us understand how Docker is managing the storage.

## Removing A Volume

To remove a volume, we use:

```bash
docker volume rm mydata
```

This should be done carefully, because deleting a volume may also delete important persistent data.

## What A Bind Mount Is

A `bind mount` maps a specific folder or file from the host machine into the container.

Example:

```bash
docker run -v ${PWD}:/app my-app
```

The exact host path syntax may differ across operating systems, but the core idea is:

- host path is mapped directly into the container

So unlike a named volume, a bind mount points to a real folder that we choose on the host machine.

## Volumes Vs Bind Mounts

This difference is very important.

### Docker Volume

- managed by Docker
- good for persistent application data
- more portable across environments

### Bind Mount

- directly uses a host machine path
- useful during development
- good when we want live access to local project files

So in simple terms:

- use `volumes` for managed persistent data
- use `bind mounts` when you want the container to work directly with host files

## Why Bind Mounts Are Useful In Development

Bind mounts are especially useful during local development.

For example, if we mount the project folder into the container:

- code changes on the host become visible inside the container
- we do not always need to rebuild the image for every small change

This is very helpful when developing:

- Python apps
- Node.js apps
- notebooks
- APIs

## A Simple Bind Mount Example

Suppose our local project is in the current folder and we want the container to use it:

```bash
docker run -it -v ${PWD}:/app python:3.11-slim bash
```

This allows the container to see the host project inside `/app`.

So the container environment can work directly with local files.

## Important Caution With Mounts

When a volume or bind mount is attached to a container path, it can override what was originally present at that path inside the image.

So mounts are powerful, but we need to use them carefully.

This is especially important when debugging why files inside a container look different than expected.

## Why Networking Is Important In Docker

Real applications often involve more than one container.

For example:

- one container runs a web app
- another container runs a database
- another container may run a cache service

These containers need a way to communicate.

That is where Docker networking becomes important.

## What Docker Networking Does

Docker networking allows containers to:

- communicate with each other
- communicate with the host machine
- expose services to the outside world

So networking is what makes multi-container applications possible.

## Container Port Vs Host Port

This distinction is very important.

A container may run an application on a port inside the container, such as:

- `5000`
- `8000`
- `3306`

But that does not automatically mean the host machine can access it.

To make a service available on the host machine, we usually publish ports.

Example:

```bash
docker run -p 5000:5000 my-app
```

This means:

- left side `5000` is the host port
- right side `5000` is the container port

So host requests to port `5000` are forwarded to port `5000` inside the container.

## Why Port Mapping Matters

Without port mapping, a web app running inside a container may not be reachable from the browser on the host machine.

So even if the application starts correctly, we still need `-p` in many cases to access it externally.

## Default Docker Networking Idea

By default, Docker provides networking support so that containers can run with isolated network settings.

When containers are attached to the same Docker network, they can often communicate using container names or service names.

This becomes especially useful in multi-container projects.

## User-Defined Networks

Docker allows us to create custom networks.

Example:

```bash
docker network create my-network
```

Then containers can be started on that network:

```bash
docker run -d --name app --network my-network my-app
docker run -d --name db --network my-network postgres
```

Now the `app` container can communicate with the `db` container through the shared network.

## Listing Networks

To see Docker networks, we use:

```bash
docker network ls
```

This shows the available network objects managed by Docker.

## Inspecting A Network

To inspect a network in detail, we use:

```bash
docker network inspect my-network
```

This helps us understand:

- which containers are attached
- network configuration details

## How Containers Communicate On The Same Network

When two containers are on the same user-defined network, one container can often reach the other using its container name.

For example:

- app container name: `app`
- database container name: `db`

Then the app may connect to the database using:

- host: `db`

instead of using `localhost`

This is a very important concept.

Inside a container:

- `localhost` usually refers to the container itself
- it does not usually mean another container

## Very Common Beginner Confusion In Networking

One of the most common beginner mistakes is trying to connect from one container to another using `localhost`.

That usually fails because:

- `localhost` inside a container means that same container

So if a web app container wants to connect to a database container, it usually needs:

- the database container name
- or the database service name in Compose

not `localhost`

## Example Of Multi-Container Communication

Suppose we have:

- a `Flask` app container
- a `PostgreSQL` container

If both are on the same Docker network, the app can connect using something like:

- database host = `db`

where `db` is the container or service name.

This is one of the key ideas that later becomes very important in `docker compose`.

## Volumes And Networking Together In Real Apps

In real applications, storage and networking often appear together.

For example:

- a database container uses a volume for persistent data
- an application container connects to that database over a Docker network

So a real setup may look like this:

- app container
- database container
- shared network
- attached volume for database data

This is one of the most common Docker patterns.

## Why This Matters In ML And MLOps

In `ML` and `MLOps` projects, volumes and networking are very useful.

### Volumes help with:

- storing datasets
- storing trained models
- storing experiment outputs
- storing logs and artifacts

### Networking help with:

- connecting an app to a database
- connecting an API to another service
- linking `MLflow` with supporting services
- running multi-service project environments

So this topic becomes very practical very quickly in ML workflows.

## Common Beginner Mistakes

At this stage, a few mistakes are very common.

### 1. Assuming Container Data Is Permanent

By default, container data is not guaranteed to remain safe if the container is removed.

### 2. Mixing Up Volumes And Bind Mounts

Remember:

- volumes are Docker-managed
- bind mounts map a host path directly

### 3. Forgetting Port Publishing

A service running inside a container is not always accessible from the host unless `-p` is used.

### 4. Using `localhost` For Another Container

Inside a container, `localhost` usually means that same container, not a different service.

### 5. Deleting Volumes Without Realizing The Data Impact

Removing a volume can remove useful persistent data.

So cleanup commands should be used carefully.

## A Simple Mental Model To Remember

The easiest mental model is:

- container storage is temporary by default
- volumes keep data persistent
- bind mounts connect host files directly
- networks let containers talk to each other
- `-p` lets the host talk to the container

If this model is clear, volumes and networking become much easier to understand.

## Key Takeaway

The most important thing to remember is:

`Volumes solve data persistence, and networking solves communication between containers and services.`

These two ideas are essential for real Docker applications.

## One-Line Summary

This section explains how Docker stores persistent data using volumes and bind mounts, and how Docker networking allows containers and services to communicate with each other and with the host machine.
