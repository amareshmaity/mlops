# AWS Cloud Setup For MLflow Tracking

## What We Are Doing

In this part, we prepare the AWS infrastructure required to run an MLflow tracking server on a remote EC2 machine.

We will:

1. Log in to AWS
2. Create an IAM user
3. Create IAM access keys
4. Install AWS CLI locally
5. Configure AWS CLI locally
6. Create an S3 bucket for MLflow artifacts
7. Launch an EC2 instance
8. Open port `5000`
9. Connect to the EC2 machine

<br/>

## Main Goal

The goal is to prepare AWS so that:

```text
Local Machine
     │
     │ MLflow tracking requests
     ▼
    EC2
     │
     │ MLflow Tracking Server
     │
     └──────────► S3
                 MLflow Artifacts
```

The setup flow is:

```text
AWS Login
   ↓
IAM User
   ↓
Access Keys
   ↓
AWS CLI
   ↓
S3 Bucket
   ↓
EC2 Instance
   ↓
Security Group
   ↓
Connect To EC2
```

<br/>

## Step 1. Log In To AWS

Open the **AWS Management Console** and sign in.

From the AWS console, we will use:

- IAM
- S3
- EC2

<br/>

## Step 2. Create An IAM User

Go to:

```text
IAM → Users → Create user
```

Example username:

```text
MLflow-user
```

### Why Create A Separate IAM User?

A separate IAM user is useful for learning because it:

- avoids using the root account directly
- keeps credentials separate
- makes permissions easier to manage

### Instance

- select single instead of group

### Permissions

- assign **administrator access**

For this learning setup, the course uses administrator access so the user can work with services such as:

- S3
- EC2
- related AWS services

> **Production note:** Do not normally give administrator access for a real project. Use **least-privilege permissions** and grant only the access required by the application.

<br/>

## Step 3. Create IAM Access Keys

Open the IAM user and go to:

```text
Security credentials → Access keys
```

Create a new access key.

Select:

```text
Command Line Interface (CLI)
```

AWS will provide:

```text
AWS Access Key ID
AWS Secret Access Key
```

Store these securely.

> **Important:** The secret access key is sensitive. Never commit it to Git, put it in a README, or expose it in screenshots.

<br/>

## Step 4. Install AWS CLI On Your Local Machine

AWS CLI must be installed on the machine from which you want to run AWS commands.

The purpose of setting up AWS CLI locally is to allow your local computer to communicate with AWS services from the terminal.

```text
Your Laptop
    │
    │ AWS CLI
    │
    ▼
   AWS
 ┌───────────────┐
 │ S3            │
 │ EC2           │
 │ IAM           │
 │ CloudWatch    │
 │ etc.          │
 └───────────────┘
```

Install the appropriate AWS CLI version for your operating system:

- Windows
- macOS
- Linux

Note: choose single user and then download .msi file

After installation, verify it:

```bash
aws --version
```

You can also run:

```bash
aws
```

to display the AWS CLI help output.

<br/>

## Step 5. Configure AWS CLI Locally

Now configure AWS CLI using the access keys created in Step 3:

```bash
aws configure
```

AWS asks for:

```text
AWS Access Key ID:
AWS Secret Access Key:
Default region name:
Default output format:
```

For this setup, enter:

```text
AWS Access Key ID: <IAM_ACCESS_KEY>
AWS Secret Access Key: <IAM_SECRET_KEY>
Default region name: us-east-1
Default output format: json
```

### Verify AWS CLI Authentication

Run:

```bash
aws sts get-caller-identity
```

If the configuration is correct, AWS returns information about the authenticated identity.

Also test S3 access:

```bash
aws s3 ls
```

<br/>

## Step 6. Create The S3 Bucket

S3 will be used to store MLflow artifacts.

Examples of artifacts include:

- model files
- run artifacts
- experiment outputs

Go to:

```text
S3 → Create bucket
```

Example bucket name:

```text
mlflow-tracking-1
```

### Region

Use:

```text
us-east-1
```

Keep related AWS resources in the same region when practical.

### Public Access

For this learning setup, the original course configuration disables:

```text
Block all public access
```

However, **do not make an MLflow artifact bucket public unless there is a specific reason**.

For a safer setup:

- keep the S3 bucket private
- use IAM permissions
- allow only the required AWS identities to access the bucket

<br/>

## Step 7. Verify The S3 Bucket From The Terminal

After creating the bucket, verify it from your local terminal:

```bash
aws s3 ls
```

You should see the bucket.

You can also directly check:

```bash
aws s3 ls s3://mlflow-tracking-1/
```

At this point, the local AWS CLI should be able to communicate with S3.

<br/>

## Step 8. Launch An EC2 Instance

Now create the machine that will host the MLflow tracking server.

Go to:

```text
EC2 → Launch instance
```

### Basic Configuration

Use the configuration from this setup:

| Setting       | Value             |
| ------------- | ----------------- |
| Instance name | `MLflow-tracking` |
| AMI           | Ubuntu            |
| Instance type | `t2.micro`        |
| Storage       | `8 GB`            |
| Region        | `us-east-1`       |

### Why Ubuntu?

Ubuntu is commonly used for server environments and works well for this setup.

### Why `t2.micro`?

It is a small instance suitable for a basic learning setup.

> AWS pricing and free-tier eligibility can change. Check the current AWS pricing/free-tier terms before launching resources.

