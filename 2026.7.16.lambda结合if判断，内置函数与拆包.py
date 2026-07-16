from ast import compare
from selectors import SelectSelector

print('helle python interpreter!')
# lambda的应用：与if三目运算结合
# 复习：三目运算
number_1 = 10
number_2 = 20
print('number_1 > number_2') if number_1 > number_2 else print('number_1 < number_2')
# 结合后的效果：使代码量减少，现在只需要两行代码
com = lambda number_1, number_2 : 'number1>number2' if number_1 > number_2 else 'number_1 < number_2'
com(number_1, number_2)
# 缺点：lambda只能实现简单逻辑，若逻辑复杂则不使用kambda。会对后期维护代码增加困难

# 内置函数
# 先导入模块
import builtins
print(dir(builtins))
# 大写字母开头一般是内置常量名，小写字母开头一般是内置函数名
# abs()返回绝对值
print(abs(-10))
# sum()求和，其中必须是可迭代对象，不能放整形
# 注意，虽然字符串和字典是可迭代对象，但字符串不能被求和。基本上就只有列表，元组和集合可以被求和
list_1 = [1,2,3,4,5,6,7]
print(sum(list_1))
# 运算时只要有一个浮点数，运算结果返回的就是浮点数

# min()/max()求最小值/最大值
a = min(1,2,3,4,5,6,7)
b = max(1,2,3,4,5,6,7)
print(a,b)
c = max(1,-2,3,-4,5,6,-7,key=abs)
print(c)

# zip()即zipper拉链函数将可迭代对象作为参数，将对象中对应的元素打包成一个个元组
list_3 = [1,2,3,4,5,6,7,8,9]
list_4 = ['大妖精','露米娅','琪露诺','米斯蒂娅']
zip_1 = zip(list_3,list_4)
print(zip_1)
for i in zip_1:
    print(i)
# 以元组形式输出，若长度不一致，则以最短长度输出

# 也可以转换成列表打印
print(list(zip(list_3,list_4)))
# 取出结果的两种方法：1，for循环，2，list形式输出

#map()可以对可迭代对象中的每一个元素进行映射，分别去执行，也叫映射函数
# mao()映射函数
# 格式
# map(已被定义的函数名,可迭代对象)   注意只写函数名，不写小括号
List1 = [1,2,3,4,5,6,7,8,9]
def f(x):
    return x*x
print(list(map(f,list_3)))

# reduce()先把对象中的两个元素取值，计算出一个值后保存者，然后与第三个元素进行计算
# reduce的使用需要先导包
# reduce(function,sequence)
# 函数必需是接受两个参数的函数
from functools import reduce
List2 = [1,2,3,4,5,6,7,8,9]
print(reduce)
def funcion0(a,b):
    return a + b
print(reduce(funcion0,List2))
# 等效为对列表List2求和

# 拆包：对于函数中的多个返回数据，去掉元组，列表，或者字典而直接获取其中元素的过程
tuple_1 = (1,2,3,4,5,6,7,8,9)
a,b,c,d,e,f,g,h,i = tuple_1
print(a,b,c,d,e,f,g,h,i)
# 要求元组内的数据格式与被定义的变量数量相同，不然会报错，值错误
# 一般在获取元组值的时候使用
# 方法二：
j,*z = (1,2,3,4)
print(z)
# z成为了列表！
# 还可以继续取z的值！！！
a1,*b1= z
print(a1,b1)
# 一般在函数调用时使用
# 复习args：
# *args用于传递一个不定数量的非键值对参数列表给函数。
# 它将所有传递的参数打包成一个元组。在定义函数时，如果你不确定会传递多少个参数，可以使用*args


