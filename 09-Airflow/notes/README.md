# Apache Airflow Notes for AI Engineering

These notes are my structured study notes while learning Apache Airflow for MLOps and AI systems. The focus is not just on definitions, but on how Airflow fits into real ML workflows such as data ingestion, retraining, orchestration, scheduling, and monitoring.

The notes are organized chapter by chapter so I can revise concepts quickly and build toward practical projects.

## What These Notes Cover

- What Apache Airflow is and why it matters in an ML project
- How Airflow fits into the data science and MLOps lifecycle
- Core concepts such as DAGs, tasks, and dependencies
- Why Airflow is a strong orchestration tool for ML and ETL pipelines
- How to get started locally using Astro and Docker

## Chapter Map

1. [01-airflow-in-ml-lifecycle.md](./01-airflow-in-ml-lifecycle.md)
   Airflow fundamentals, workflow automation, and where orchestration fits in the end-to-end ML lifecycle.

2. [02-core-concepts-dag-task-dependency.md](./02-core-concepts-dag-task-dependency.md)
   DAGs, tasks, direction, acyclic behavior, and execution dependencies.

3. [03-why-airflow-for-mlops.md](./03-why-airflow-for-mlops.md)
   Reasons Airflow is useful for MLOps, including orchestration, automation, monitoring, and retries.

4. [04-local-setup-with-astro.md](./04-local-setup-with-astro.md)
   Practical setup notes for running Airflow locally with Astro and Docker.

## How I Intend to Use These Notes

- Revise concepts before building workflows
- Use them as quick reference during project work
- Extend them later with code examples, operators, hooks, scheduling, XCom, and deployment patterns

## Current Scope

These notes currently cover the foundational concepts and setup workflow. I can expand them later with:

- DAG authoring patterns
- Operators and sensors
- XCom and inter-task communication
- Scheduling and cron expressions
- ETL and ML retraining pipeline examples
- Production deployment notes