<br/>

## Step 9. Create Or Select An EC2 Key Pair

During EC2 creation, AWS asks for a key pair.

If you do not already have one, create it.

Example name:

```text
MLflow-tracking
```

Download the private key:

```text
MLflow-tracking.pem
```

### Why Is The `.pem` File Needed?

The `.pem` file is used to authenticate when connecting to the EC2 instance through SSH.

The purpose of `.pem` file is to access EC2 server from your local cmd.

For example:

```bash
ssh -i MLflow-tracking.pem ubuntu@<public-ip>
```

Keep the `.pem` file secure.

> The `.pem` file is **not** an AWS CLI credential and is not used with `aws configure`.

<br/>

### `.pem` VS 'aws cli` Authentication

|             | `.pem` file                    | AWS CLI login               |
| ----------- | ------------------------------ | --------------------------- |
| Purpose     | Log into **EC2 server**        | Access **AWS services**     |
| Used by     | SSH                            | AWS CLI                     |
| Credentials | SSH private key                | IAM Access Key + Secret Key |
| Example     | `ssh -i key.pem ubuntu@IP`     | `aws s3 ls`                 |
| Gives you   | Terminal access **inside EC2** | Permission to call AWS APIs |

<br/>

## Step 10. Configure EC2 Network Access

During EC2 creation, configure the security group.

The MLflow server will use:

```text
Port: 5000
Protocol: TCP
```

Add an inbound rule for port `5000`.

For the learning setup:

```text
Type: Custom TCP
Port: 5000
Source: 0.0.0.0/0
```

### Why Port `5000`?

MLflow commonly runs on port `5000`.

The browser will later access:

```text
http://<public-ip>:5000
```

### Security Warning

`0.0.0.0/0` allows connections from any IPv4 address.

This is convenient for learning but exposes the port publicly.

For a safer setup, restrict the source to a known IP address whenever possible.

<br/>

## Step 11. Launch The EC2 Instance

Review the configuration and launch the instance.

After launching, the instance initially appears as:

```text
Pending
```

Wait until it becomes:

```text
Running
```

<br/>

## Step 12. Get The EC2 Public IP

Open the EC2 instance details and find:

```text
Public IPv4 address
```

Example:

```text
54.xxx.xxx.xxx
```

You will use this address later to:

- connect to EC2
- open the MLflow UI
- configure the local MLflow tracking URI

<br/>

## Step 13. Connect To The EC2 Machine

There are two common approaches.

### Option A — EC2 Instance Connect

From the EC2 instance page:

```text
Connect → EC2 Instance Connect → Connect
```

This opens a browser-based terminal.

### Option B — SSH Using The `.pem` File

From your local terminal:

```bash
chmod 400 MLflow-tracking.pem
```

Then:

```bash
ssh -i MLflow-tracking.pem ubuntu@<public-ip>
```

For example:

```bash
ssh -i MLflow-tracking.pem ubuntu@54.xxx.xxx.xxx
```

> The exact SSH username depends on the AMI. For Ubuntu, it is commonly `ubuntu`.

<br/>

## Step 14. Confirm You Are Inside EC2

Once connected, you should see a shell prompt similar to:

```text
ubuntu@ip-xxx-xxx-xxx-xxx:~$
```

You are now working **inside the EC2 machine**.

The next part will configure this machine for MLflow.

<br/>

## What We Have Completed

At this stage, we have:

- [x] Logged in to AWS
- [x] Created an IAM user
- [x] Created IAM access keys
- [x] Installed AWS CLI locally
- [x] Configured AWS CLI locally
- [x] Verified AWS authentication
- [x] Created an S3 bucket
- [x] Launched an EC2 instance
- [x] Created/selected an EC2 key pair
- [x] Opened port `5000`
- [x] Obtained the EC2 public IP
- [x] Connected to the EC2 machine

<br/>

## Important Concepts To Remember

### IAM Access Key vs EC2 `.pem` Key

These are different credentials for different purposes.

| Credential            | Used For                   |
| --------------------- | -------------------------- |
| IAM Access Key ID     | AWS API/CLI authentication |
| IAM Secret Access Key | AWS API/CLI authentication |
| EC2 `.pem` file       | SSH authentication to EC2  |

```text
IAM Access Keys
      ↓
   AWS CLI
      ↓
AWS Services
```

```text
EC2 .pem
    ↓
   SSH
    ↓
EC2 Instance
```

<br/>

## Essential Commands

### AWS CLI

#### Check AWS CLI

```bash
aws --version
```

#### Configure AWS CLI

```bash
aws configure
```

#### Verify AWS Identity

```bash
aws sts get-caller-identity
```

#### List S3 Buckets

```bash
aws s3 ls
```

#### Check MLflow S3 Bucket

```bash
aws s3 ls s3://mlflow-tracking-1/
```

<br/>

### EC2 SSH

#### Protect The `.pem` File

```bash
chmod 400 MLflow-tracking.pem
```

#### Connect To Ubuntu EC2

```bash
ssh -i MLflow-tracking.pem ubuntu@<public-ip>
```

<br/>

## One-Line Summary

**Configure AWS access with IAM and AWS CLI, create an S3 bucket for MLflow artifacts, launch an Ubuntu EC2 instance, open port `5000`, and connect to the instance so the MLflow tracking server can be configured next.**
