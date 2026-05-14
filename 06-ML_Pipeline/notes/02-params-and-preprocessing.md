# Params And Preprocessing Notes

## Why `params.yaml` Is Used

Instead of hardcoding everything inside Python files, the project keeps important paths and settings inside `params.yaml`.

This is useful because:

- configuration stays in one place
- DVC can track parameter changes
- the code becomes easier to maintain

## Example Parameters

The notes in the module use two main sections:

```yaml
preprocess:
  input: data/raw/data.csv
  output: data/processed/data.csv

train:
  data: data/processed/data.csv
  model: models/model.pkl
  random_state: 42
  n_estimators: 100
  max_depth: 5
```

## What `preprocess.py` Does

The preprocessing step is intentionally simple.

Main job:

- read the raw CSV
- create the output folder if needed
- save the processed CSV

## Key Libraries Used In Preprocessing

- `pandas`
- `yaml`
- `os`

## Flow Inside `preprocess.py`

What I understood from the code:

1. Load preprocessing parameters from `params.yaml`
2. Read the input CSV with `pandas`
3. Create the output directory using `os.makedirs(..., exist_ok=True)`
4. Save the processed file to the configured output path

## Important Learning Point

In the video, preprocessing is very basic.

The aim is not advanced feature engineering here.

The aim is to show how a pipeline stage is created.

So even if the logic is simple, the stage is still important because it teaches:

- how to read config
- how to create outputs
- how to connect one stage to the next

## What I Can Add Later In Real Projects

Inside preprocessing, I can later include:

- missing value handling
- categorical encoding
- scaling
- feature engineering
- train/validation data preparation

## Personal Reminder

The transcript shows a few path adjustments while coding.

So I should double-check:

- whether I am saving to `processed` or `preprocessed`
- whether headers are preserved correctly
- whether train and evaluate scripts are reading the same version of data

