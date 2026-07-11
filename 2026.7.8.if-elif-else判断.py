# if基本格式
# if 满足的要求:
#     满足要求做的事情
age = int(input("请输入年龄"))
if age < 100 :
    print("抱歉，你未达到飞升资格")
else :
    print("NB")
# input里面默认的是字符串类型，所以要用int转换类型为数字
inf1 = int(input("inf1"))
inf2 = int(input("inf2"))
if inf1 > inf2 :
   print("说的道理！")
if inf1 == 114 and inf2 == 514 :
    print(inf1 , inf2)

if inf1 > inf2 or inf1 < inf2 :
    print("我喜欢你（1")

print(not 114>514)
# 三目运算示例
print("啊对的对的") if inf1 > inf2 else print("啊错的错的")
# 等效为：
if inf1 > inf2 :
    print("啊对的对的")
else:
    print("啊错的错的")
print("\n\n\n")
inf3 = int(input("???"))
inf4 = int(input("!!!"))
if inf3 > inf4 :
    print(54188,"!!!")
elif inf3 < inf4 :
    print(14524,"???")
else :
    print("!?强强?!")
score = int(input("输入分数"))
if score >= 95:
    print("!?强强?!")
elif score >= 90:
    print("牛\t逼")
elif score >= 80:
    print("啊对的对的对的")
elif score >= 70:
    print("真正的勇士，敢于直面淋漓的鲜血，敢于面临惨怛的现实，这是怎么样的一个幸福者与不幸者！")
else:
    print("!?弱弱?!")
print("\n")
girl1 = "古明地恋"
girl2 = "古明地觉"
girl3 = "芙兰朵露"
girl4 = "蕾米莉亚"
girl = input("输入你的“老婆”")
if girl == "滴蜡熊":
    print("awmc")
elif girl == girl1 or girl == girl2 or girl == girl3:
    print("这是好的！！！")
else:
    print("威严！！！")
inf1 = input("你的xp等级")
if inf1 == "A":
    print("你是深渊者等级")
    inf2 = int(input("你的xp系数"))
    if inf2 > 700:
        print("你TM开了吧")
    elif 600 < inf2 < 700:
        print("啊对的对的")
elif inf1 == "B":
    print("你是觉醒者等级")
    inf3 = int(input("你的xp系数"))
    if inf3 > 500:
        print("啊对的对的")
    elif 400 < inf3 < 500:
        print("加油罢！")
elif inf1 == "C":
    print("你是正常等级")

