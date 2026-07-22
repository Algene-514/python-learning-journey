import json
name = str(input("Enter your name: "))
filename = "usersnames.json"
with open(filename,'w') as f:
    users = json.dump(name,f)
print(f'你的名字是{name}!')