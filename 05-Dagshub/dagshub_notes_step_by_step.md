# DagsHub Notes Step by Step

These notes are organized into a clear step-by-step study format.

The flow of learning is:

1. Understand what DagsHub is
2. Understand why it is useful in MLOps
3. Create a DagsHub repository
4. Connect local project code to DagsHub
5. Use DVC with DagsHub to version data
6. Understand how DagsHub, Git, DVC, and MLflow work together

---

## 1. What is DagsHub?

DagsHub is an **AI/ML collaboration platform** that can act as a **remote repository** for machine learning projects.

It supports work around:

- experiments
- datasets
- models
- collaboration
- reproducibility

It is especially useful when a project is being done by:

- multiple data scientists
- multiple ML engineers
- multiple team members working on different modules

In such cases, everyone needs a shared place where they can:

- see code
- see data versions
- compare experiments
- collaborate on the same project

That shared place can be DagsHub.

---

## 2. Why DagsHub is useful in MLOps

DagsHub fits naturally with the MLOps tools used in ML projects:

- **Git** for code tracking
- **DVC** for data and model versioning
- **MLflow** for experiment tracking

DagsHub becomes powerful because it can bring these together in one remote setup.

### Main idea

In local development:

- MLflow can run locally
- code may be stored locally
- data may be stored locally

But in team projects we usually want a **remote and collaborative setup**.

DagsHub helps with that by providing a hosted place where you can:

- maintain project code
- manage data with DVC
- log MLflow experiments
- collaborate with teammates

---

## 3. Main features

DagsHub supports these important capabilities:

### 3.1 Code versioning

Like GitHub, DagsHub can store and manage Git-based project code.

### 3.2 Data versioning

With DVC, DagsHub can help store and version:

- datasets
- model files
- large ML artifacts

### 3.3 Experiment tracking

DagsHub can be used with MLflow so that experiments are tracked in a remote collaborative place instead of only on a local machine.

### 3.4 Model registry and lineage

Important platform features include:

- model registry
- data and model lineage
- dataset management

### 3.5 Collaboration

It also supports:

- inviting collaborators
- discussions around experiments or files
- project sharing

### 3.6 Integration with other tools

DagsHub can integrate with many parts of an MLOps stack, such as:

- TensorFlow
- scikit-learn
- Pandas
- Hugging Face
- Keras
- AWS
- Azure
- Google Cloud

---

## 4. DagsHub vs GitHub

One of the clearest ways to understand DagsHub is to compare it with GitHub.

### GitHub mainly gives you

- code versioning
- Git-based collaboration

### DagsHub gives you

- code versioning
- data versioning support through DVC
- experiment logging support through MLflow

### Simple comparison

GitHub is mainly for code collaboration.

DagsHub is more ML-focused because it supports:

- code
- data
- experiments

This is why it is useful in MLOps projects.

---

## 5. Step-by-step: Getting started with DagsHub

This section gives a clean getting-started flow.

### Step 1: Create an account

Go to DagsHub and sign up.

You can sign up using:

- GitHub
- Google

After signing up, log in to your DagsHub account.

### Step 2: Create a new repository

After login, create a new repository.

Common repository creation options include:

- blank repository
- repository from templates
- connect an existing repository

You can also connect repositories from platforms such as:

- GitHub
- GitLab
- Bitbucket

### Step 3: Choose repository type

For a simple start, create a **blank repository**.

Example:

- repository name like `demo-dagshub`
- public or private visibility

Then click **Create Repository**.

### Step 4: Understand what you see after creation

After repository creation, the repository page looks somewhat similar to GitHub.

But the important difference is that DagsHub gives project sections related to:

- data
- Git
- DVC
- experiments
- models
- collaboration

DagsHub can also provide remote storage and can connect to storage systems like:

- S3
- Google Drive
- cloud buckets

---

## 6. Step-by-step: Start a local project connected to DagsHub

This is the practical local-project workflow.

### Step 1: Clone the DagsHub repository

After creating the empty repo on DagsHub, clone it locally.

General idea:

```bash
git clone <dagshub_repo_url>
```
If it ask for credentials, then use your 
1. dagshub username
2. dagshub access token: 
    * go to dagshub setting (your profile)
    * access token
    * copy the token and paste it as password 

