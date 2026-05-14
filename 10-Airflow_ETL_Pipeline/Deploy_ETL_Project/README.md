# Deploy ETL Project on Astronomer Airflow with PostgreSQL on AWS

This guide turns the deployment transcript into a clean set of notes for taking the local Airflow ETL project to the cloud using:

- Astronomer Astro for managed Apache Airflow
- AWS RDS for PostgreSQL
- The existing DAG in [`../ETL_Project/dags/etl.py`](../ETL_Project/dags/etl.py)

The goal is simple:

1. Keep Airflow running in Astronomer Cloud
2. Move PostgreSQL out of the local Docker container and into AWS
3. Update Airflow connections so the deployed DAG writes into the AWS database

## What Is Being Deployed

The ETL pipeline already exists locally in the Astro project under [`../ETL_Project`](../ETL_Project).

The DAG:

- creates the `apod_data` table if it does not exist
- calls NASA's APOD API
- transforms the response
- inserts the final data into PostgreSQL

Important connection IDs used by the DAG:

- `my_postgres_connection`
- `nasa_api`

These names must match exactly inside the Astronomer Airflow UI.

## Cloud Architecture

Local development setup:

- Airflow runs in Docker through Astro
- PostgreSQL runs in Docker through `docker.compose.yml`

Cloud deployment setup:

- Airflow runs in Astronomer Astro
- PostgreSQL runs in AWS RDS
- Airflow connects to AWS RDS over the internet using the RDS endpoint

So the only major runtime change is the PostgreSQL host. Instead of using the local container host, you use the AWS RDS endpoint in the Airflow connection.

## Prerequisites

Before starting, make sure you have:

- an Astronomer Astro account
- AWS account access
- Astro CLI installed locally
- the ETL project available on your machine
- a NASA API key

Useful project location:

- Astro project root: [`../ETL_Project`](../ETL_Project)

## Step 1: Create an Astronomer Astro Account

Go to `https://cloud.astronomer.io` and create a new account.

During onboarding:

- create an organization or personal workspace
- choose the free trial if available
- create a deployment on AWS from the Astro UI

The transcript shows Astro offering trial credits for first-time users. The exact trial details may change over time, but the setup flow is the same.

## Step 2: Create an Astro Deployment

Inside Astro:

1. Create a workspace
2. Create a deployment
3. Choose `AWS` as the deployment platform

At this stage Astro prepares a managed Airflow environment for your project.

You may initially see messages like:

- `No healthy deployments found`
- `Airflow unavailable`

That is normal before the first code deployment finishes.

## Step 3: Log In from the Astro CLI

Open a terminal in the Astro project folder:

```powershell
cd ..\ETL_Project
astro login
```

This opens a browser and asks you to authenticate your Astro CLI session with your Astronomer account.

## Step 4: Deploy the Airflow Project to Astro

From the same [`../ETL_Project`](../ETL_Project) folder, run:

```powershell
astro deploy
```

What happens here:

- Astro builds the project image
- validates the DAGs
- pushes the image to Astronomer
- updates the Airflow deployment

If prompted, select the target deployment created in the Astro UI.

After deployment:

- wait a few minutes for Airflow to become healthy
- refresh the deployment page until the Airflow environment is available

## Step 5: Create PostgreSQL in AWS RDS

Astronomer manages Airflow, but it does not create your application database for this project. That is why PostgreSQL is created separately in AWS.

In AWS:

1. Open `RDS`
2. Go to `Databases`
3. Click `Create database`

Recommended settings from the transcript:

- Create method: `Standard create`
- Engine type: `PostgreSQL`
- Template: `Free tier` for practice/demo use
- DB instance class: small free-tier compatible instance
- Allocated storage: default free-tier value is enough for this demo

Suggested database values used in the transcript:

- Database name: `postgres`
- Master username: `postgres`
- Master password: `postgres`

You can use stronger credentials in real projects, but if you do, the Airflow connection must use the same values.

## Step 6: Enable Network Access to RDS

For Airflow in Astronomer to reach the database, the database must be reachable over the network.

In the RDS setup:

- enable `Public access`

Then open the database's security group and update inbound rules:

1. Open the RDS instance
2. Open its linked VPC security group
3. Edit inbound rules
4. Add a PostgreSQL rule

Typical PostgreSQL rule:

- Type: `PostgreSQL`
- Protocol: `TCP`
- Port: `5432`
- Source: a custom CIDR range

The transcript demonstrates a wide-open rule for quick testing. For learning, that works, but for safer practice prefer restricting access to known IP ranges instead of allowing the whole internet.

