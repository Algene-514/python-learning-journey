# 一：
from operator import ifloordiv

queue = []
queue.append('灵梦')
queue.append('魔理沙')
queue.append('妖梦')
print(queue)
queue.insert(0,"uuz")
print(queue)
queue.pop(2)
print(queue)

# 二：
contacts = {'古明地恋':114514}
A = str(input('想要添加的联系人'))
B = int(input('其电话号码'))
contacts[A] = B
print(contacts)
print(contacts.get('？？？'))
print("古明地恋要销号，请为该客户提供销号服务")
C = str(input("销号对象"))
D = contacts.pop(C)
if str(contacts.get('古明地恋')) == "None":
    print(f'{C}已成功销号，原号码为{D}')
else :
    print("操作失败，您被炒了！")

# 三：
name_list = ['古明地恋']
print('输入参加社团的人名')
for i in range(0,5):
    i = str(input(f"输入第{i}号名字"))
    name_list.append(i)
print(name_list)

print("似乎有重复的？")
name_set = set(name_list)
print(name_set)

name_set.add("古明地恋")
print(name_set)
if "古明地恋" in name_set:
    print("我们需要更多的恋恋！！！")

# 四，
name_tuple = tuple(name_list)
print(name_tuple)
print(name_tuple[0])

X_tuple = (1,2,3,4,[5,6,7,8,9])
X_tuple[4].append(10)
print(X_tuple)

# 四点一:
list3 = [i for i in range(1,11)]
list4 = [i for i in range(1,11) if i%2==0]
print(list3)
print(list4)
score = [100,110.120,130,140,150]
new_score = [scores + 5 for scores in score ]
print(new_score)


# 五！！！：
text = 'helloworld'
print(text)
char_list = [char for char in text]
print(char_list)
chr_tuple = set(char_list)
print(f"包含的字母有{chr_tuple}")

