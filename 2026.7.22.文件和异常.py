# # 1从文件中读取数据
# # 读取文件可以编写这样一个程序：
# # 读取一个文本文件的内容，重新设置这些数据的格式并将其写入文件
#
# # 1.1读取整个文件
# # 先创建一个文本文件(.txt)
# # 下面的程序打开并读取文件，并将其内容显示在屏幕上
# with open('text_py.txt') as file_obj:
#     content = file_obj.read()
# print(content,1)
# # 对于该程序的解释：
# # 函数open()接受一个参数：要打开的文件名称。之后Python在当前执行文件所在的目录中查找指定文件
# # 之后将该对象赋值给 file_obj以供以后使用
# # 关键字with在不再需要访问文件后将其关闭
# # 然而也可以使用open()和close()来打开和关闭文件，但如果这样做，若有bug导致close无法执行，那么文件将不会关闭
# # 未妥善关闭文件可能导致数据丢失或受损。总之，使用close的风险较大
# # 相较于原文件，输出的唯一不同是末尾多了个空行，因为read()达到文件末尾时返回一个空字符串，该空字符串显示出来就是一个空行
# # 想要消除它，我们可以在函数调用print()中使用rstrip(),其可以用来删除字符串末尾的空白部分
# print(content.rstrip(),1)
#
# # 1.2文件路径
# # 根据组织文件的方式，有时需要在其他目录中打开文件，但是Python只能在本文件夹内查找
# # 要解决这个问题，需要让Python打开不与程序文件位于同一个目录中的文件，需要提供文件路径，让它自己去查找
# with open('test_content/text.txt') as obj1:
#     content1 = obj1.read()
#     print(content1)
# # 即使用相对文件路径来打开，指定具体文件夹和文件
# # 也可以用绝对文件路径，即文件在计算机上的具体位置，在相对路径行不通时，可以用绝对路径
# # 绝对路径较长，因此将其给一个变量赋值，在将变量给open()会比较方便
# file_path ="C:/Users/12131/PyCharmMiscProject/基础学习/test_content/text.txt"
# with open(file_path) as obj2:
#     content2 = obj2.read()
# print(content2)
# # window系统中用的是反斜杠\，但是python中用的是斜杠/
#
# # 1.3逐行读取
# # 要以每次一行的方式检查文件，可以对对象使用for循环:
# with open('text_py.txt') as obj3:
#     for line in obj3:
#         print(line.rstrip())
import os
from shlex import split

# 1.4创建一个包含文件名的列表
# 使用关键字with时，open()返回的文件对象只在with代码块内可用。
# 如果要在with代码块外访问文件的内容，可以在with代码块内将文件的各行储存在一个列表中，并在with外使用该列表
#
# with open('text_py.txt') as obj4:
#     lines = obj4.readlines()
# for line in lines:
#     print(line.rstrip())
# #     readlines()从文件中读取每一行，并将其储存在一个列表中
# #     接下来列表被赋值给lines
#
# # 1.5使用文件的内容
# pi_sting = ""
# for line in lines:
#     pi_sting += line.rstrip()
# print(len(pi_sting))
# # 可见其中内容是以字符串形式被读取的，若使用数字，则要用int()转换
#
# # # 1.1.6圆周率前1000000位包含你的生日吗？
# birth = input("输入你的生日")
# if birth in pi_sting:
#     print('YES')
# else:
#     print('NO')

# # 2.写入文件
# # 2.1写入空文件
# # 将文本写入文件，在调用open()时需要提供另一个实参，告诉Python你要写入打开的文件
# filename = 'test2.txt'
# with open(filename,'w') as obj0:
#     obj0.write('nice to meet you\n')
# # open()的第二个参数"w"告诉python要以写入模式打开这个文件
# # 打开文件时可以指定读取模式“r”,写入模式"w",附加模式'a'或读写模式'r+'
# # 若省略该参数，默认以只读模式打开
# for add in range(10):
#     with open(filename,'a') as obj1:
#         obj1.write('nice to meet you!\n')
# # 函数write不会在末尾加换行符，需要手动添加

# 3,异常
# python使用称为'异常'的特殊对象来管理程序执行1期间发生的错误
# 若编写了处理异常的代码，程序将继续执行
#
# 3.1 处理ZeroDivisionError异常
# print(5/0)
# 如5/0，是ZeroDivisionError异常对象，若执行则会显示：
# Traceback (most recent call last):
#   File "C:\Users\12131\PyCharmMiscProject\基础学习\2026.7.22.文件和异常及测试代码.py", line 84, in <module>
#     print(5/0)
#           ~^~
# ZeroDivisionError: division by zero

# 3.2使用try-except代码块：
try:
    print(5/0)
except ZeroDivisionError:
    print('零不能成为除数')

'''
这里Python找到了处理异常的except代码并运行该代码
这样用户看到的是一条友好的错误消息而不是traceback
这样就不会使程序崩溃终止了，代码可以继续进行下去！！！
'''

