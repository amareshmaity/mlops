# Core Concepts: DAG, Task, and Dependency

## DAG

DAG stands for Directed Acyclic Graph.

In Airflow, a DAG is a collection of tasks that are organized into a workflow. The DAG defines what should run, in what order, and under what schedule.

## Why It Is Called Directed

Directed means the workflow has a clear execution flow.

Example:

`data_ingestion -> preprocessing -> model_training`

This direction tells Airflow that one task should happen before the next one.

## Why It Is Called Acyclic

Acyclic means the workflow should not loop back on itself.

This is valid:

`A -> B -> C`

This is not valid:

`A -> B -> C -> A`

No task should create a circular dependency in the execution graph.

## Simple Definition to Remember

A DAG is a workflow blueprint.

It does not just list tasks; it also defines their structure and relationship.

## Task

A task is an individual unit of work inside a DAG.

Examples of tasks:

- run a Python function
- query a database
- call an external API
- write data to storage
- train a model
- send a notification

Each task should ideally do one clear job.

## Dependency

Dependencies define the order in which tasks run.

If task B depends on task A, then task B should start only after task A finishes successfully.

Example:

- data ingestion must finish before preprocessing
- preprocessing must finish before model training
- model training must finish before deployment

Without dependencies, Airflow would not know the correct execution order.

## Nodes and Edges

When visualized as a graph:

- nodes represent tasks
- edges represent relationships between tasks

So in a workflow graph:

`A -> B -> C`

- `A`, `B`, and `C` are nodes
- arrows are edges

## Mapping DAG Concepts to ML Work

An ML workflow can naturally be represented as a DAG:

- Task 1: ingest data
- Task 2: clean and preprocess data
- Task 3: train model
- Task 4: evaluate model
- Task 5: deploy model

This makes Airflow especially useful for MLOps because most ML systems already have a stepwise structure.

## Design Principles for Good Airflow Thinking

- Break large workflows into clear tasks.
- Keep the execution order explicit.
- Avoid circular logic.
- Make each task easy to understand and debug.

## Key Takeaways

- A DAG is a collection of connected tasks.
- Tasks are the smallest executable units in a workflow.
- Dependencies control order of execution.
- Directed means execution has a defined path.
- Acyclic means the workflow cannot loop back into itself.
