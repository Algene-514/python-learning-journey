# 作用域 指变量生效的范围，分为两种，分别是全局变量和局部变量
# 全局变量：函数外部定义的变量，在整个文件中均有效
a = 114514
def func1():
    print(a)
def func2():
    a =415411
    print(a)
def func3():
    print(a)
func1()
func2()
func3()
# 若函数内部需要变量时，会先从内部寻找，没有后再取函数外部的
# 局部变量：函数内部定义的变量，从函数定义开始到函数结束有效
def func4():
    num =111
    print(num)
# print(num)只能在函数内部使用，函数外部不可使用，

# 在函数内部修改全局变量的值，使用global关键字
# global 变量名
# 将局部变量升级为全局变量

def func5():
    global num,name    #多个变量的话直接用逗号隔开即可
    num =111
    name = 'Algene'
    print(num,name)

def func6():
    print(num,name)

func5()
func6()

# nonlcal：将变量声明为外层变量(是外层函数的局部变量，而不是全局变量)
# 对上一级进行修改
def outer():
    n = 514
    print(n)
    def inner():
        nonlocal n
        n = 1
        print(n)
    inner()
    print(n)
outer()



# 匿名函数（没有名字的函数，即lambda函数）
# 格式
# 函数名 = lambda 形参:返回值
# 调用
# 结果 = 函数名(实参)
def calculate(a,b):
    return a+b
print(calculate(1,2))
# 其等效匿名函数让如下,其只需要两行代码
cal = lambda a,b: a+b
print(cal(1,3))

# 匿名函数的参数格式:
# 1,无参数:
test1 = lambda : '114514'
print(test1())
# 2,一个或两个参数,上面已经演示
# 3,默认参数:
test2 = lambda name,age = 495 : (name,age)
print(test2('蕾米莉亚',))
# 4,关键字参数：
fund = lambda **kwargs:kwargs
print(fund(mane = '???',age = 99))








