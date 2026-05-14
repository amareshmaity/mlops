# AWS Cloud Setup For MLflow Tracking

## What We Are Doing In This Part

Here we are setting up the AWS side of the project so that MLflow tracking can run on a remote `EC2` machine.

In the previous part, we had already:

- completed the local ML project code
- added MLflow logging
- kept a placeholder for the remote tracking URI
- documented the overall AWS setup steps in the project `README.md`

Now we are actually preparing the cloud infrastructure needed for tracking.

The main tasks here are:

- log in to the AWS console
- create an IAM user
- generate access keys
- configure AWS CLI locally
- create an S3 bucket
- create an EC2 instance
- open port `5000`
- connect to the EC2 machine

## Main Goal Of This Setup

The main goal is to make sure that our MLflow tracking server can run inside AWS and later receive experiment logs from our local machine.

The setup flow is:

`AWS login -> IAM user -> AWS CLI configuration -> S3 bucket -> EC2 instance -> security group -> connect to server`

## Why This Part Is Important

Without this AWS setup:

- the remote tracking URI cannot be used
- MLflow cannot run on EC2
- experiment artifacts cannot be stored in S3
- the local project cannot send runs to a cloud-hosted MLflow server

So this part builds the actual infrastructure needed for remote experiment tracking.

## Step 1. Log In To The AWS Console

The first step is to log in to the `AWS Management Console`.

We can do this by searching for:

- `AWS console login`
- or `AWS login console`

Once logged in, we reach the AWS dashboard where we can access services like:

- `IAM`
- `S3`
- `EC2`

## Why This Step Comes First

We need the AWS console because all the cloud resources for this project will be created from there.

This includes:

- the IAM user
- the S3 bucket
- the EC2 instance

## Step 2. Create An IAM User

The next step is to create a dedicated IAM user for this setup.

We do this from:

```text
IAM -> Users -> Create user
```

A sample name used here is:

```text
MLflow-user
```

## Why We Create A Separate IAM User

Creating a separate IAM user is useful because:

- it avoids using the root account directly
- credentials become easier to manage
- access can be controlled more safely
- it matches better with real project practice

## Access Given To The IAM User

In this setup, administrator access is attached directly to the IAM user.

This is done mainly for learning convenience because we need access to:

- `S3`
- `EC2`
- related AWS services

## Important Real-World Note

For learning, administrator access makes setup easier.

But in real company environments:

- full admin access is usually not given
- users are given only the permissions they actually need
- least-privilege access is the safer approach

So for real projects, it is better to use only the required permissions.

## Step 3. Create Access Keys

After creating the IAM user, we go into:

```text
Security credentials -> Access keys
```

Then we create a new access key.

While creating the key, we choose:

```text
Command Line Interface (CLI)
```

## Why We Choose CLI Access

We choose CLI access because we want to use:

```bash
aws configure
```

This will allow our local machine to talk to AWS services from the terminal.

## Important Credentials Generated Here

When the key is created, AWS gives us:

- `AWS Access Key ID`
- `AWS Secret Access Key`

We should store these carefully.

Downloading the CSV is a good idea so we can refer to the credentials later if needed.

## Security Reminder

These keys are sensitive.

If someone else gets them, they may be able to access our AWS account resources depending on the attached permissions.

So we should:

- never expose them publicly
- avoid sharing screenshots with visible keys
- delete unused users or keys after practice

## Step 4. Install AWS CLI

Before configuring AWS from the terminal, we need to install `AWS CLI`.

We can search for:

```text
aws cli download
```

AWS provides installation methods for:

- `Windows`
- `Linux`
- `Mac`

## Platform-Specific Idea

### Windows

We can download the MSI installer and run it directly.

### Mac

We can use the GUI installer provided by AWS.

### Linux

We can follow the shell-based installation steps from the AWS documentation.

## How We Check AWS CLI Installation

After installation, we can verify it from the terminal using:

```bash
aws
```

If AWS CLI is installed correctly, we should see help output from the command.

## Why This Check Matters

If this command does not work:

- AWS CLI is either not installed
- or it is not available in the system path

So checking it early saves time before configuration.

## Step 5. Configure AWS CLI Locally

Once AWS CLI is installed, we configure it using:

```bash
aws configure
```

This command asks for four things:

- AWS Access Key ID
- AWS Secret Access Key
- default region name
- default output format

## Values Used In This Setup

The values used here are:

- access key: from IAM user
- secret key: from IAM user
- region: `us-east-1`
- output format: `json`

## Why `aws configure` Is Important

This step links our local terminal with our AWS account.

That means tools and code can later access resources like:

- S3 bucket
- EC2 services
- MLflow artifact storage through AWS-backed resources

## Step 6. Understand What S3 Is

Before creating the bucket, it helps to understand what `S3` is.

`AWS S3` is an object storage service.

We can think of it as a cloud storage system that is commonly used to:

- store files
- store datasets
- store model artifacts
- store experiment-related outputs

## Why We Need S3 In This Project

In this MLflow setup, `S3` will be used to store experiment artifacts.

That means things like:

- model files
- run artifacts
- MLflow outputs

will be stored in the bucket.

