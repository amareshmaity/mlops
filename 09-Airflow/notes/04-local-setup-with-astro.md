# Local Setup with Astro

## Why Use Astro

Astro, provided by Astronomer, is a managed development experience for Apache Airflow. It simplifies local setup and reduces the friction that usually comes from configuring Airflow manually.

For learning and project work, Astro is useful because it gives a ready-made Airflow project structure and runs Airflow in Docker containers.

## Main Idea

Instead of installing and wiring everything by hand, Astro helps initialize an Airflow project with the required files and local runtime configuration.

## Prerequisites

Before starting:

- Docker should be installed and running
- Astro CLI should be available
- a project folder should be created for the Airflow work

<br/>

### Install Astro CLI
1. Open PowerShell or Command Prompt as an administrator.
2. Run the following command:
  ```bash
  winget install -e --id Astronomer.Astro
  ```
3. Verification
To confirm the installation was successful, open a new terminal and run:
```bash
astro version
```

## Basic Initialization Flow

Inside the project directory, initialize the project with:

```bash
astro dev init
```

This creates the standard Airflow development structure.

## Typical Generated Project Structure

Important folders and files commonly include:

- `dags/`
  Stores DAG definitions
- `include/`
  Additional project assets or helper resources
- `plugins/`
  Custom Airflow plugins
- `tests/`
  Test files for workflows or utilities
- `Dockerfile`
  Runtime image definition
- `requirements.txt`
  Python dependencies
- `.env`
  Environment variables
- `airflow_settings.yaml`
  Airflow-related settings such as connections or variables

## The `dags/` Folder

This is the most important starting point.

Airflow loads workflow definitions from this folder. A DAG file usually contains:

- the DAG definition
- task definitions
- task dependencies

An example DAG often demonstrates a simple ETL-style flow such as:

- fetch data from an API
- process or return that data
- print or store results

## Starting Airflow Locally

To start the local environment:

```bash
astro dev start
```

This command launches the required services through Docker. A typical local stack includes:

- Airflow webserver
- scheduler
- metadata database such as PostgreSQL
- supporting runtime containers

## Accessing the UI

After startup,
- go to docker desktop
- image of airflow project
- go to containers - api-server
- click on `...` and then open with browser

or directly access with 
`http://localhost:11028`

The web UI helps inspect:

- available DAGs
- graph view
- code view
- event logs
- task logs
- run history
- durations and calendar views

## Running a DAG

From the UI, a DAG can be:

- enabled
- triggered manually
- observed while tasks execute

This makes the UI useful not just for monitoring but also for understanding task flow during learning.

## Important Concepts Visible in the UI

### Graph View

Shows the tasks and their dependencies visually.

### Logs

Shows task-level execution details, which helps debug failures and inspect output.

### Event Logs

Shows activity related to DAG runs and task actions.

### XCom

Used for passing small pieces of data between tasks. This becomes important when one task needs to share output with another.

## Stopping the Local Environment

To stop the local Airflow stack:

```bash
astro dev stop
```

## Why This Setup Is Helpful for Learning

- it removes much of the manual configuration burden
- it gives a working local Airflow environment quickly
- it makes DAG development easier to iterate on
- it fits well with containerized MLOps workflows

## Practical Notes

- Docker is central to the setup, so container basics are worth knowing.
- The Airflow UI is one of the best learning tools because it makes workflow execution visible.
- Astro is a practical way to begin learning Airflow before moving to larger production setups.

## Key Takeaways

- Astro simplifies local Airflow development.
- Docker is required for the local runtime.
- `astro dev init` creates the project structure.
- `astro dev start` launches the environment.
- The Airflow UI is useful for running, visualizing, and debugging DAGs.
