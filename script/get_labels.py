import json

with open('script/label_map.json', 'r') as file:
    label_map = json.load(file)

label_list = list(label_map.keys())

with open('script/label_map_tfjs.json', 'w') as file:
    json.dump(label_list, file, indent=4)
