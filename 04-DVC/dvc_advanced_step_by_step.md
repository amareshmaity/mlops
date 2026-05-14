# Advanced DVC Step-by-Step

This file is for the **next level of DVC learning** after basic `dvc init`, `dvc add`, and `dvc checkout`.

The goal is to learn DVC the way it is used in real MLOps projects.

## What you already know

By now, you should already be comfortable with:

- `git init`
- `dvc init`
- `dvc add`
- `.dvc` files
- DVC cache
- `git checkout`
- `dvc checkout`

If yes, then the next advanced topics should be learned in this order.

## Learning roadmap

1. Learn DVC remote storage
2. Learn `dvc push` and `dvc pull`
3. Learn DVC pipelines with `dvc stage add`
4. Learn `dvc repro`
5. Learn parameters, metrics, and plots
6. Learn DVC experiments
7. Learn team workflow with Git + DVC

---

## Step 1: Learn remote storage

### Why this matters

In real projects, the DVC cache on your local machine is not enough.

You usually want to store datasets and model files in a shared remote location such as:

- S3
- Google Drive
- Google Cloud Storage
- Azure Blob
- another local/shared folder

DVC uses **remote storage** to keep data and model files outside Git.

### Main commands

```bash
dvc remote add -d myremote <remote_path_or_url>
```

### Example with a local folder remote

```bash
dvc remote add -d localstorage E:\dvc-storage
```

What this does:

- creates a DVC remote named `localstorage`
- makes it the default remote because of `-d`

### Important idea

- Git stores code and DVC metadata
- DVC remote stores the actual large data/model files

### Practice task

1. Create a remote storage location
2. Add it with `dvc remote add`
3. Check `.dvc/config`

You should understand:

- where DVC data lives locally
- where DVC data lives remotely

---

## Step 2: Learn `dvc push` and `dvc pull`

### Why this matters

This is how data moves between your local cache and the remote storage.

### `dvc push`

```bash
dvc push
```

Purpose:

- uploads tracked data from local DVC cache to remote storage

### `dvc pull`

```bash
dvc pull
```

Purpose:

- downloads required tracked data from remote storage into your workspace/cache

### Real project meaning

Typical idea:

- `git push` sends code
- `dvc push` sends data/model artifacts

And on another machine:

- `git pull` gets code
- `dvc pull` gets data/model artifacts

### Practice task

1. Track a file with `dvc add`
2. Commit the `.dvc` file with Git
3. Run `dvc push`
4. Delete the local tracked file
5. Run `dvc pull`
6. Confirm the file comes back

### What you should understand

- Git alone is not enough for large ML files
- `dvc push` and `dvc pull` are the real sharing mechanism

---

## Step 3: Learn DVC pipelines with `dvc stage add`

### Why this matters

This is where DVC becomes much more powerful.

Instead of only versioning files, you start versioning the **workflow**.

Typical ML pipeline:

- data ingestion
- data preprocessing
- feature engineering
- model training
- model evaluation

DVC can describe these steps as stages in a pipeline.

### Main command

```bash
dvc stage add -n <stage_name> -d <dependency> -o <output> <command>
```

### Example

```bash
dvc stage add -n prepare -d src/prepare.py -d data/raw -o data/processed python src/prepare.py
```

This means:

- stage name = `prepare`
- dependencies = `src/prepare.py`, `data/raw`
- output = `data/processed`
- command = `python src/prepare.py`

### What gets created

DVC usually writes stage information into:

- `dvc.yaml`
- `dvc.lock`

### Important idea

A stage becomes invalid if:

- code changes
- dependency files change
- parameter values change

Then DVC knows the stage should run again.

### Practice task

Create a very small fake ML pipeline:

1. one script that reads input data
2. one script that processes it
3. one script that creates a dummy model output

Then define them as DVC stages.

---

## Step 4: Learn `dvc repro`

### Why this matters

Once stages are defined, `dvc repro` reruns the pipeline when needed.

### Main command

```bash
dvc repro
```

### What it does

- checks stage dependencies
- finds what changed
- reruns only the required stages in the correct order

This is very useful because you do not need to manually remember every pipeline step.

### Example flow

Suppose:

- you change preprocessing code
- training depends on preprocessing output

Then `dvc repro` can rerun:

- preprocess stage
- train stage
- evaluate stage

without rerunning unrelated work.

### Why this is good for MLOps

It gives you:

- reproducibility
- automation
- dependency-aware reruns

### Practice task

1. Create 2 or 3 DVC stages
2. Run `dvc repro`
3. Change one dependency
4. Run `dvc repro` again
5. Observe which stages rerun

---

## Step 5: Learn parameters, metrics, and plots

