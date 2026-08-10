# Params And Preprocessing Notes

## Why `params.yaml` Is Used

Instead of hardcoding everything inside Python files, the project keeps important paths and settings inside `params.yaml`.

This is useful because:

- configuration stays in one place
- DVC can track parameter changes
- the code becomes easier to maintain

<br/>

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

<br>

## What `preprocess.py` Does

The preprocessing step is intentionally simple.

Main job:

- read the raw CSV
- create the output folder if needed
- save the processed CSV

<br/>

## Key Libraries Used In Preprocessing

- `pandas`
- `yaml`
- `os`

<br/>

## Flow Inside `preprocess.py`


1. Load preprocessing parameters from `params.yaml`
2. Read the input CSV with `pandas`
3. Create the output directory using `os.makedirs(..., exist_ok=True)`
4. Save the processed file to the configured output path



### Note:

Inside preprocessing, you can later include:

- missing value handling
- categorical encoding
- scaling
- feature engineering
- train/validation data preparation


