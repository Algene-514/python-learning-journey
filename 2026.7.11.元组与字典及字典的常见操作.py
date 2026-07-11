# 一.元组，tulpe
# 基本格式：元组名 = (元素1，元素2，元素3，......)
# 所有元素包含在小括号内，元素与元素直接用逗号隔开，不同元素可以是不同的数据类型
A = (1,2,3,"1",[1,23,4,5,],6,1)
# print(type(A))
# B = (1,)
# C = (1)
# print(type(B),type(C))
# 只有一个元素时，结尾带上逗号才能算是tulpe，否则返回该元素数据类型
# 元组（tulpe）只支持查询操作，不支持增删改操作！！！
# print(A[3])
# 元组也有下标，从0开始
# 支持查询，如count()，index()，len()。与列表的用法相同
# len()查看“长度”，即数据个数
# print(A.count(1)) # 对1的数量计数
# print(A.index(2)) #查询2的位置
# print(len(A)) # 查询A的“长度”
# 元组也可以使用切片操作
#元组的应用场景：

# 1.函数的参数与返回值

# 2.格式化输出后的（）本质上一个元组
# name = input("your name: ")
# age = int(input("your age: "))
# A = (name,age)
# print("your name is %s, your age is %d"%A)
# 保护数据安全，使数据不可修改

# # 二，字典
# # 字典的基本格式
# # 字典名 = {键1:值1,键2:值2,键3:值3,......}
# # 注意逗号与冒号的使用
# # '键值对'形式保存，键与值间用”:“隔开，键值对间用”，“隔开
# dic = {'name':"Algene",'age':17,'name':"Algene514"}
# print(type(dic))
# print(dic)
# # 字典中的键具有唯一性，而值可以重复
# # 但如果重复，不会报错，键名前面的值会被后面的值覆盖
# print(dic)
# # 〇，字典的操作：增删改查
#
# # 1.查：字典中无下标，查找元素需要根据键名
# # （1）变量名[键名]
# # 键名不存在时报错
# print(dic['age'])
# # （2）变量名.get(键名)
# # 键名不存在时，返回none，若不想返回none，可自己设置
# print(dic.get('???',"被uuz吃掉了QwQ"))

# 2,修：修改元素
dic = {'name':"Algene",'age':17,'name':"Algene514"}
# 通过键名修改
dic["name"] = "Algene514"
print(dic["name"])

# 3,若键名不存在，则为新增元素
dic["???"] = 114514
print(dic)

# 4,删除元素
# （1）del：可以删除字典，也可以删除字典内的元素，若无指定元素，则报错
del dic["???"]
print(dic)
del dic
dic = {'你是':114514}
print(dic)

# (2)clear():清空字典的所有键值对，但是保留字典本身
dic.clear()
print(dic)
dic["???"] = 114514
print(dic)

# (3)pop()删除指定键值对，若不存在，则报错
# 必需有指定键名，不然则报
dic.pop("???")
print(dic)
dic["???"] = 111
dic.popitem()
print(dic)
# popitem默认删除最后一个键值对