Then move inside the cloned repository:

```bash
cd <repo_name>
```

### Step 2: Open the project in VS Code

A common command here is:

```bash
code .
```

### Step 3: Add an initial file like `README.md`

Because the repo is empty, create a `README.md` file first so there is something to commit.

### Step 4: Commit and push the initial code

Typical Git flow:

```bash
git add README.md
git commit -m "first commit"
git branch -M main
git push -u origin main
```

After this, the repository will show at least one tracked file on DagsHub.

---

## 7. Step-by-step: Prepare environment for DVC + DagsHub

Next, prepare an isolated environment and install the required packages.

### Step 1: Create a virtual environment

Example command:

```bash
conda create -p venv python==3.10 -y
```

This creates a virtual environment folder in the project itself.

### Step 2: Ignore the environment folder in Git

Create `.gitignore` and add the environment folder name:

```text
venv
```

This prevents the environment from being tracked in Git.

### Step 3: Create `requirements.txt`

Useful packages for this setup are:

- `dagshub`
- `dvc`

Extra S3 support may also be needed when using the DagsHub DVC remote.

### Step 4: Activate the environment

The environment can be activated from different terminals depending on your shell.

### Step 5: Install requirements

General idea:

```bash
pip install -r requirements.txt
```

---

## 8. Step-by-step: Add data to the project

Now the next part is data tracking.

### Step 1: Create a `data` folder

Inside the project, create a folder such as:

```text
data/
```

### Step 2: Add a dataset

Example dataset:

```text
data/data.csv
```

This dataset becomes the example file that DVC will manage.

---

## 9. Step-by-step: Initialize DVC in the local project

Now DVC is initialized inside the cloned DagsHub project.

### Command

```bash
dvc init
```

### What this does

It creates DVC-related files such as:

- `.dvc/`
- `.dvc/config`
- `.dvcignore`

This means the project is now ready for DVC-based data versioning.

---

## 10. Step-by-step: Track the dataset with DVC

### Command

```bash
dvc add data/data.csv
```

### What happens after this

When you run `dvc add`, DVC:

- starts tracking the dataset
- creates a `.dvc` metadata file
- adds the actual file content to the DVC cache
- ensures the real data file is not directly tracked by Git

After this, Git should track:

- `data/.gitignore`
- `data/data.csv.dvc`

### Git commands

```bash
git add data/.gitignore
git add data/data.csv.dvc
git commit -m "added data.csv with DVC"
```

### Important understanding

At this point:

- Git is tracking the DVC metadata
- DVC is tracking the actual dataset

---

## 11. Step-by-step: Configure DagsHub as a DVC remote

This is one of the most important advanced parts of the setup.

The project code is already in DagsHub through Git.

Now we also want the **actual DVC-managed data** to be stored in the **DagsHub DVC remote**.

### Where to find the setup information

Inside the DagsHub repository UI, there is a remote setup area where DagsHub provides:

- remote name setup
- endpoint URL
- access key
- secret access key

### Step 1: Add the DVC remote

Copy the remote setup command from DagsHub.

General pattern:

```bash
dvc remote add origin <remote_location>
```

This is typically an S3-compatible DagsHub remote.

### Step 2: Set the remote endpoint URL

Then configure the endpoint URL provided by DagsHub.

General pattern:

```bash
dvc remote modify origin endpointurl <dagshub_endpoint>
```

### Step 3: Set access key ID

Copy the access key from the DagsHub UI and configure it for the remote.

### Step 4: Set secret access key

Copy the secret key from the DagsHub UI and configure it as well.

### Step 5: Verify remote setup

Then verify the remote configuration and confirm that `origin` is the configured remote.

```bash
git remote -v
dvc status -r <remote-name> (e.g., dvc status -r origin)  # to check connection
```

### Important idea

This remote is where DVC will store the actual versioned data for the project.

So now:

- code metadata goes through Git
- actual dataset content goes through the DVC remote in DagsHub

---

## 12. Extra package note

When interacting with the DagsHub DVC remote, an error related to S3 support may appear.

The lesson from that part is:

- DagsHub DVC remote uses an S3-compatible backend
- your DVC setup may need S3 support installed

In that case, install the missing support and retry the command.

### Practical takeaway

