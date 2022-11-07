import json
import os

def swag_formatter():
    folder = f"{os.getcwd()}/dataset/"
    corpus = json.load(open(f"{folder}context.json"))
    train = json.load(open(f"{folder}train.json"))
    valid = json.load(open(f"{folder}valid.json"))
    test = json.load(open(f"{folder}test.json"))
    save_keys = ['id', 'question', 'paragraphs', 'relevant']
    ending_names = [f"ending{i}" for i in range(4)]
    
    for idx, data in enumerate(['train', 'valid', 'test']):
        print(data)
        results = []
        for element in eval(data):
            pairs = {}
            for key in save_keys:
                if key == 'relevant':
                    if idx != 2:
                        pairs['label'] = element['paragraphs'].index(element[key])
                    else:
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
        filename = f"{folder}swag_{data}.json" if data != 'test' else f"swag_{data}.json"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(json_obj)

if __name__ == '__main__':
    swag_formatter()
