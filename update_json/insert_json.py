import json

file = 'data.json'

# with open('data.json', 'r+') as f:
#     data = json.load(f)
#     print("data")
#     data['id'] = 134 # <--- add `id` value.
#     f.seek(0)        # <--- should reset file position to the beginning.
#     json.dump(data, f, indent=4)
#     f.truncate()     # remove remaining part

with open(file) as f:
    json_decoded = json.load(f)

# print(json_decoded)

batter = json_decoded['batters']['batter']

# print(json.dumps(batter, indent = 4))

batter.append({"id": "1005", "type": "Indian Food"})

print(json.dumps(json_decoded, indent = 4))

with open(file, 'w') as f:
    json.dump(json_decoded, f, indent=4)