If `dvc pull` or `dvc push` complains about S3 support, install the required DVC S3 dependency and try again.

---

## 13. Step-by-step: Pull and push data with DVC remote

Once the remote is configured, use `origin` as the DVC remote name.

### Pull current remote data

```bash
dvc pull -r origin
```

Purpose:

- fetch current tracked data from remote

### Push local tracked data

```bash
dvc push -r origin
```

Purpose:

- upload local DVC-tracked data to the DagsHub remote

### Push Git-tracked files too

After `dvc push`, the Git-tracked project files still need to be pushed:

```bash
git push origin main
```

### Important workflow idea

For a complete update, both are needed:

- `dvc push` for data
- `git push` for code and DVC metadata

---

## 14. What appears in DagsHub after pushing

After pushing, DagsHub shows:

- Git enabled
- DVC enabled
- data pipeline view
- DVC-managed data files
- file history

The dataset appears as a DVC-managed file in the repository UI.

You can also inspect:

- file content
- commit history
- changes across versions

---

## 15. Step-by-step: Update the dataset version

To create a second dataset version, modify the CSV, for example by deleting some rows.

### Step 1: Modify the data file

Example idea:

- remove some records from `data/data.csv`

### Step 2: Re-track it with DVC

```bash
dvc add data/data.csv
```

This updates the DVC metadata because the file content changed.

### Step 3: Add and commit updated metadata in Git

A simple Git update flow is:

```bash
git add .
git commit -m "second commit"
```

### Step 4: Sync the new version

```bash
dvc pull -r origin
dvc push -r origin
git push origin main
```

### Result

Now DagsHub can show:

- the new dataset version
- the previous dataset version
- history and comparisons across commits

---

## 16. End-to-end understanding: Git + DVC + MLflow + DagsHub

One of the most important ideas in this setup is the division of responsibilities.

### Git

Git tracks:

- code
- README
- configuration files
- DVC metadata files

### DVC

DVC tracks:

- datasets
- model files
- large artifacts

### MLflow

MLflow tracks:

- experiments
- runs
- metrics
- model logging information

### DagsHub

DagsHub acts as the shared remote platform where:

- Git code can be hosted
- DVC data can be remotely stored
- MLflow experiments can be logged
- teams can collaborate

This is why DagsHub is a very useful MLOps platform.

---

## 17. Structured workflow you should remember

If you want to remember the process in one sequence, use this:

1. Create a DagsHub account
2. Create a DagsHub repository
3. Clone the repo locally
4. Add initial code like `README.md`
5. Push initial Git commit
6. Create and activate virtual environment
7. Install `dagshub`, `dvc`, and any required remote support
8. Add dataset into `data/`
9. Run `dvc init`
10. Run `dvc add <data_file>`
11. Commit `.dvc` metadata with Git
12. Configure DagsHub DVC remote from the repository UI
13. Run `dvc pull -r origin`
14. Run `dvc push -r origin`
15. Run `git push origin main`
16. Make data changes later
17. Repeat `dvc add`, Git commit, `dvc push`, and `git push`

---

## 18. Why this matters in real projects

This setup becomes useful because in ML projects:

- code changes
- data changes
- experiments change
- multiple people work together

Without a proper remote system, it becomes hard to manage all these pieces.

DagsHub helps by giving one place for:

- remote code collaboration
- remote DVC data storage
- remote MLflow experiment tracking

---

## 19. Quick revision points

- DagsHub is an ML-focused collaboration platform.
- It can be used as a remote repository for MLOps projects.
- It supports Git, DVC, and MLflow workflows.
- Git tracks code.
- DVC tracks datasets and large files.
- MLflow tracks experiments.
- DagsHub can host all of these in a collaborative remote setup.
- `dvc add` tracks the dataset with DVC.
- DVC metadata is committed with Git.
- DagsHub provides a DVC remote configuration.
- `dvc push` uploads DVC data.
- `git push` uploads code and metadata.
- DagsHub can show DVC-managed files and their history.

---

## 20. One-line summary

DagsHub is a collaborative MLOps platform that combines Git-based code hosting, DVC-based data versioning, and MLflow-based experiment tracking in one remote repository workflow.

## Code example
https://dagshub.com/amaresh/demo-dagshub