Later, the MLflow server running on EC2 will work with this storage.

## Step 7. Create An S3 Bucket

Now we create a new S3 bucket from:

```text
S3 -> Create bucket
```

A sample bucket name used in this setup is:

```text
mlflow-tracking-1
```

## Region Check Before Creating The Bucket

Before creating the bucket, we should check the AWS region.

In this setup, the region used is:

```text
us-east-1
```

It is a good idea to keep the bucket and other services in the same region when possible.

## Public Access Setting

During bucket creation, the setup disables:

```text
Block all public access
```

Then AWS asks for confirmation that the bucket may become public.

## Practical Note About Public Access

This is done here to make the setup easier for learning and access from code.

But in real projects, public access should be handled carefully.

Safer practice usually means:

- keeping the bucket private
- using IAM policies properly
- exposing only what is necessary

## What The Bucket Will Contain

Right after creation, the bucket is empty.

Later, it will hold MLflow-related artifacts such as:

- run folders
- model files
- tracking outputs

## Step 8. Create An EC2 Instance

Now we create the machine that will host the MLflow server.

We do this from:

```text
EC2 -> Launch instance
```

## Basic EC2 Configuration Used Here

The setup uses:

- instance name: something like `MLflow-tracking`
- AMI: `Ubuntu`
- instance type: `t2.micro`
- storage: `8 GB`

## Why These Choices Make Sense

### Ubuntu

Ubuntu is commonly used and works well for server-side setup.

### `t2.micro`

This is chosen because it is lightweight and often falls under free-tier usage for learning accounts.

### `8 GB` Storage

This is usually enough for a basic MLflow tracking server setup.

## Key Pair Requirement

While launching the instance, AWS asks for a key pair.

If one is not already selected, we need to create a new key pair.

A sample name can be:

```text
MLflow-tracking
```

When the key pair is created, a `.pem` file gets downloaded.

## Why The Key Pair Matters

The key pair is generally used for secure access to the EC2 machine.

Even if we are not using it immediately in this part, it is still part of the EC2 creation process.

So we should keep the `.pem` file safely.

## Inbound Traffic Settings During Launch

During launch, the basic HTTP / HTTPS access options are enabled as needed.

But one more important port still needs to be opened manually:

- port `5000`

This is important because MLflow UI will run on that port.

## Step 9. Wait For The Instance To Start

After launching, the EC2 instance first appears in a:

- pending state

We wait until it changes to:

- running state

Only after that do we continue with the security settings and connection step.

## Step 10. Add Security Group Rule For Port 5000

This is one of the most important steps in the AWS setup.

After the instance is running, we go to:

```text
EC2 instance -> Security -> Security group -> Edit inbound rules
```

Then we add a new inbound rule:

- type: custom TCP
- port: `5000`
- source: `0.0.0.0/0`

## Why Port `5000` Is Required

MLflow tracking server usually runs on port `5000`.

If this port is not open:

- the browser cannot access the MLflow UI
- the tracking server may still run internally
- but we will not be able to open it from outside

## Important Note About `0.0.0.0/0`

Using `0.0.0.0/0` means the port is open from any IP address.

This is convenient for learning and testing, but it is not the safest option for production.

In real environments, it is better to:

- restrict access to known IPs
- use proper network controls
- avoid unnecessarily exposing services publicly

## Step 11. Connect To The EC2 Instance

Once the instance is running and the port rule is added, we connect to the machine.

We can do this through:

```text
EC2 Instance Connect
```

From the instance page, we click:

```text
Connect
```

This opens a browser-based shell connected to the EC2 machine.

## What We See After Connecting

After connection, we get a terminal prompt inside the EC2 machine.

This is where we will run the server-side commands in the next part.

That shell will be used to:

- update the system
- install Python and pip tools
- install MLflow
- install AWS CLI and `boto3`
- create the environment for the tracking server
- launch the MLflow server

## Why This Connection Step Matters

This confirms that:

- the instance is running
- we can reach the machine
- the environment is ready for server setup in the next part

## What We Complete At This Stage

By the end of this part, we have:

- logged in to AWS
- created an IAM user
- generated AWS access keys
- configured AWS CLI locally
- created an S3 bucket
- launched an EC2 instance
- added a custom inbound rule for port `5000`
- connected to the EC2 machine

## What Comes Next

After this setup, the next step is to configure the EC2 machine itself.

That includes:

- updating packages
- installing Python-related tools
- installing MLflow
- installing `awscli` and `boto3`
- configuring AWS on the server
- launching the MLflow tracking server

## AWS Steps We Want To Remember

### Configure AWS CLI

```bash
aws configure
```

### Verify AWS CLI

```bash
aws
```

## Cloud Resources Created Here

### IAM

- user for AWS access
- access keys for CLI configuration

### S3

- bucket for MLflow artifacts

### EC2

- Ubuntu instance for the MLflow server
- port `5000` opened for the tracking UI

## One-Line Summary

Here we prepare the AWS infrastructure for MLflow tracking by configuring AWS CLI, creating an IAM user, setting up an S3 bucket, launching an EC2 instance, and opening port `5000` for the MLflow server.
