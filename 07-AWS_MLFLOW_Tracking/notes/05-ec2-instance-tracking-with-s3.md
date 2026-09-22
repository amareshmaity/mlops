# Tracking Experiments From EC2 With S3

## What We Are Doing In This Part

Here we complete the full remote MLflow tracking setup.

The goal is to:

1. Connect to the EC2 instance
2. Install the required tools
3. Create the Python environment
4. Install MLflow, AWS CLI, and boto3
5. Configure AWS inside EC2
6. Start the MLflow tracking server
7. Connect the local `app.py` to the remote server
8. Run an experiment
9. Verify the run in MLflow UI and S3
10. Clean up AWS resources

<br/>

## Main Goal

The goal is to run the MLflow tracking server on **EC2** and use **S3 as the artifact store**.

```text
Local Machine
     │
     │  MLflow Tracking URI
     ▼
EC2
     │
     │  MLflow Tracking Server
     │
     ├── Tracking metadata → SQLite
     │
     └── Artifacts → S3
```

The complete flow is:

```text
Connect to EC2
      ↓
Update packages
      ↓
Install Python tools
      ↓
Install Pipenv
      ↓
Install virtualenv
      ↓
Create MLflow folder
      ↓
Install MLflow + AWS CLI + boto3
      ↓
Enter Pipenv environment
      ↓
Configure AWS
      ↓
Start MLflow server
      ↓
Open MLflow UI
      ↓
Configure local tracking URI
      ↓
Run app.py
      ↓
Verify MLflow + S3
      ↓
Clean up AWS resources
```

<br/>

## Step 1. Connect To The EC2 Machine

First connect to the EC2 instance using SSH.

Example:

```bash
ssh -i <key-file.pem> ubuntu@<public-ip>
```

Once connected, commands are executed inside the EC2 server.

<br/>

## Step 2. Update The Package List

Run:

```bash
sudo apt update
```

### Why?

This updates the package metadata on the EC2 machine so that package installation uses the latest available package information.

<br/>

## Step 3. Install Python And Pip Tools

Install Python 3, pip, and Python virtual-environment support:

```bash
sudo apt install -y python3 python3-pip python3-venv
```

Verify:

```bash
python3 --version
pip3 --version
```

### Why?

These tools are required because MLflow and the other Python dependencies will be installed next.

<br/>

## Step 4. Install Pipenv

Install Pipenv:

```bash
sudo apt install -y pipenv
```

### What Is Pipenv?

`pipenv` is a Python project and dependency management tool.

It helps create and manage an isolated Python environment for the MLflow project.

<br/>

## Step 5. Install virtualenv

Install `virtualenv`:

```bash
sudo apt install -y virtualenv
```

### What Is virtualenv?

`virtualenv` is a tool for creating isolated Python environments.

It keeps project dependencies separated from the system Python environment.

> **Note:** Pipenv already manages an isolated environment for the project, so manually using `virtualenv` is not normally necessary when following the Pipenv workflow. It is included here because it is part of this course setup.

<br/>

## Step 6. Create A Working Folder For MLflow

Create a directory and enter it:

```bash
mkdir mlflow
cd mlflow
```

This keeps the MLflow server setup organized in one location.

<br/>

## Step 7. Install MLflow

Install MLflow through Pipenv:

```bash
pipenv install mlflow
```

This installs MLflow and its dependencies inside the Pipenv environment.

### Why?

The EC2 machine will host the MLflow tracking server, so MLflow must be installed on EC2.

<br/>

## Step 8. Install AWS CLI

Install AWS CLI through Pipenv:

```bash
pipenv install awscli
```

Verify it:

```bash
pipenv run aws --version
```

### Why?

The EC2 machine needs AWS CLI so it can interact with AWS services such as S3.

<br/>

## Step 9. Install boto3

Install boto3:

```bash
pipenv install boto3
```

### Why?

`boto3` is the Python SDK for AWS services.

It allows Python applications and tools to interact programmatically with services such as S3.

<br/>

## Step 10. Enter The Pipenv Environment

Enter the environment:

```bash
pipenv shell
```

After entering it, the installed MLflow and other dependencies are available in the project environment.

You can verify MLflow:

```bash
mlflow --version
```

<br/>

## Step 11. Configure AWS Inside EC2

Now configure AWS credentials on the EC2 machine:

```bash
aws configure
```

You will be asked for:

```text
AWS Access Key ID:
AWS Secret Access Key:
Default region name:
Default output format:
```

For this setup, the region used in the course is:

```text
us-east-1
```

### Verify The AWS Configuration

Run:

```bash
aws sts get-caller-identity
```

