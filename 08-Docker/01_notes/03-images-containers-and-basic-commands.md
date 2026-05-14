# Images, Containers, And Basic Commands

## What We Are Learning In This Part

In this section, the goal is to understand the two most important practical Docker concepts:

- `images`
- `containers`

Along with that, we will also learn the basic Docker commands used in everyday work.

This section is important because once Docker is installed, the next step is learning how Docker actually runs applications.

## The Core Idea We Need To Remember

In Docker, the relationship between image and container is the foundation of everything.

The simple idea is:

`image -> container`

That means:

- an `image` is the packaged blueprint
- a `container` is the running instance created from that image

If this idea is clear, most beginner Docker commands become much easier to understand.

## What A Docker Image Is

A `Docker image` is a read-only packaged template that contains everything needed to run an application.

It may include:

- application code
- runtime
- libraries
- system dependencies
- configuration defaults

So we can think of an image as a ready-made package from which containers can be created.

## Important Nature Of An Image

An image is not the running application itself.

It is the packaged source used to start the application.

This is similar to the difference between:

- a class and an object in programming
- a blueprint and an actual building

So an image is the definition, while a container is the running result.

## What A Docker Container Is

A `container` is a running or stopped instance created from an image.

When Docker starts an image, it creates a container that has:

- an isolated runtime environment
- a process to execute
- its own temporary writable layer

So a container is the live, operational form of an image.

## One Image Can Create Many Containers

This is another important idea.

A single image can be used to create multiple containers.

For example:

- one `nginx` image can create many running `nginx` containers
- one Python app image can be started multiple times as separate containers

This is useful because the same packaged application can be reused again and again.

## Images Vs Containers In One Simple Table Idea

The easiest way to remember the difference is:

- `image` means packaged template
- `container` means running instance

So:

- images are built or downloaded
- containers are run, stopped, started, and removed

## Where Images Usually Come From

Images usually come from one of two places:

### 1. Docker Hub Or Another Registry

We can download ready-made images from a registry.

Common examples include:

- `python`
- `ubuntu`
- `nginx`
- `mysql`

### 2. Our Own Dockerfile

We can also create our own image by writing a `Dockerfile` and building it locally.

That is how custom project images are usually made.

## Pulling An Image

To download an image from a registry, we use:

```bash
docker pull <image-name>
```

For example:

```bash
docker pull nginx
```

This downloads the `nginx` image to the local machine.

If the image is already available locally, Docker may reuse the local copy instead of downloading it again.

## Understanding Image Names And Tags

Docker images often use:

`image-name:tag`

For example:

```bash
python:3.11
ubuntu:22.04
nginx:latest
```

Here:

- `python` is the image name
- `3.11` is the tag

The tag helps specify a particular version of the image.

This is important because using explicit versions often makes projects more reproducible.

## Running A Container

To create and start a container from an image, we use:

```bash
docker run <image-name>
```

For example:

```bash
docker run hello-world
```

This command tells Docker:

- find the image locally
- pull it if needed
- create a container
- start the container

So `docker run` is one of the most important beginner commands.

## What `docker run` Usually Does

When we use `docker run`, Docker generally performs these steps:

1. checks whether the image exists locally
2. pulls the image if it is missing
3. creates a container from the image
4. starts the container
5. runs the default command inside the container

This means a single command is doing multiple actions for us.

## Running In Interactive Mode

Some containers are useful when we want to work inside them directly.

For that, a common pattern is:

```bash
docker run -it ubuntu
```

Here:

- `-i` keeps input open
- `-t` gives an interactive terminal

This is useful when we want to enter a shell-like environment inside the container.

## Running In Detached Mode

Sometimes we want a container to run in the background.

For that, we use:

```bash
docker run -d nginx
```

Here, `-d` means detached mode.

This is commonly used for services like:

- web servers
- APIs
- databases

## Naming A Container

Docker can auto-generate container names, but we can also provide our own.

Example:

```bash
docker run --name my-nginx nginx
```

This makes the container easier to identify later.

Naming containers becomes very useful when managing multiple services.

## Listing Running Containers

To see currently running containers, we use:

```bash
docker ps
```

This command usually shows:

- container ID
- image name
- command
- creation time
- status
- ports
- container name

This is one of the most frequently used Docker commands.

## Listing All Containers

