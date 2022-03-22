import json

def load_json(file_name):
    with open(file_name) as jsonfile:
        data = json.load(jsonfile)
    return data

def dump_json(json_data, file_name):
    with open(file_name, 'w') as jsonfile:
        json.dump(json_data, jsonfile, ensure_ascii=False)
