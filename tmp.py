import json
path = 'test.json'
# load json data
with open(path, "r") as json_file:
    json_data = json.load(json_file)
    
print(json_data)