# 3.3通过使用异常避免程序崩溃
def caculator(a,b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        print('除数不能为零')
        return ''
    finally:
        print('已完成程序')

print(caculator(1,0))
# 程序崩溃可不好，不懂技术的用户会被搞迷糊，怀有恶意的用户还会通过traceback来获悉你不想让他知道的信息
# 有时候，训练有素的攻击者可以根据这些信息判断出可以对你的代码发起怎样的攻击

# 3.4 else代码块
# 依赖try代码块成功执行的代码都应放到else代码块中：
def caculator1(a,b):
    try:
        answer = a / b
    except ZeroDivisionError:
        print('除数不能为零')
        return ''
    else:
        print(answer)
    finally:
        print('已完成程序')

# try-except-else代码块的工作原理如下：
# Python尝试try代码块中的代码(只有可能引发异常的代码才需要放在try语句中)
# 有一些仅在try代码块成功时才需要运行的代码应该放在else代码块中。
# except告诉Python，如果尝试运行try代码块中的代码发生了指定的异常该怎么办

# 3.5处理FileNotFounndError异常
# 即查找文件失败
file9 = '114514'
try:
    with open(file9,) as obj9:
        cont = obj9.read()
except FileNotFoundError:
    print('未找到指定文件')

# 3.6分析文本
# 下面提取童话《爱丽丝的不可思议之国》文本，并尝试计算其包含多少个词
# 我们用split()，它能根据一个字符串创建一个单词列表
# 原理是以空格为分隔符将字符串分割为多个部分并将所有部分储存到列表中
# 这里关于encoding
# 计算机用二进制（0和1）存储一切。
# 文本需要被编码成二进制，并被解码回文本。
# 编码标准（如 ASCII、GBK、UTF-8）。
# UTF-8 是目前全球通用的标准（万国码）
# 因此这里需要添加一个encoding解码
def caculator0(book):
    """计算一个文本中有多少个词"""
    try:
         with open(book,encoding='utf-8') as ob:
             dairy = ob.read()
    except FileNotFoundError:
        print("文件不存在！")
    else:
        dair = dairy.split()
        length = len(dair)
        print(length)
# 3.7使用多个文件
list0 = ["拂晓前线.txt","dairies.txt","hao"]
for book in list0:
    caculator0(book)

# 3.8静默失败：
# 若想让出现错误时想什么都没发生一样继续进行
# 使用pass语句，这明确地让Python什么都不要做
# 示例：
def caculator9(book):
    """计算一个文本中有多少个词"""
    try:
         with open(book,encoding='utf-8') as ob:
             dairy = ob.read()
    except FileNotFoundError:
        pass
    else:
        dair = dairy.split()
        length = len(dair)
        print(length)
list0 = ["拂晓前线.txt","dairies.txt","hao"]
for book in list0:
    caculator9(book)

# 4,存储数据
# 一种简单的数据储存方式：使用模块json
# 模块json可以将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。
# 还可以用其在Python程序间分享数据。
# 更重要的是JSON数据格式并非Python专用。
# 注意：JSON（JavaScript Object Notation）格式最初是为JavaScript开发的，但随后成为了一种常见格式

# 4.1使用json.dump() 和json.load()
import json # 先导入json模块
numbers =[2,3,4,5,6]
yyy = {"1":1,"2":2,"3":3,"4":4,"5":5}
file01 = 'numbers.json' # 新建文件,扩展名json指出数据为JSON格式
with open(file01,'w') as f: #打开文件
    json.dump(numbers,f) # 导入数据
    json.dump(yyy,f)
# json.dump()接受两个实参，分别是储存对象和可用于储存数据的对象
# 随后python会建立一个相应的json文件储存数据,这是一种在程序之间共享数据的简单方式

# 4.2
# 保护和读取用户生成的数据
# import json
# filename = "usersname.json"
# # 如果已经注册了用户名，就加载它
# # 若未注册，则注册并储存用户名
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     print("用户未注册，请先注册")
#     username = str(input("Enter your name: "))
#     with open(filename,'w') as f:
#         json.dump(username,f)
# else:
#     print(f"welcome back {username} ")

# 4.3重构
# 代码能够正确运行，但通过将其划分未一系列完成具体工作的函数，还需要改进。这样的过程成为"重构"
# 重构让代码更清晰，容易理解
# 如重构刚刚的
# remamber_me.py文件

# import json
#
# def get_stored_username():
#     filename1 = "usersname.json"
#     '''收集用户信息并问候用户'''
#     try:
#         with open(filename1) as f1:
#             username = json.load(f1)
#     except FileNotFoundError:
#         return None
#     else:
#         return username
# def get_new_username():
#     print("用户未注册，请先注册")
#     username = str(input("Enter your name: "))
#     filename = "usersname.json"
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f'我记住你了 {username} ！')
# def great_user():
#     username = get_stored_username()
#     if username:
#         print(f'welcome {username}')
#     else:
#         get_new_username()
#
# great_user()
# 这样，每一个函数都执行一个清晰的任务
# 使代码清晰而易于维护和拓展的话，这种划分是必不可少的！

# 拓展：验证用户
# 若用户是先前的用户，则欢迎；若并非原用户，则重新注册
import json

def get_stored_username():
    filename1 = "usersname.json"
    '''收集用户信息并问候用户'''
    try:
        with open(filename1) as f1:
            username = json.load(f1)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    print("用户未注册，请先注册")
    username = str(input("Enter your name: "))
    filename = "usersname.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f'我记住你了 {username} ！')

def great_user():
    username = get_stored_username()
    check = str(input("Enter your name: "))
    if check == username:
        print(f'welcome {username}')
    else:
        get_new_username()

great_user()






