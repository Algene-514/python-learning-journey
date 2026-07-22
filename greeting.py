import json
filename = 'usersnames.json'
with open(filename) as f:
    name = json.load(f)
print(f"哦！是你，{name}!")