This is one of the most useful DVC features for ML workflows.

### 5.1 Parameters

Instead of hardcoding values in Python scripts, put them in `params.yaml`.

Example:

```yaml
learning_rate: 0.01
epochs: 10
batch_size: 32
```

Then your code reads from `params.yaml`.

When creating a stage, you can track params:

```bash
dvc stage add -n train -d src/train.py -d data/processed -p learning_rate,epochs,batch_size -o model.pkl python src/train.py
```

### Why parameters matter

If a parameter changes, DVC understands that the stage may need to be rerun.

### 5.2 Metrics

Metrics are values like:

- accuracy
- precision
- recall
- F1 score
- RMSE

These are usually written into files such as:

- `metrics.json`
- `metrics.yaml`

Example stage:

```bash
dvc stage add -n evaluate -d src/evaluate.py -d model.pkl -m metrics.json python src/evaluate.py
```

### Why metrics matter

You can compare model performance across runs and commits.

Useful command:

```bash
dvc metrics show
```

You may also use:

```bash
dvc metrics diff
```

### 5.3 Plots

Plots help compare learning curves and experiment outputs visually.

Examples:

- loss curve
- accuracy curve
- confusion matrix data

Example stage:

```bash
dvc stage add -n evaluate -d src/evaluate.py -d model.pkl --plots plots.csv python src/evaluate.py
```

Useful command:

```bash
dvc plots show
```

### Practice task

1. Create `params.yaml`
2. Create one training stage using `-p`
3. Save metrics into `metrics.json`
4. Save plot data into `plots.csv`
5. Run the pipeline
6. Inspect metrics and plots

---

## Step 6: Learn DVC experiments

### Why this matters

Experiment tracking is a big part of MLOps.

DVC provides experiment commands so you can compare multiple runs without manually creating many Git commits immediately.

### Main command family

```bash
dvc exp
```

Common subcommands:

- `dvc exp run`
- `dvc exp show`
- `dvc exp diff`
- `dvc exp apply`

### Simple idea

You change:

- params
- code
- dependencies

Then run:

```bash
dvc exp run
```

And DVC helps record and compare those experimental results.

### Useful learning outcome

You should understand the difference between:

- normal Git commits
- temporary or comparative DVC experiments

### Practice task

1. Change one parameter in `params.yaml`
2. Run `dvc exp run`
3. Change another parameter
4. Run `dvc exp run`
5. Compare them using `dvc exp show`

---

## Step 7: Learn the real team workflow

This is how DVC is commonly used in a collaborative project.

### Typical flow

One teammate:

1. updates code
2. updates data or pipeline
3. runs pipeline
4. commits Git-tracked files
5. runs `dvc push`
6. runs `git push`

Another teammate:

1. runs `git pull`
2. runs `dvc pull`
3. gets both code and matching data/model artifacts

### Key understanding

Use Git for:

- code
- `dvc.yaml`
- `dvc.lock`
- `.dvc` files
- `params.yaml`
- small metrics files if desired

Use DVC remote for:

- datasets
- model files
- pipeline outputs
- large artifacts

---

## Step 8: Best practices for MLOps projects

### Good habits

- keep raw data, processed data, and models in separate folders
- use `params.yaml` for tunable settings
- define ML steps as DVC stages
- commit `dvc.yaml`, `dvc.lock`, and `.dvc` files to Git
- push large data to DVC remote, not to Git
- use meaningful stage names like `prepare`, `train`, `evaluate`

### Common mistakes to avoid

- storing large datasets directly in Git
- forgetting `dvc push` after tracking new data
- hardcoding parameters in scripts
- not committing `dvc.yaml` or `.dvc` files
- treating DVC only as a file versioning tool and ignoring pipelines

---

## Suggested practice order for you

Follow this exact order:

1. Add a local remote storage
2. Practice `dvc push` and `dvc pull`
3. Create one simple `prepare` stage
4. Create one simple `train` stage
5. Run `dvc repro`
6. Add `params.yaml`
7. Add `metrics.json`
8. Practice `dvc exp run`

If you do these 8 steps yourself, your DVC understanding will become project-ready.

---

## Mini cheat sheet

```bash
dvc remote add -d myremote <path_or_url>
dvc push
dvc pull
dvc stage add -n <name> -d <dep> -o <out> <command>
dvc repro
dvc metrics show
dvc metrics diff
dvc plots show
dvc exp run
dvc exp show
```

---

## Final summary

Basic DVC teaches you how to version data.

Advanced DVC teaches you how to:

- share data remotely
- build reproducible ML pipelines
- track parameters
- compare metrics
- visualize plots
- manage experiments
- collaborate with teams in real MLOps projects
