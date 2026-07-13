# # 一，类型转换：
# # 1，int（）：使转换为一个整数。
# # 注意：其只能转换由纯数字组成的“字符串”含义小数点或+和-的符号都会报错
# a = int(input("输入数字"))
# print(a)
# b = 1.14514
# c = int(b)
# print(c)
# # 强行将“浮点型”转整形，则会去掉小数点后的数，只保留整数部分
#
# # 2.float()：转换为浮点型（小数）
# d = float(input("输入小数"))
# print(d)
# # 若直接输入整数的话会默认保留小数点后一位
# # 不支持转换数字与小数点以外的元素
#
# # 3，str():字符串转换,任何类型都可以被转换：
# e = str(input("输入任何你想输入的东西"))
# print(e,type(e))
# list = [1,2,3,4,5]
# print(str(list),type(str(list)))
#
# # 4,eval():执行一个表达式，再返回这个表达式的值/执行运算并返回运算的值
# print(eval(input("输入表达式")))
# 整形不能相加
# 可以实现list，dict，tuple，str之间的转换
str = "[1,2,3,4,5,6,7,8,9]"
li1 = eval(str)
print(type(li1))
# 就相当于去掉引号
# eval()很强大，但不安全，容易被恶意修改数据，不建议使用

# list 将可迭代对象转换成列表
# 支持转换为list的类型：str，tuple，dict，set
set1 = {1,2,3,4,5,6,7,8,9}
f = list(set1)
print(f)
# 字典转列表，会取键值为列表的元素
dic = {"1":"2","3":"4"}
print(list(dic))


