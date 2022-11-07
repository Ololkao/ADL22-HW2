import argparse
import pandas as pd

def main(qa_prediction, output_path):
    df_pred = pd.read_json(qa_prediction, typ="series").reset_index()
    df_pred.columns = ['id', 'answer']
    df_pred.to_csv(output_path, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Predict testing data as csv file")
    parser.add_argument(
        "--json_path",
        type=str,
        default=None,
        help="path to the json file from QA"
    )
    parser.add_argument(
        "--pred_path",
        type=str,
        default=None,
        help="path to the output predictions"
    )
    args = parser.parse_args()

    main(args.json_path, args.pred_path)