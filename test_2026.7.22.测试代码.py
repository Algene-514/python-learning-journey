# 测试代码

# 1.测试函数
# def user_name(first,last):
#     full_name = f"{first} {last}"
#     return full_name.title()
# print(user_name('Al','Gene'))
# user_list = []
# print('现在开始录入姓名，按T键随时终止')
# while True:
#     first = input("输入你的姓:")
#     if first == 'T':
#         print("程序已终止")
#         break
#     last = input("输入你的名: ")
#     if last == 'T':
#         print("程序已终止")
#         break
#     user_list.append(user_name(first,last))
#     print(user_name(first,last))
# print(user_list)

# Python提供了一种自动测试函数输出的高效方式

# 1.1单元测试和测试用例
'''
Python标准库中的模块unittest提供了代码测试工具。
单元测试用于核实函数的某个方面没有问题：
测试用例是一组单元测试，它们一道核实函数在各种情形下的行为都符合要求
全覆盖的测试用例包含一整套单元测试，涵盖了各种可能的函数使用方法

通常只要对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖

'''

# 1.2可通过的测试
'''
编写测试用例:
1,先导入模块unittest和要测试的函数
2,再创建一个继承unittes.TestCase的类
3,并编写一系列方法对函数行为的不同方面进行测试
'''
# 必需继承unittest.TestCase类，这样Python才知道如何运行编写的测试！
# 示例:
# import unittest
# from user_name import user_name01
#
# class NameTestCase(unittest.TestCase):
#     '''测试user_name.py'''
#
#     def test_first(self):
#         '''能处理像是Algene的名字吗？'''
#         formatted_name = user_name01('Al','gene')
#         # 这里使用了unisttest中最有用的功能之一：断言方法。其核实得到的结果是否与期望的结果一致
#         self.assertEqual(formatted_name,"Al Gene") #即formatted_name 是否等于"Al Gene"
#
# if __name__ == '__main__':
#     unittest.main() # 用来运行测试用例。
# 首先导入了模块unittest和要测试的函数
# 创建一个名为NamesTestCase的类，用于包含一系列针对user_name01的单元测试
# 运行该文件时"test_2026.7.22.测试代码"，所有以test_打头的方法都将自动运行。
# 运行后出现了以下信息
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
'''
其中句点表示有一个测试通过了
接下来的一行指出Python运行了一个测试，消耗的时间不到0.001秒
'''

# 1.3未通过的测试
# 这里故意让断言处无法相等
import unittest
from user_name import user_name01

class NameTestCase(unittest.TestCase):
    '''测试user_name.py'''

    def test_first(self):
        '''能处理像是Algene的名字吗？'''
        formatted_name = user_name01('Al','gene')
        # 这里使用了unisttest中最有用的功能之一：断言方法。其核实得到的结果是否与期望的结果一致
        self.assertEqual(formatted_name,"AlGene") #即formatted_name 是否等于"Al Gene"

if __name__ == '__main__':
    unittest.main() # 用来运行测试用例。

# 出现了以下信息
# F
# ======================================================================
# FAIL: test_first (__main__.NameTestCase.test_first)
# 能处理像是Algene的名字吗？
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "C:\Users\12131\PyCharmMiscProject\基础学习\test_2026.7.22.测试代码.py", line 85, in test_first
#     self.assertEqual(formatted_name,"AlGene") #即formatted_name 是否等于"Al Gene"
#     ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
# AssertionError: 'Al Gene' != 'AlGene'
# - Al Gene
# ?   -
# + AlGene
#
#
# ----------------------------------------------------------------------
# Ran 1 test in 0.002s
#
# FAILED (failures=1)
'''
这包含了很多信息，因为测试未通过时，需要让你知道的事情有很多
字母E指出测试中有一个单元测试导致了错误
接下来指出了test_first发生了错误
之后出现一个标准的traceback指出问题
最后一条信息指出：单元测试未通过
'''