If the credentials are valid, AWS returns information about the current identity.

### Important

The AWS configuration on your local machine does **not** automatically transfer to EC2.

EC2 is a separate environment, so it needs its own AWS authentication method.

> **Production note:** For EC2 workloads, an IAM role / instance profile is generally preferable to storing long-lived access keys with `aws configure`.

<br/>

## Step 12. Verify S3 Access

Before starting MLflow, verify that EC2 can access S3.

List the available buckets:

```bash
aws s3 ls
```

Then check the MLflow bucket:

```bash
aws s3 ls s3://mlflow-tracking-1/
```

If these commands work, the EC2 machine can communicate with S3 using the configured AWS identity.

<br/>

## Step 13. Start The MLflow Tracking Server

#### Start MLflow Server

```bash
mlflow server \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root s3://mlflow-tracking-bucket-327 \
  --host 0.0.0.0 \
  --port 5000 \
  --workers 1 \
  --allowed-hosts "*" \
  --cors-allowed-origins "*"
```

### What Each Option Means

#### `--backend-store-uri`

```text
sqlite:///mlflow.db
```

Stores MLflow tracking metadata in a local SQLite database.

Examples of tracking metadata include:

- parameters
- metrics
- run information

#### `--default-artifact-root`

```text
s3://mlflow-tracking-1
```

Defines S3 as the artifact location.

Artifacts can include:

- model files
- run outputs
- artifact directories

#### `--host 0.0.0.0`

Allows the MLflow server to accept connections through the EC2 network interface instead of being available only through localhost.

#### `--port 5000`

Runs MLflow on port `5000`.

The EC2 security group must allow the required inbound traffic on this port.

#### Check mlflow ui

In browser search for "http://ec2-**\***-255.compute-1.amazonaws.com:5000"

The above url is the public dns in aws

---

### Solve the out-of-memory problem (RAM)

To run the application minimum RAM required is 4 GB. But AWS free EC2 instance type like `t3-micron` has RAM 1 GB that is not enough. That's why you have to select `t3-small` or high instance.

You can also create virtual RAM

```bash
pkill -9 -f mlflow

# Allocate 2 Gigabytes of space for the swap file
sudo fallocate -l 2G /swapfile

# Lock permissions so only the root user can read it
sudo chmod 600 /swapfile

# Set up the file as Linux swap area
sudo mkswap /swapfile

# Enable the swap space immediately
sudo swapon /swapfile


echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# verify the extra memory has been allocated
free -h


```

<br/>

## Step 14. Open The MLflow UI

Copy the **public IP address** of the EC2 instance.

Open:

```text
http://<public-ip>:5000
```

If the UI opens successfully, it confirms that:

- EC2 is reachable
- MLflow is running
- port `5000` is accessible

At this point, the UI may be empty because the local application has not sent an experiment run yet.

<br/>

## Step 15. Configure The Local `app.py`

Go back to the local project.

Update:

```python
remote_server_uri = ""
```

to:

```python
remote_server_uri = "http://<public-ip>:5000"
```

Replace `<public-ip>` with the actual public IP address of the EC2 instance.

### Why?

This tells the local application where the remote MLflow tracking server is running.

<br/>

## Step 16. Set The MLflow Tracking URI Locally

In the local terminal, run:

```bash
export MLFLOW_TRACKING_URI=http://<public-ip>:5000
```

Verify:

```bash
echo $MLFLOW_TRACKING_URI
```

This tells the local process which MLflow tracking server to use.

<br/>

## Step 17. Run `app.py`

Run the local application:

```bash
python app.py
```

The experiment should now send its tracking information to the MLflow server running on EC2.

<br/>

## Step 18. Verify The Run In MLflow UI

Refresh:

```text
http://<public-ip>:5000
```

You should now see the experiment run.

Check:

- run details
- metrics such as `RMSE`, `MAE`, and `R2`
- parameters such as `alpha` and `l1_ratio`
- logged model artifacts

<br/>

## Step 19. Verify Artifacts In S3

Check the S3 bucket:

```bash
aws s3 ls s3://mlflow-tracking-1/
```

You should see directories created by MLflow.

These can contain:

- experiment artifact directories
- model files
- outputs generated during the run

You can also inspect the bucket recursively:

```bash
aws s3 ls s3://mlflow-tracking-1/ --recursive
```

<br/>

## Step 20. Update The Project README

Document the setup in the project's `README.md`.

Include:

- MLflow tracking URI
- EC2 commands
- AWS/S3 commands
- setup steps
- MLflow server command

This makes the setup easier to reproduce later.

<br/>

## Step 21. Clean Up AWS Resources

After verifying the complete setup, clean up the resources used for practice.

