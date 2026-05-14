# DVC Notes

## What is DVC?

DVC stands for **Data Version Control**.

It is an MLOps tool used to:

- version datasets
- version model files
- track changes in large files such as images, audio, video, text, CSVs, and ML artifacts
- make ML workflows repeatable and reproducible

In simple words:

- **Git** is great for tracking code
- **DVC** is great for tracking data and model files

## Why do we need DVC?

In machine learning projects, data changes over time.

Examples:

- new rows are added to a dataset
- files are cleaned or updated
- new model versions are trained

If we do not track those changes, then later we may not know:

- which dataset version was used
- which model file belongs to which experiment
- how a result was produced

DVC helps solve this problem by making data and model versioning easier.

## DVC vs Git

### Git

Git mainly tracks:

- source code
- config files
- small text-based project files

### DVC

DVC mainly tracks:

- datasets
- model artifacts
- large files not suitable for Git

### How they work together

- Git tracks the code and DVC metadata files
- DVC tracks the actual data/model content

So in an ML project, **Git + DVC** is a very common combination.

## Main idea behind DVC tracking

When we run `dvc add` on a file:

1. DVC starts tracking that file.
2. Git stops tracking the real file content directly.
3. DVC creates a `.dvc` file for that data file.
4. DVC stores the actual file content in its cache.
5. The `.dvc` file contains a reference, including an **MD5 hash** of the file content.

That means DVC does not mainly rely on storing the whole large file in Git.
Instead, Git tracks the small metadata file, and DVC manages the real data through cache and remote storage.

## Important DVC concepts

### 1. `dvc init`

This initializes DVC in the project.

It creates the `.dvc` folder and related config files.

### 2. `.dvc` file

Example: `data.txt.dvc`

This file stores metadata such as:

- file path
- hash/reference to the tracked content

Git tracks this file.

### 3. Cache

DVC stores actual tracked content in a cache directory.

The file content is saved in cache using a hash-based structure.

### 4. MD5 hash

When file content changes, its hash changes too.

So every version of the data can be identified and linked correctly.

### 5. `dvc checkout`

This command restores the correct version of data based on the current Git-tracked DVC metadata.

Very important idea:

- `git checkout` changes the tracked code and `.dvc` metadata
- `dvc checkout` restores the corresponding actual data file

## Basic workflow

### Step 1: Create project and environment

- create a new folder
- create a virtual environment
- activate it

### Step 2: Initialize Git

```bash
git init
```

### Step 3: Install DVC

```bash
pip install dvc
```

### Step 4: Initialize DVC

```bash
dvc init
```

This creates DVC-related files such as:

- `.dvc/`
- `.dvcignore`
- config files

### Step 5: Create a data file

Example:

```text
data/data.txt
```

Initial content:

```text
this is the first version
```

### Step 6: Track the file with DVC

```bash
dvc add data/data.txt
```

After this:

- DVC creates `data/data.txt.dvc`
- DVC adds the actual file to cache
- Git should track the `.dvc` file
- the real data file is ignored by Git

### Step 7: Commit DVC metadata with Git

```bash
git add data/data.txt.dvc
git add data/.gitignore
git commit -m "track first version of data"
```

## What happens when data changes?

Suppose `data.txt` changes from:

```text
this is the first version
```

to:

```text
this is the second version
```

Then we run:

```bash
dvc add data/data.txt
```

What changes?

- DVC creates a new hash for the new content
- cache stores the new version
- `data.txt.dvc` gets updated

Then we commit the updated metadata:

```bash
git add data/data.txt.dvc
git commit -m "second version"
```

The same process happens again for a third version or any later version.

## How version rollback works

This is one of the most important practical ideas in DVC.

To go back to an older version:

1. Checkout the older Git commit:

```bash
git log
git checkout <commit_id>
```

2. Restore the correct data version:

```bash
dvc checkout
```

Why both commands?

- `git checkout` moves the project to an older metadata state
- `dvc checkout` uses that metadata to restore the matching data file

To return to the latest version:

```bash
git checkout main
dvc checkout
```

## Why this is powerful

DVC is useful because it helps us:

- track dataset versions properly
- track model file versions
- manage large files outside normal Git tracking
- reproduce old results
- move between different data versions safely

This becomes very useful in real ML projects where:

- datasets keep changing
- models are large
- multiple experiments are run
- collaboration is required

## Remote storage idea

Initially, DVC stores data in the local cache.

Later, the cache can be connected to remote storage such as:

- S3
- Google Cloud
- Azure Blob
- Google Drive

So:

- Git can store code and DVC metadata
- DVC remote storage can store large data/model files

This is one reason DVC is more suitable than Git alone for ML data and large artifacts.

## Quick exam-style revision

- DVC stands for **Data Version Control**.
- DVC is used to track **data files and model files**.
- Git is used mainly to track **code and metadata files**.
- `dvc init` initializes DVC in a project.
- `dvc add <file>` starts tracking a file with DVC.
- DVC creates a `.dvc` file containing metadata and file hash information.
- Actual file content is stored in the **DVC cache**.
- When file content changes, its **hash changes**.
- `git checkout` changes commit state.
- `dvc checkout` restores the correct data version for that state.
- DVC can use remote storage like **S3, GCP, Azure, or Google Drive**.

## One-line summary

DVC is a tool that works with Git to version datasets and ML artifacts, using metadata, hashes, and cache so we can reproduce and restore different data versions easily.

