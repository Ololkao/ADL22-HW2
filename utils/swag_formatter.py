import argparse
import json
import os

def swag_formatter(corpus, data):
    # folder = f"{os.getcwd()}/dataset/"
    # corpus = json.load(open(f"{folder}context.json"))
    # train = json.load(open(f"{folder}train.json"))
    # valid = json.load(open(f"{folder}valid.json"))
    # test = json.load(open(f"{folder}test.json"))
    save_keys = ['id', 'question', 'paragraphs', 'relevant']
    ending_names = [f"ending{i}" for i in range(4)]
    
    # for idx, data in enumerate(['train', 'valid', 'test']):
        # print(data)
        # results = []
        # for element in eval(data):
    corpus = json.load(open(corpus))
    data = json.load(open(data))
    results = []
    for element in data:
        pairs = {}
        for key in save_keys:
            if key == 'relevant':
                # if idx != 2:
                #     pairs['label'] = element['paragraphs'].index(element[key])
                # else:
                pairs['label'] = 0
            elif key == 'paragraphs':
                for i, num in enumerate(element[key]):
                    pairs[ending_names[i]] = corpus[num]
            elif key == 'question':
                pairs['sent1'] = element[key]
                pairs['sent2'] = ''
            else:
                pairs['video-id'] = element[key]
        results.append(pairs)
    json_obj = json.dumps(results, indent=2, ensure_ascii=False)
    # filename = f"{folder}swag_{data}.json" if data != 'test' else f"swag_{data}.json"
    filename = 'swag_test.json'
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json_obj)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="convert test datat to swag format")
    parser.add_argument(
        "--context_file",
        type=str,
        required=True,
        help="path to the context file."
    )
    parser.add_argument(
        "--testing_file",
        type=str,
        required=True,
        help="path to the testing file."
    )
    args = parser.parse_args()

    swag_formatter(args.context_file, args.testing_file)
