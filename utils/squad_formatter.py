import json

folder = "dataset/"
corpus = json.load(open(f"{folder}context.json"))
train = json.load(open(f"{folder}train.json"))
valid = json.load(open(f"{folder}valid.json"))
test = json.load(open(f"{folder}test.json"))

def squad_formatter():
    save_keys = ['id', 'question', 'context', 'answers']
    for idx, data in enumerate(['train', 'valid', 'test']):
        print(data)
        results = []
        for element in eval(data):
            pairs = {}
            for key in save_keys:
                if key == 'answers':
                    if idx != 2:
                        new_dict = {}
                        for k, v in element[key[:-1]].items():
                            if k != "text":
                                new_dict["answer_" + k] = [v]
                            else:
                                new_dict[k] = [v]
                        pairs[key] = new_dict
                elif key == 'context':
                    if idx != 2:
                        pairs[key] = corpus[element['relevant']]
                    else:
                        pairs[key] = corpus[element['paragraphs'][-1]]
                else:
                    pairs[key] = element[key]
            results.append(pairs)
        json_obj = json.dumps(results, indent=2, ensure_ascii=False)
        with open(f"{folder}squad_{data}.json", "w", encoding="utf-8") as file:
            file.write(json_obj)
    
if __name__ == '__main__':
    squad_formatter()