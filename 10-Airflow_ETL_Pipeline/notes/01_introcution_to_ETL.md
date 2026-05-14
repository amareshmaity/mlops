# Introduction to ETL

## What Is ETL?

ETL stands for:

- **Extract**
- **Transform**
- **Load**

It is a process used to collect data from one or more sources, clean or reshape that data, and store it in a final destination where it can be used for analytics, machine learning, or reporting.

## Why ETL Matters

In real-world data projects, data usually does not come from a single place. It can come from:

- Internal databases
- Third-party APIs
- IoT devices
- Other external or paid data sources

Because the data is spread across multiple systems, we need a reliable way to bring everything together. ETL helps us do that in a structured pipeline.

## ETL in a Data Project Lifecycle

In a typical data science or data engineering project:

1. Requirements are gathered from business stakeholders, product owners, and domain experts.
2. The data science or analytics team identifies what data is needed to solve the problem.
3. The big data or data engineering team builds a data pipeline to collect and prepare that data.
4. The processed data is stored in a central location for downstream use.

This ETL process is an important part of the larger **data pipeline**.

## ETL Stages Explained

### 1. Extract

The **extract** step means collecting data from source systems.

Examples of sources:

- APIs
- Internal databases
- IoT devices
- External services

If a project needs data from 4 to 5 different sources, the first job of the pipeline is to fetch that data from all of them.

### 2. Transform

The **transform** step means preparing the raw data so it becomes useful and consistent.

This may include:

- Combining data from multiple sources
- Cleaning incomplete or inconsistent records
- Selecting only the required fields
- Changing the format of the data
- Converting the output into a structured format such as JSON

The goal of transformation is to make the data easier to use for the next stages of the project.

### 3. Load

The **load** step means storing the transformed data into a final destination.

Common destinations include:

- PostgreSQL
- SQL Server
- MongoDB
- Other SQL or NoSQL databases

After loading, the data science or analytics team can work from this single prepared source instead of querying many separate systems.

## Simple Flow of an ETL Pipeline

**Multiple Data Sources** -> **Extract Data** -> **Transform / Clean / Combine** -> **Load into Database**

This creates one dependable source of truth for the team.

## ETL vs Data Pipeline

- A **data pipeline** is the full system that moves data from source to destination.
- **ETL** is a core process inside that pipeline.

So, ETL is often a major part of a data pipeline, especially when data must be cleaned and reshaped before storage.

## Role of Airflow in ETL

Apache Airflow is used to **orchestrate and schedule** ETL pipelines.

Airflow helps us:

- Run ETL jobs automatically
- Schedule jobs daily, weekly, or at any custom interval
- Manage the sequence of tasks
- Build reliable and repeatable workflows

This is useful when fresh data must be collected regularly instead of manually running the pipeline every time.

## Example Project Mentioned in the Transcript

The planned project in the transcript follows this flow:

1. Read data from an API
2. Extract selected fields
3. Transform the data into JSON
4. Load the result into a PostgreSQL database
5. Schedule the whole process using Airflow

The setup may also use Docker so the database and pipeline environment stay portable and easier to deploy.

## Key Takeaways

- ETL means **Extract, Transform, Load**.
- It helps combine data from multiple sources into one usable destination.
- Transformation makes raw data clean, structured, and analysis-ready.
- Loading stores the prepared data in a database or storage system.
- Airflow is useful because it can schedule and manage ETL workflows automatically.

## Short Summary

ETL is the foundation of many modern data engineering workflows. It allows teams to gather data from different places, convert it into a useful format, and store it in one central system. Airflow makes this process practical in production by automating when and how the pipeline runs.
