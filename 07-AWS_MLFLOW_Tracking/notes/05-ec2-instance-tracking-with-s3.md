# Tracking Experiments From EC2 With S3

## What We Are Doing In This Part

Here we are completing the full remote MLflow tracking setup.

In the previous part, we had already:

- created the IAM user
- configured AWS CLI locally
- created the S3 bucket
- launched the EC2 instance
- opened port `5000`
- connected to the EC2 machine

Now we are doing the server-side setup inside EC2 and then connecting our local ML project to that remote MLflow server.

The main tasks here are:

- install required tools inside EC2
- set up the Python environment on the server
- install `mlflow`, `awscli`, and `boto3`
- configure AWS credentials inside EC2
- start the MLflow tracking server
- connect the local `app.py` to the remote server
- verify runs in both MLflow UI and S3
- clean up AWS resources after practice

## Main Goal Of This Part

The main goal is to make the MLflow tracking server actually run on the EC2 instance and use S3 as the artifact store.

The flow is:

`connect to EC2 -> install dependencies -> configure AWS inside EC2 -> launch MLflow server -> update local app -> run experiment -> verify in UI and S3`

## Why This Part Is Important

This is the step where everything comes together.

Without this part:

- EC2 would just be an empty machine
- MLflow server would not start
- S3 would not receive artifacts
- local experiment runs would still not be tracked remotely

So this is the part that turns the cloud setup into a working MLflow tracking system.

## Step 1. Run Commands Inside The EC2 Machine

Once we connect to the EC2 instance, we start running setup commands one by one in the server shell.

The first command is:

```bash
sudo apt update
```

## Why We Run `apt update`

This updates the package list on the EC2 machine.

It is a common first step because:

- package metadata becomes current
- installation becomes smoother
- we reduce issues caused by outdated package references

## Step 2. Install Python Pip Tools

After updating packages, we install Python package tools using `apt`.

The idea here is to make sure the machine has:

- `python3`
- `pip`
- supporting Python tools

This is necessary because MLflow and related libraries will be installed next.

## Step 3. Install `pipenv`

To keep the server setup clean, we install `pipenv` using `apt`:

```bash
sudo apt install pipenv
```

## Why We Use `pipenv`

`pipenv` helps us create an isolated environment for the MLflow server inside the EC2 machine.

That makes the server-side setup cleaner and easier to manage.

## Step 4. Install `virtualenv`

Next, we install `virtualenv`.

This helps provide environment support on the EC2 machine.

The command pattern becomes:

```bash
sudo apt install virtualenv
```

## Why `virtualenv` Is Helpful Here

It helps us keep the MLflow setup isolated from the rest of the server environment.

That makes the server-side setup cleaner and easier to manage.

## Step 5. Create A Working Folder For MLflow

After the basic tools are installed, we create a directory for MLflow on the EC2 machine.

The idea is:

```bash
mkdir mlflow
cd mlflow
```

## Why We Create A Separate Folder

This helps us keep the EC2-side tracking setup organized.

Inside this folder, we install and run the tools needed for the MLflow server.

## Step 6. Install MLflow Inside The EC2 Environment

Inside the MLflow folder, we install `mlflow` using `pipenv`.

The command is:

```bash
pipenv install mlflow
```

This installs MLflow and its dependencies into the server-side environment.

## Why MLflow Must Be Installed Here

We need MLflow installed on EC2 because this machine is going to host the tracking server.

That means the server itself must be able to run:

- MLflow backend
- model logging support
- artifact routing to S3

## Step 7. Install AWS CLI Inside EC2

After MLflow is installed, we also install AWS CLI inside the EC2 environment.

The command is:

```bash
pipenv install awscli
```

## Why AWS CLI Is Needed On The Server

AWS CLI is needed inside EC2 because the machine itself must be able to authenticate with AWS when interacting with services like S3.

This is separate from our local AWS CLI setup.

So we need AWS configuration in two places:

- on our local machine
- on the EC2 machine

## Step 8. Install `boto3`

Next, we install:

```bash
pipenv install boto3
```

## Why `boto3` Is Needed On EC2

`boto3` is needed because MLflow and the environment must be able to work with AWS services programmatically.

Since S3 is being used as the artifact store, `boto3` becomes an important part of the setup.

## Step 9. Enter The `pipenv` Shell

After the installations are complete, we activate the environment using:

```bash
pipenv shell
```

This opens the virtual environment inside the EC2 machine.

## Why This Step Matters

Once the shell is active:

- MLflow commands run inside the configured environment
- installed dependencies are available
- the server setup becomes easier to manage

## Step 10. Configure AWS Inside The EC2 Machine

Now we configure AWS credentials inside the EC2 server itself.

We use:

```bash
aws configure
```

Then we provide:

- access key ID
- secret access key
- region: `us-east-1`
- output format

## Why We Need AWS Configuration On EC2 Too

Even though AWS CLI was already configured locally, that local configuration does not automatically transfer to the EC2 machine.

The EC2 machine is a separate environment.

So if MLflow on EC2 needs to access S3, then EC2 itself must know:

- which credentials to use
- which region to use

## Step 11. Launch The MLflow Tracking Server

This is the most important step in the EC2 setup.

Now we run the MLflow server command with the S3 bucket as the default artifact root.

The structure of the command is like this:

```bash
mlflow server \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root s3://mlflow-tracking-1 \
  --host 0.0.0.0 \
  --port 5000
```

## Important Parts Of This Command

### `--backend-store-uri`

This defines where MLflow stores tracking metadata.

In many setups, a local SQLite database is used for this.

### `--default-artifact-root`

This points to the S3 bucket.

That means MLflow artifacts like:

