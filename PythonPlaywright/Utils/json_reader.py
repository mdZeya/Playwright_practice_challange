import json

def read_json(testdata):
    with open(testdata) as file:
        return json.load(file)