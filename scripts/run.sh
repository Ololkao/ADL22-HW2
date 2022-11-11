# "${1}": path to the context file.
# "${2}": path to the testing file.
# "${3}": path to the output predictions.

# will produce swag_test.json in cwd
python utils/swag_formatter.py --context_file "${1}" --testing_file "${2}"

# will produce format_test.json in cwd
bash ./scripts/test_cs.sh

# will produce prediction from output/test_qa, here use the best rather than nbest.
# The final result is saved as format_test.json in cwd
bash ./scripts/test_qa.sh

# convert format from json to csv for kaggle
python utils/kaggle_submission.py --json_path "output/test_qa/predict_predictions.json" --pred_path "${3}"