- model files
- run outputs
- artifact folders

will be stored in S3.

### `--host 0.0.0.0`

This makes the server accessible externally, not just from localhost inside EC2.

### `--port 5000`

This matches the security-group rule we created earlier.

## What We Should See After Starting The Server

Once the command runs successfully, MLflow starts listening on port `5000`.

This confirms that:

- the server is running
- the port is active
- the instance is ready to accept tracking traffic

## Step 12. Open The MLflow UI From The Browser

Now we go back to the EC2 instance page and copy the **public IP address**.

Then we open:

```text
http://<public-ip>:5000
```

## Why This URL Works

This works because:

- the MLflow server is running on EC2
- it is bound to port `5000`
- the security group allows inbound access to that port

If everything is correct, the MLflow UI should open in the browser.

## What This Confirms

If the UI opens successfully, it confirms:

- EC2 is reachable
- MLflow server is running correctly
- network access is configured correctly

At this stage, the UI may still be empty because no experiment has been sent to it yet.

## Step 13. Update `remote_server_uri` In `app.py`

Now we go back to the local project and update the tracking URI in `app.py`.

Earlier, we had kept:

```python
remote_server_uri = ""
```

Now we replace it with the actual EC2 MLflow URL, such as:

```python
remote_server_uri = "http://<public-ip>:5000"
```

## Why This Step Is Necessary

Until we update this variable:

- our local script does not know where the remote MLflow server is
- experiment logs cannot be sent to EC2

So this step connects the local code to the cloud tracking server.

## Step 14. Set The MLflow Tracking URI Locally

Before running the project, we set the tracking URI in our local terminal:

```bash
export MLFLOW_TRACKING_URI=http://<public-ip>:5000
```

## Why This Step Matters

This makes sure the local process knows exactly which MLflow tracking server it should use.

## Step 15. Run `app.py`

After setting the tracking URI correctly, we run the script:

```bash
python app.py
```

Now the experiment should run successfully and the model should be logged to the remote MLflow server.

## What We Expect To See

We should see successful logging output, and the run should now appear in the MLflow UI hosted on EC2.

This means:

- parameters are logged
- metrics are logged
- artifacts are logged
- model information is registered in MLflow

## Step 16. Verify The Run In MLflow UI

Now when we refresh the MLflow UI in the browser, we should see the tracked experiment.

Inside the UI we can inspect:

- run details
- metrics like `RMSE`, `MAE`, and `R2`
- parameters like `alpha` and `l1_ratio`
- logged model artifacts

## Artifacts Visible In The UI

The artifacts section can show files such as:

- model files
- `requirements.txt`
- other generated MLflow files

This confirms that the run is not only logged as metadata but also stores useful outputs.

## Step 17. Verify The Artifacts In S3

After the run succeeds, we also check the S3 bucket.

When we refresh the bucket contents, we should see new folders created by MLflow.

These folders contain:

- experiment artifact directories
- model files
- outputs generated during the run

## Why This Verification Is Important

Checking S3 confirms that:

- the artifact root is correctly configured
- EC2 can successfully write to S3
- MLflow is storing remote artifacts as expected

So we verify the setup in two places:

- MLflow UI for experiment tracking
- S3 for artifact storage

## Step 18. Update The Project README

At this stage, it is also useful to update the project `README.md` with:

- the MLflow tracking URI
- the EC2 commands used
- the setup steps followed

This helps us because:

- the setup has many steps
- it is easier to repeat the process later
- the README becomes a ready-made checklist

## Step 19. Clean Up AWS Resources After Practice

After the experiment tracking has been verified, the final step is cleanup.

This is extremely important in AWS practice work.

## Terminate The EC2 Instance

We should terminate the EC2 instance once we are done.

Why:

- running instances may continue generating charges
- unused resources create unnecessary cost

So after testing, we should stop or terminate the instance properly.

## Delete The IAM User If It Was Created Only For Practice

If the IAM user was created only for this setup, we should also delete it after use.

This helps because:

- unused credentials should not remain active
- it reduces security risk
- it keeps the AWS account cleaner

## What About The S3 Bucket

The S3 bucket can remain if we want to keep the artifacts.

Usually, it does not create the same kind of immediate compute cost as EC2.

Still, we should be aware of:

- stored data
- bucket permissions
- whether we still need it

## What We Complete At This Stage

By the end of this part, we have:

- configured the EC2 machine for MLflow
- installed `mlflow`, `awscli`, `boto3`, and environment tools
- configured AWS credentials inside EC2
- launched the MLflow tracking server on port `5000`
- connected the local `app.py` to the remote tracking URI
- logged an experiment successfully
- verified the run in MLflow UI
- verified the artifacts in S3
- cleaned up AWS resources

## Commands We Want To Remember

### Update Package List

```bash
sudo apt update
```

### Install MLflow In EC2

```bash
pipenv install mlflow
```

### Install AWS CLI In EC2

```bash
pipenv install awscli
```

### Install `boto3`

```bash
pipenv install boto3
```

### Activate `pipenv` Shell

```bash
pipenv shell
```

### Configure AWS Inside EC2

```bash
aws configure
```

### Start MLflow Server

```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root s3://mlflow-tracking-1 --host 0.0.0.0 --port 5000
```

### Run Local Script

```bash
python app.py
```

### Export Tracking URI

```bash
export MLFLOW_TRACKING_URI=http://<public-ip>:5000
```

## One-Line Summary

Here we complete the AWS-based MLflow setup by running the tracking server on EC2, storing artifacts in S3, connecting the local training script to the remote URI, verifying the run in MLflow and S3, and cleaning up the cloud resources afterward.
