# Docker Quick Revision Cheat Sheet

## Main Idea In One Line

`Docker packages an application and its dependencies into a portable container so it runs consistently across environments.`

## Core Terms To Remember

- `image` = packaged blueprint
- `container` = running instance of an image
- `Dockerfile` = recipe to build an image
- `volume` = Docker-managed persistent storage
- `bind mount` = direct mapping from host path to container path
- `network` = communication layer between containers
- `docker compose` = tool to run multi-container applications from one config file

## Most Important Relationships

- `Dockerfile -> image -> container`
- `image -> many possible containers`
- `volume -> persistent data outside container lifecycle`
- `compose.yaml -> multiple services managed together`

## Docker Installation Quick Check

Use these commands after installation:

```bash
docker --version
docker version
docker info
docker run hello-world
```

If `hello-world` runs successfully, the Docker setup is usually working properly.

## Most Important Docker Commands

### Image Commands

```bash
docker pull nginx
docker images
docker rmi nginx
docker build -t my-app .
```

Remember:

- `pull` downloads an image
- `images` lists local images
- `rmi` removes an image
- `build` creates an image from a Dockerfile

### Container Commands

```bash
docker run hello-world
docker run -it ubuntu
docker run -d nginx
docker run --name my-nginx nginx
docker ps
docker ps -a
docker stop my-nginx
docker start my-nginx
docker restart my-nginx
docker rm my-nginx
docker logs my-nginx
docker inspect my-nginx
docker exec -it my-nginx bash
```

Remember:

- `run` creates and starts a new container
- `ps` shows running containers
- `ps -a` shows all containers
- `stop` stops a running container
- `start` starts an existing stopped container
- `rm` removes a container
- `logs` shows container output
- `exec` runs commands inside a running container

## Must-Remember `docker run` Options

- `-it` = interactive terminal
- `-d` = detached mode
- `--name` = custom container name
- `-p host:container` = port mapping
- `-v source:target` = volume or mount attachment

Example:

```bash
docker run -d --name my-app -p 5000:5000 my-image
```

## Common Dockerfile Instructions

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENV APP_ENV=dev
CMD ["python", "app.py"]
```

Remember:

- `FROM` = base image
- `WORKDIR` = working folder inside container
- `COPY` = copy files into image
- `RUN` = execute command during image build
- `EXPOSE` = document container port
- `ENV` = set environment variables
- `CMD` = default startup command

## `RUN` Vs `CMD`

- `RUN` happens during image build
- `CMD` happens when the container starts

Easy memory trick:

- `RUN` builds the environment
- `CMD` starts the application

## Recommended Python Dockerfile Pattern

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Why this pattern is useful:

- dependency layer can be reused
- rebuilds become faster when only source code changes

## Volumes Quick Revision

Remember:

- container data is temporary by default
- volumes keep data persistent
- volumes can survive container removal

Important commands:

```bash
docker volume create mydata
docker volume ls
docker volume inspect mydata
docker volume rm mydata
```

Example:

```bash
docker run -v mydata:/app/data my-app
```

## Bind Mount Quick Revision

Remember:

- bind mount uses a real host path
- useful in local development
- code changes on host can be visible inside container

Example:

```bash
docker run -v ${PWD}:/app my-app
```

## Networking Quick Revision

Remember:

- containers communicate through Docker networking
- host port and container port are different things
- `localhost` inside a container usually means that same container

Example port mapping:

```bash
docker run -p 5000:5000 my-app
```

Example custom network:

```bash
docker network create my-network
docker network ls
docker network inspect my-network
```

Example containers on same network:

```bash
docker run -d --name app --network my-network my-app
docker run -d --name db --network my-network postgres
```

If both are on the same network, the app can usually connect to the database using host `db`.

## Docker Compose Quick Revision

Main idea:

- Compose manages multiple related containers together

Common file name:

```text
compose.yaml
```

Small example:

```yaml
services:
  app:
    build: .
    ports:
      - "5000:5000"

  db:
    image: postgres:15
```

## Most Important Compose Commands

```bash
docker compose up
docker compose up -d
docker compose down
docker compose build
docker compose ps
docker compose logs
docker compose logs -f
docker compose restart
```

Remember:

- `up` starts services
- `up -d` starts in background
- `down` stops and removes Compose containers
- `build` rebuilds service images
- `ps` shows service status
- `logs` shows logs

## Important Compose Keys

- `services` = service definitions
- `image` = use existing image
- `build` = build from Dockerfile
- `ports` = host-container port mapping
- `volumes` = persistent storage or bind mounts
- `environment` = environment variables
- `depends_on` = startup dependency order

## Docker In ML And MLOps Quick Revision

Docker helps in ML by:

- improving reproducibility
- packaging training environments
- packaging inference APIs
- reducing dependency conflicts
- supporting MLflow and multi-service local setups

Common ML use cases:

- training environment packaging
- prediction API containerization
- MLflow local stack
- multi-service ML systems with Compose

## Common Beginner Mistakes

- mixing up `image` and `container`
- thinking `docker run` starts an old container instead of creating a new one
- confusing `RUN` and `CMD`
- assuming container data is permanent
- using `localhost` to reach another container
- forgetting port mapping with `-p`
- thinking Compose is different from Docker instead of built on top of it

## 5 Fast Memory Hooks

- `image = blueprint`
- `container = running app instance`
- `Dockerfile = recipe`
- `volume = persistence`
- `Compose = multi-container manager`

## Final One-Line Revision

`Docker helps build, run, isolate, persist, and connect applications in a reproducible way, while Docker Compose helps manage multiple services together.`