## Terminate The EC2 Instance

If the instance is no longer needed, stop or terminate it.

Why?

- Running EC2 instances can generate charges.
- Unused resources create unnecessary cost.

## Remove Practice IAM Credentials

If an IAM user was created only for this practice setup, remove the unused credentials/user according to your AWS setup.

This reduces unnecessary security exposure.

## S3 Bucket

Keep the S3 bucket if you want to retain the MLflow artifacts.

If you no longer need the bucket, clean it up as well.

<br/>

## Essential Commands To Remember

### EC2 / Linux

#### Update Packages

```bash
sudo apt update
```

#### Install Python

```bash
sudo apt install -y python3-pip
```

#### Install Pipenv

```bash
sudo apt install -y pipenv
```

#### Install virtualenv

```bash
sudo apt install -y virtualenv
```

#### Create MLflow Directory

```bash
mkdir mlflow
cd mlflow
```

<br/>

### Pipenv

#### Install MLflow

```bash
pipenv install mlflow
```

#### Install AWS CLI

```bash
pipenv install awscli
```

#### Install boto3

```bash
pipenv install boto3
```

#### Enter Environment

```bash
pipenv shell
```

<br/>

### AWS CLI

#### Check AWS CLI

```bash
aws --version
```

#### Configure AWS

```bash
aws configure
```

#### Check Current AWS Identity

```bash
aws sts get-caller-identity
```

#### List S3 Buckets

```bash
aws s3 ls
```

#### List MLflow Bucket

```bash
aws s3 ls s3://mlflow-tracking-1/
```

#### List S3 Contents Recursively

```bash
aws s3 ls s3://mlflow-tracking-1/ --recursive
```

<br/>

### MLflow

#### Start MLflow Server

```bash
mlflow server \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root s3://mlflow-tracking-bucket-327 \
  --host 0.0.0.0 \
  --port 5000 \
  --workers 1 \
  --allowed-hosts "*" \
  --cors-allowed-origins "*"
```

#### Check mlflow ui

In browser search for "http://ec2-**\***-255.compute-1.amazonaws.com:5000"

The above url is the public dns in aws

---

### Solve the out-of-memory problem (RAM)

To run the application minimum RAM required is 4 GB. But AWS free EC2 instance type like `t3-micron` has RAM 1 GB that is not enough. That's why you have to select `t3-small` or high instance.

You can also create virtual RAM

```bash
pkill -9 -f mlflow

# Allocate 2 Gigabytes of space for the swap file
sudo fallocate -l 2G /swapfile

# Lock permissions so only the root user can read it
sudo chmod 600 /swapfile

# Set up the file as Linux swap area
sudo mkswap /swapfile

# Enable the swap space immediately
sudo swapon /swapfile


echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# verify the extra memory has been allocated
free -h


```

<br/>

#### Run Local Application

```bash
python app.py
```

#### Set Tracking URI

```bash
export MLFLOW_TRACKING_URI=http://<public-ip>:5000
```

<br/>

## Complete Setup Command Sequence

For quick revision:

```bash
# 1. Update packages
sudo apt update

# 2. Install Python tools
sudo apt install -y python3 python3-pip python3-venv

# 3. Install environment tools
sudo apt install -y pipenv
sudo apt install -y virtualenv

# 4. Create MLflow project directory
mkdir mlflow
cd mlflow

# 5. Install dependencies
pipenv install mlflow
pipenv install awscli
pipenv install boto3

# 6. Enter environment
pipenv shell

# 7. Configure AWS
aws configure

# 8. Verify AWS
aws sts get-caller-identity
aws s3 ls

# 9. Start MLflow
mlflow server \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root s3://mlflow-tracking-1 \
  --host 0.0.0.0 \
  --port 5000
```

Then, on the **local machine**:

```bash
export MLFLOW_TRACKING_URI=http://<public-ip>:5000
python app.py
```

<br/>

## Final Architecture

```text
                 LOCAL MACHINE
                      │
                      │
             MLFLOW_TRACKING_URI
                      │
                      ▼
              ┌───────────────┐
              │      EC2      │
              │               │
              │ MLflow Server │
              │   Port 5000   │
              └───────┬───────┘
                      │
             ┌────────┴────────┐
             │                 │
             ▼                 ▼
       SQLite Database        S3
       Tracking Metadata    Artifacts
                            │
                            ├── Models
                            ├── Outputs
                            └── Run Artifacts
```

<br/>

## One-Line Summary

**EC2 runs the MLflow tracking server, SQLite stores tracking metadata, S3 stores artifacts, and the local `app.py` sends experiment tracking data to the remote MLflow server.**
