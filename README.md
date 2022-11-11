# Homework 2 ADL NTU

## Environment
```shell
# If you have conda, we recommend you to build a conda environment called "adl-hw2"
make
conda activate adl-hw2
pip install -r requirements.txt
# Otherwise
pip install -r requirements.in
```

## Optional setup
```shell
# use tensorboard for model tracking (plotting the result)
pip install tensorboard
```

## Quick prediction
```shell
# follow the specification on slides
bash scripts/run.sh "${1}" "${2}" "${3}"
```

---

The full running procedure is listed below for reproduction, and all the hyper-parameters are documented in the scripts.

## Convert data format (swag)
```python
# "${1}": path to the context file.
# "${2}": path to the testing file.
python utils/swag_formatter.py --context_file "${1}" --testing_file "${2}"
```

## Context Selection
### Training CS
```shell
bash ./scripts/run_cs.sh
```

### Testing CS
```shell
# will produce format_test.json in cwd
bash ./scripts/test_cs.sh
```

## Question Answering
### Training QA
```bash
bash ./scripts/run_qa.sh
```

### Testing QA
```bash
# will produce prediction from output/test_qa, here use the best rather than nbest.
# The final result is saved as format_test.json in cwd
bash ./scripts/test_qa.sh
```

## Submit to Kaggle
```bash
# "${3}": path to the output predictions.
# convert format from json to csv for kaggle
python utils/kaggle_submission.py --json_path "output/test_qa/predict_predictions.json" --pred_path "${3}"
```
