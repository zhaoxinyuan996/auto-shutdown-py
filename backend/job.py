import json

with open('../config.json') as f:
    config = json.loads(f.read())

while config:
    for i in config:
        ...