To see both running and stopped containers, we use:

```bash
docker ps -a
```

This is useful because many containers may have already stopped after finishing their task.

For example, `hello-world` usually appears here after it exits.

## Listing Images

To see all local images, we use:

```bash
docker images
```

This command shows details like:

- repository
- tag
- image ID
- creation time
- size

It helps us understand what images are available locally.

## Stopping A Running Container

To stop a running container, we use:

```bash
docker stop <container-name-or-id>
```

For example:

```bash
docker stop my-nginx
```

This is used when a background container is running and we want to stop its process cleanly.

## Starting A Stopped Container

If a container already exists and is currently stopped, we can start it again with:

```bash
docker start <container-name-or-id>
```

Example:

```bash
docker start my-nginx
```

This starts the existing container again instead of creating a new one.

## Restarting A Container

To quickly restart a container, we use:

```bash
docker restart <container-name-or-id>
```

This is useful when configuration changes require the service to restart.

## Removing A Container

To remove a stopped container, we use:

```bash
docker rm <container-name-or-id>
```

Example:

```bash
docker rm my-nginx
```

This deletes the container object from the local Docker environment.

It is important to remember:

- stopping a container is not the same as removing it
- removed containers no longer exist locally

## Removing An Image

To remove an image, we use:

```bash
docker rmi <image-name-or-id>
```

Example:

```bash
docker rmi nginx
```

This deletes the image from the local system if it is not required by existing containers.

## Viewing Container Logs

To see the output of a container, we use:

```bash
docker logs <container-name-or-id>
```

This is very useful for:

- debugging application startup
- checking errors
- understanding what happened inside a container

Logs become especially important when containers run in detached mode.

## Inspecting A Container

To view detailed information about a container, Docker provides:

```bash
docker inspect <container-name-or-id>
```

This gives low-level details such as:

- networking information
- mounted volumes
- environment configuration
- internal metadata

This command is often used for debugging.

## Executing Commands Inside A Running Container

Sometimes we need to run a command inside an already running container.

For that, we use:

```bash
docker exec -it <container-name-or-id> bash
```

This is useful for:

- checking files inside the container
- verifying installed packages
- debugging application behavior

If `bash` is not available, some images may use `sh` instead.

## A Simple Practical Flow

One beginner-friendly practical flow looks like this:

1. pull an image
2. run a container from that image
3. check running containers
4. inspect logs if needed
5. stop the container
6. start it again if needed
7. remove the container when finished

So the full learning flow becomes:

`pull -> run -> check -> stop -> start -> remove`

## Example With `nginx`

A simple example sequence is:

```bash
docker pull nginx
docker run -d --name my-nginx nginx
docker ps
docker logs my-nginx
docker stop my-nginx
docker start my-nginx
docker rm -f my-nginx
```

This gives a practical understanding of the most common Docker lifecycle operations.

## Common Beginner Confusions

At this stage, a few confusions are very common.

### 1. Image And Container Are Not The Same

Many beginners mix them up.

Remember:

- image = packaged blueprint
- container = running instance

### 2. `docker run` Creates A New Container

If we run the same image again using `docker run`, Docker creates another container.

It does not reopen the previous one automatically.

### 3. Stopped Containers Still Exist

A stopped container is still present unless we remove it.

That is why `docker ps -a` is important.

### 4. Deleting A Container Does Not Always Delete The Image

Containers and images are separate objects.

Removing one does not automatically remove the other.

## Why These Commands Matter In Real Projects

These basic commands are not just for learning.

They are used constantly in real work for:

- local development
- debugging services
- testing application packaging
- running databases and APIs
- validating deployment behavior

So this chapter forms the everyday working vocabulary of Docker.

## Mental Model To Remember

The simplest mental model is:

- images are templates
- containers are running instances
- pull gets an image
- run creates and starts a container
- ps shows containers
- stop/start manages container state
- rm and rmi clean up containers and images

If this model is clear, Docker becomes much easier to use.

## Key Takeaway

The most important thing to remember is:

`A Docker image is the packaged blueprint, and a container is the running instance created from that image.`

Most basic Docker commands revolve around managing these two things.

## One-Line Summary

This section explains how Docker images are downloaded or built, how containers are created from those images, and which basic commands are used to run, inspect, stop, and remove them.
