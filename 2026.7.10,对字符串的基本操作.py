# first_term = int(input("输入首项"))
# normal_difference = int(input("输入公差"))
# num_terms = int(input("输入项数"))
# total = 0
# for i in range(1,num_terms+1):
#     total += first_term ** i
# print(total)
import code
from base64 import encode

#一, 字符串编码：二进制与自然语言文字的一一对应关系
# 字符串编码转换：
# 编码：encode
# 将其他编码的字符串转换成Unicode编码
# 解码：decode
# 将Unicode编码转换成其他编码的字符串
# eg:字符串类型与bytes类型的转换
inf1 = "w(ﾟДﾟ)w"
print(inf1,type(inf1))
# type()用来查看当前信息类型
inf2 = inf1.encode()
print(type(inf2))
inf3 = inf2.decode()
print(type(inf3))
# .encode与.decode分别是编码与解码
# 其有三个参数(self,encoding(编码方式),errors)

inf4 = "komeijikoishi"
inf5 = inf4.encode("utf-8")
print(type(inf5))

#二, 字符串运算符：
# 1.“+”拼接字符串eg：
print(10 + 10)
print("10"+"10")
inf6 = 114
inf7 = 514
print(inf6 , inf7 , sep="")

# 2."*"重复输出eg：
print("114514114514!\n"*10)

# 成员运算符，检查字符串中是否包含了个子字符
# in 如果包含，返回Ture，若不包含，返回False
# not in 与之相反
# eg
inf8 = "114514"
print("1" in inf8, "2" in inf8)

#三,下标/索引：用来迅速地找到需要的数据
# Python中索引默认从0开始
# 格式：字符串名[下标值]
# 从左往右数，索引从0开始
# eg
inf9 = "hello world"
print(inf9[0])
# 这里索取到了第1个字符h
for i in inf9:
    print(i)
# 从右往左数，下标从-1开始

# 四,切片
# 语法：[起始:结束:步长]
# 作用：对操作对象截取其中一部分的操作
# 遵循包前不包后原则
# eg
Inf2 = "hello , the fuck world"
print(Inf2[0:3])
# 若end不写，则默认全部截取到
# eg
Inf3 = "甲乙丙丁"
print(Inf3[1:])
# 同理，从右往左是从-1开始
# 步长step表示选取间隔，不写步长则默认为1，其绝对值表示切取间隔，正负号表示切取方向
# 正数表示从左往右取值，负数表示从右往左

# find
# find检测某一个子字符串是否包含在字符串中,如果有就返回字符串下标,没有就返回-1
# 参数:sub,_start,_end(子字符串,开始位置下标,结束位置下标
# 若开始位置与结束位置下标省略,则表在整个字符串中查找
Inf4 = "114514"
print(Inf4.find ("11"))
# 输出的是第一个目标的索引值
# 同样遵循包前不包后原则:
print(Inf4.find("1",2,6))

# index()
# 检测某一个子字符串是否包含在字符串中,如果有就返回字符串下标,没有就报错
# 结束位置与开始位置可以省略,同样是在整个字符串中查找
# 与find的区别:没有找到的反应:一个返回-,一个报错
# 同样遵循包前不包后原则

# count()
# 返回某个子字符串在字符串中出现的次数,没有则返回0
# 同样的参数有开始位置与结束位置

#五,关于判断的:
# startwith()是否以某个子字符串开头,是的话返回Ture,不是的话返回False,可以在指定范围内查找
#eg:
st = "114514"
print(st.startswith("114"))

# endwith()是否以某个子字符串结尾,是的话返回Ture,不是的话返回False,可以在指定范围内查找,与startwith语法类似
# 是否大写/小写:isupper/islower:检测字符串中所有的字母是否都大写/小写,是的话就返回Ture

st_2 = "AAA"
print(st_2.isupper())

# 六,修改元素
# replace(self,old,new,count)
# (旧内容,新内容,替换次数)
# 替换次数可以省略,默认全部替换
# eg:
st_3 = ("吃了么梁非凡!")
print(st_3.replace("吃","喝"))
# split():指定分隔符来切字符串并以列表形式返回
print(st_3.split("了"))
# 如果字符串内不包含分割内容,则会作为一个整体而不进行切割
print(st_3.split("???"))
# 可以指定分割次数

# capitalize:使第一个字符大写,其他都小写
st_4 = "aBcDeFg"
print(st_4.capitalize())
# lower()使大写字母都转为小写
print(st_4.lower())
# upper()使大写字母都转为小写





















































































