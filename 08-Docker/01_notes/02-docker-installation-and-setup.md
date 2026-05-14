# Docker Installation And Setup

## What We Are Learning In This Part

In this section, the goal is to understand how to install Docker properly and verify that the environment is ready for practical work.

The main focus is:

- what needs to be installed
- the difference between `Docker Desktop`, `Docker Engine`, and the `Docker CLI`
- how to verify that Docker is working
- how to run the first test container

This section is important because before working with images, containers, or Dockerfiles, we need a correct local setup.

## What We Need Before Installing Docker

Before installing Docker, we should remember one simple point:

Docker is not just one small command-line tool.

A working Docker setup usually includes:

- the Docker daemon or engine
- the Docker command-line interface
- background services that manage containers
- in some systems, a desktop application for easier control

So installation means preparing the whole Docker environment, not only downloading one file.

## Docker Desktop Vs Docker Engine Vs Docker CLI

These terms are often confusing at the beginning, so it is important to separate them clearly.

### Docker Engine

`Docker Engine` is the core runtime that actually builds and runs containers.

It is responsible for:

- building images
- starting containers
- stopping containers
- managing networks and volumes

So we can think of Docker Engine as the main backend of Docker.

### Docker CLI

The `Docker CLI` is the command-line interface we use to interact with Docker.

For example, commands like these come from the CLI:

```bash
docker --version
docker ps
docker images
```

The CLI sends instructions to Docker Engine.

### Docker Desktop

`Docker Desktop` is a packaged application commonly used on `Windows` and `macOS`.

It usually provides:

- Docker Engine
- Docker CLI
- a graphical interface
- settings for resources and integrations
- easier setup for local development

So on Windows and macOS, many beginners use Docker Desktop because it is the easiest way to get started.

## Installation Choices By Operating System

The installation path depends on the operating system.

### On Windows

The most common option is:

- install `Docker Desktop`

This is usually the easiest setup for local development.

On Windows, Docker commonly works with:

- `WSL 2`
- virtualization support

So Docker on Windows may depend on system features being enabled first.

### On macOS

The most common option is also:

- install `Docker Desktop`

This gives a straightforward setup for running containers locally.

### On Linux

On Linux, many users install:

- `Docker Engine`
- `Docker CLI`
- related container runtime packages

Linux often gives more direct access to the Docker runtime without needing Docker Desktop.

## Typical Installation Flow

At a high level, the setup process usually looks like this:

1. download Docker for the operating system
2. install Docker components
3. restart the machine if needed
4. start Docker services or Docker Desktop
5. verify installation using Docker commands
6. run a test container

This is the first practical workflow we need to remember.

## Important Requirement On Windows

On `Windows`, Docker often depends on:

- virtualization being enabled in BIOS or UEFI
- `WSL 2` support
- Windows features required for containerization

If these are not enabled, Docker installation may complete but containers may not run correctly.

So when Docker fails on Windows, one of the first things to check is whether the system-level requirements are enabled.

## Update wsl and docker desktop via cmd
### Update wsl
1. Open PowerShell or Windows Command Prompt in administrator mode.
2. Run below commands
    ```bash
    wsl --version
    wsl --update
  ```

### Update docker desktop
```bash
docker desktop update check     # Check for updates
docker desktop update download  # Download the latest update
docker desktop update install   # Install the downloaded update
```

## First Things To Check After Installation

After installation, we should confirm that Docker is available from the terminal.

### Check Docker Version

```bash
docker --version
```

This command confirms that the Docker CLI is installed and accessible from the terminal.

### Check More Detailed Version Information

```bash
docker version
```

This usually shows:

- client version details
- server version details

If the client is available but the server is not running, this command helps reveal that problem.

### Check General Docker Information

```bash
docker info
```

This command gives a broader view of the Docker environment, such as:

- number of containers
- number of images
- storage driver details
- configured runtime information

It is a useful diagnostic command.

## Why Docker Desktop Must Be Running

On systems that use `Docker Desktop`, installing Docker is not always enough by itself.

The Docker services also need to be running.

That means:

- Docker Desktop may need to be opened
- background services may need a few seconds to start
- the terminal may show connection errors if Docker is not fully started yet

So if a Docker command fails right after installation, the issue may simply be that Docker Desktop is not running.

## Running The First Test Container

Once Docker is installed, the next step is to run a small test container.

A very common first test is:

```bash
docker run hello-world
```

This command helps us verify several things at once:

- Docker can connect to the engine
- Docker can pull an image if it is not already available
- Docker can create and start a container
- the container can run successfully

If this works, it is a strong sign that the Docker installation is healthy.

## What Happens In `docker run hello-world`

This command may look small, but several steps happen internally:

1. Docker checks whether the `hello-world` image exists locally
2. if not, Docker pulls it from a registry
3. Docker creates a container from that image
4. Docker starts the container
5. the container prints a success message and exits

This is a very useful first example because it shows the basic flow:

`pull image -> create container -> run container`

## Useful Starter Commands After Installation

After the first successful run, these are good starter commands to try:

### List Running Containers

```bash
docker ps
```

This shows containers that are currently running.

### List All Containers

```bash
docker ps -a
```

This shows:

- running containers
- stopped containers

### List Downloaded Images

```bash
docker images
```

This shows the images available on the local machine.

## Common Beginner Problems

At the setup stage, a few problems are very common.

### 1. Docker Command Not Found

This usually means:

- Docker is not installed properly
- the terminal was opened before installation completed
- the system path was not refreshed yet

### 2. Cannot Connect To The Docker Daemon

This usually means:

- Docker Desktop is not running
- Docker services are stopped
- the engine is not started yet

### 3. Virtualization Or WSL-Related Errors

This is especially common on Windows.

It may mean:

- virtualization is disabled
- `WSL 2` is not configured correctly
- required Windows features are missing

### 4. Permission Issues On Linux

On Linux, Docker may be installed but normal users may not have permission to run Docker commands without elevated privileges.

This is often a user-group or permission configuration issue.

## What A Healthy Docker Setup Looks Like

A healthy installation usually means:

- `docker --version` works
- `docker version` shows both client and server information
- `docker info` runs successfully
- `docker run hello-world` works without errors

If all of these work, we are usually ready to move on to images and containers.

## Why This Setup Step Matters In Real Projects

In real development, environment issues waste a lot of time.

A correct Docker installation gives us:

- a stable starting point
- consistent local development
- fewer dependency conflicts with the host machine
- an easier path toward project packaging and deployment

So this setup step may feel simple, but it is actually the foundation for everything that comes next.

## Mental Model To Remember

At this stage, the easiest mental model is:

- install Docker
- make sure the engine is running
- verify with version and info commands
- run a simple test container

That is the basic setup checklist.

## Key Takeaway

The most important thing to remember is:

`A Docker setup is complete only when the Docker engine is running and a test container can run successfully.`

Installation alone is not the full proof. Verification is equally important.

## One-Line Summary

Docker installation and setup means preparing the Docker environment, confirming that the engine is running, and verifying everything with simple commands like `docker --version` and `docker run hello-world`.
