import json
filename = "usersname.json"
# 如果已经注册了用户名，就加载它
# 若未注册，则注册并储存用户名
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    print("用户未注册，请先注册")
    username = str(input("Enter your name: "))
    with open(filename,'w') as f:
        json.dump(username,f)
else:
    print(f"welcome back {username} ")

# 4.3重构
# 代码能够正确运行，但通过将其划分未一系列完成具体工作的函数，还需要改进。这样的过程成为"重构"
# 重构让代码更清晰，容易理解
