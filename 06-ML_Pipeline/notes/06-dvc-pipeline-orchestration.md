# DVC Pipeline Orchestration Notes

## Main Idea

At first, `preprocess.py`, `train.py`, and `evaluate.py` are just separate scripts.

The final step of this module is to connect them into one proper pipeline using DVC stages.

## Why DVC Stages Matter

DVC stages help define:

- what command should run
- what inputs a stage depends on
- what parameters affect that stage
- what outputs the stage creates

This makes the workflow reproducible.

## DVC Initialization

First step:

```bash
dvc init
```

## Track Raw Data With DVC

The raw dataset is added to DVC:

```bash
dvc add data/raw/data.csv
```

After this, Git should track:

- `data/raw/data.csv.dvc`
- `data/raw/.gitignore`

## Stage 1: Preprocess

The preprocess stage concept is:

- dependencies: source code + raw data
- parameters: preprocess input/output
- output: processed data

Command idea:

```bash
dvc stage add -n preprocess \
    -p preprocess.input,preprocess.output \
    -d src/preprocess.py -d data/raw/data.csv \
    -o data/processed/data.csv \
    python src/preprocess.py
```

## Stage 2: Train

The train stage concept is:

- dependencies: training code + processed data
- parameters: train-related config
- output: trained model

Command idea:

```bash
dvc stage add -n train \
    -p train.data,train.model,train.random_state,train.n_estimators,train.max_depth \
    -d src/train.py -d data/processed/data.csv \
    -o models/model.pkl \
    python src/train.py
```

## Stage 3: Evaluate

The evaluate stage concept is:

- dependencies: evaluation code + trained model + processed data
- output: evaluation execution

Command idea:

```bash
dvc stage add -n evaluate \
    -d src/evaluate.py -d models/model.pkl -d data/processed/data.csv \
    python src/evaluate.py
```

## Run The Full Pipeline

To execute the whole pipeline:

```bash
dvc repro
```

This runs the stages in dependency order.

So the flow becomes:

`preprocess -> train -> evaluate`

## Why This Is Powerful

What I liked most here:

- the pipeline becomes structured
- outputs are tracked properly
- if an input changes, DVC knows which stages need rerun
- the full workflow is reproducible

## DagsHub Remote Integration

The final setup also pushes DVC-managed files to the DagsHub remote.

Typical flow:

```bash
dvc remote add origin <remote-url>
dvc remote modify origin endpointurl <endpoint-url>
dvc push -r origin
git push origin main
```

## Final Understanding

This is the complete MLOps picture from this module:

- Git tracks code and metadata
- DVC tracks data, model files, and pipeline stages
- MLflow tracks experiments
- DagsHub acts as the remote collaboration platform

