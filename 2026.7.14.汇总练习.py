# 一：

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
# contacts.get('古明地恋') 返回的是 None（一个特殊值），不是字符串 "None"。
# None 是判断 None 的标准写法）。
# 更安全的写法（因为如果用户销号对象不是 '古明地恋'，pop 会直接报错）：
if contacts.get('古明地恋') is None:
    print(f'{C}已成功销号，原号码为{D}')
else :
    print("操作失败，您被炒了！")

# 三：
name_list = ['古明地恋']
print('输入参加社团的人名')
for i in range(0,5):
    # i = str(input(f"输入第{i}号名字"))
    name = str(input(f"输入第{i}号名字"))
# ⚠️小瑕疵：这里的i覆盖了循环变量
#     name_list.append(i)
    name_list.append(name)
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
# 第五关：终极王者混合实战（10分钟）
# 目标：把列表、字典、集合、元组串起来用，解决真实问题。
# 题目：统计一段文本中每个字母出现的次数，并找出哪些字母出现了重复。
# 给定字符串：text = "hello world"（注：忽略空格）。
# 要求
# 使用 列表推导式 或 for 循环，提取出所有的字母（去除空格），放进列表 char_list 里。（提示：for char in text if char != " "）
# 使用 集合 找出所有不重复的字母。
# 创建一个 字典 count_dict，统计每个字母出现的次数（比如 'h': 1, 'e': 1, 'l': 3...）。
# 遍历字典，用 if 判断找出出现次数大于 1 的字母，放进一个 列表 repeat_list 里。
# 最后打印：重复出现的字母有：['l', 'o']（只是示例，看你的结果）。
## 1
text = 'hello world'
print(text)
char_list = [char for char in text if char != ' ']
print(char_list)
# 2
chr_set = set(char_list)
print(f"包含的字母有{chr_set}")
# 3
char_dict = {}
for char in char_list:
    if char not in char_dict:
        char_dict[char] = 1
    else:
        char_dict[char] += 1
print(char_dict)
# 4
repeat_list = []
for char_1 in char_dict:
    if char_dict[char_1] > 1:
        repeat_list.append(char_1)
# 5
print(repeat_list)