## Step 7: Copy the RDS Endpoint

Once the RDS instance is available, copy the database endpoint from AWS.

It will look similar to:

```text
your-db-name.xxxxxx.region.rds.amazonaws.com
```

This endpoint becomes the `Host` value in the Airflow PostgreSQL connection.

## Step 8: Open Airflow in Astronomer

After `astro deploy` completes and the deployment becomes healthy:

1. Open the Astro deployment
2. Click `Open Airflow`

If Airflow does not open immediately:

- refresh the page
- wait until the deployment status becomes healthy
- make sure the image finished building and deploying

## Step 9: Create the PostgreSQL Connection in Airflow

Inside Airflow:

1. Go to `Admin`
2. Open `Connections`
3. Create a new connection

Use these values:

- Connection Id: `my_postgres_connection`
- Connection Type: `Postgres`
- Host: `YOUR_RDS_ENDPOINT`
- Schema: `postgres`
- Login: `postgres`
- Password: `postgres`
- Port: `5432`

Why these values matter:

- the DAG in [`../ETL_Project/dags/etl.py`](../ETL_Project/dags/etl.py) uses `my_postgres_connection`
- the host must point to AWS RDS, not the local Docker hostname

## Step 10: Create the NASA API Connection in Airflow

Create another Airflow connection for the API call.

Use:

- Connection Id: `nasa_api`
- Connection Type: `HTTP`
- Host: `https://api.nasa.gov`

Add the API key in the connection extras:

```json
{
  "api_key": "YOUR_NASA_API_KEY"
}
```

This matches the DAG code, which reads:

```python
{{ conn.nasa_api.extra_dejson.api_key }}
```

## Step 11: Trigger the DAG

Open the DAGs page in Airflow and find:

- `nasa_apod_postgres`

Then:

1. enable the DAG if needed
2. trigger a run manually

The transcript shows that after the environment is ready, the DAG can be triggered from the Airflow UI and should start running successfully.

## Step 12: Verify Each ETL Stage

Open the DAG graph and inspect the tasks:

- `create_table`
- `extract_apod`
- `transform_apod_data`
- `load_data_to_postgres`

What to verify:

- `create_table` should create `apod_data` if it does not already exist
- `extract_apod` should fetch data from NASA API
- `transform_apod_data` should prepare the required fields
- `load_data_to_postgres` should insert the row into PostgreSQL

Green task status means the flow is working correctly.

## Step 13: Verify Data in PostgreSQL

To confirm the load step worked, connect to the AWS PostgreSQL database using a DB client such as DBeaver.

Use:

- Host: `YOUR_RDS_ENDPOINT`
- Port: `5432`
- Database: `postgres`
- Username: `postgres`
- Password: `postgres`

Then run:

```sql
SELECT * FROM apod_data;
```

If the DAG has been triggered multiple times, you should see multiple inserted rows.

## Deployment Flow Summary

The full deployment flow is:

1. Build the ETL project locally with Astro
2. Create an Astro deployment in Astronomer Cloud
3. Log in with `astro login`
4. Deploy code with `astro deploy`
5. Create PostgreSQL in AWS RDS
6. Allow network access to the RDS instance
7. Copy the RDS endpoint
8. Configure `my_postgres_connection` in Airflow
9. Configure `nasa_api` in Airflow
10. Trigger the DAG
11. Confirm records are inserted into `apod_data`

## Key Idea to Remember

The deployment works because the DAG code does not need major changes.

Only the runtime environment changes:

- Airflow moves from local Docker to Astronomer Astro
- PostgreSQL moves from local Docker to AWS RDS
- Airflow connections are updated to point to the cloud resources

That is the main production deployment concept demonstrated by this project.

## Practical Notes and Cautions

- Run `astro deploy` from the Astro project directory, which is [`../ETL_Project`](../ETL_Project), not from the transcript folder.
- The Airflow connection IDs must exactly match the IDs used in the DAG.
- RDS may take several minutes to become available after creation.
- Astro deployments may also take a few minutes before Airflow becomes healthy.
- Opening PostgreSQL to the internet is acceptable for a learning demo, but not ideal for production.
- In production, use strong passwords, restricted security groups, secrets management, and private networking.

## Quick Checklist

- Astro account created
- Astro deployment created on AWS
- `astro login` completed
- `astro deploy` completed successfully
- AWS RDS PostgreSQL created
- RDS security group allows PostgreSQL access
- RDS endpoint copied
- `my_postgres_connection` created in Airflow
- `nasa_api` created in Airflow
- `nasa_apod_postgres` triggered successfully
- data verified in `apod_data`
