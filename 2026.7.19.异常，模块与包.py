# 想要在自己编写的程序中自定义异常
# 抛出异常：raise
# 步骤：
# 1，创建Exception('xxx')对象，xxx-异常提升信息
# 2，raise抛出这个异常对象
# def 异常():
#     raise Exception('草泥马使用了“异常”，效果拔群！')
#     print('哼哼哼啊啊啊啊啊啊啊')
# 异常()
# 执行了raise后的代码不会再被执行
import os
from time import time

import pytest


# 需求：限定用户输入密码长度，若长度不符合，则报错
# def secret():
#     User_secret = str(input('输入密码！！！'))
#     if 6 <=len(User_secret) <= 11 :
#         return User_secret
#     else:
#         raise Exception("密码长度不对啊啊啊啊啊啊啊！！！！")
# # 捕获异常，为了检测到异常时程序不终止
# try:
#     print(secret())
# except Exception as e:
#     print(e)

# 模块：在python中一个py文件就是一个模块里面定义的函数和变量，需要时可以导入模块，即执行一个py文件
# 分类：
# 1，内置模块
#如 random,time,os,logging，直接导入即可使用
# 2，第三方模块（第三方库）
# 需要进行下载
# 下载命令：在cmd窗口输入 pip install 模块名
# 3，自定义模块
# 自己在项目中定义的模块
# 命名要遵循标识符规定和变量的命名规范，不要与内置模块起冲突，否则不能运行、

# 模块的导入方式一:
# import 模块1,模块2,......(可以多个导入，也可以单独导入 )

# 调用方式：
# 模块名.功能名
# import pytest
# print(pytest.test)
# pytest.fun1()
# 模块的导入方式二:
# form 模块名 import 功能1,功能2
# from pytest1 import fun2
# fun2()
# 调用时若没有导入则会报错
# 导入函数只需要函数名，不需要小括号

# 模块的导入方式三
# from 模块名 import *
# 把模块中的全部内容全部导入
# 当导入模型中的单个功能但多个模块功能名相同时，默认使用后导入的模块的功能

import pytest
import pytest1
pytest.fun1()
pytest.fun2()
pytest1.fun1()
pytest1.fun2()

# as给模块起别名：
# 语法：
# improt 模块名 as 别名

import pytest as pt
pt.fun1()
pt.fun2()

# as给功能其别名
# 语法
# from 模块名 import 功能名 as 别名
from pytest1 import fun2 as  f2
f2()

# 内置全局变量：__name__（隔离“测试代码”和“功能代码”）
# 语法：
# 1，if __name__ == "__main__":
# 作用：用来控制py文件在不同的应用场景执行不同的逻辑
#文件当前程序执行，即自己执行自己：__name__ == "__main__"
# 文件被当作模块被其他文件导入：__name__ == 模块名
# 详细解释：
# 🎭 核心比喻：你是“主角”还是“嘉宾”？
# 场景 A（直接运行）：
# 你直接双击运行 my_tool.py，这时候你就是这场戏的主角。
# 导演（Python 解释器）会把这个文件的名字设为 "__main__"。
# 场景 B（被邀请）：你写了一个 math_utils.py，里面有个加法函数。
# 另一个文件 app.py 通过 import math_utils 把你请过去帮忙。
# 这时候你只是特邀嘉宾，你的名字不再是主角（__main__），而是你的真实文件名 "math_utils"。
# 🔑 __name__ 的“一键切换”功能
# __name__ 这个变量，就像一个自动识别的名牌，它会根据文件的处境自动改变值：
# 如果你直接运行这个文件（python 你的文件.py） → __name__ 的值 = "__main__"
# 如果别人把你导入进去（import 你的文件） → __name__ 的值 = "你的文件名"（不含.py）
# 🛠️ 这玩意到底有什么用？（经典用法）
# 最大的作用就是：隔离“测试代码”和“功能代码”。
#  def add(a, b):
#     return a + b
#  底下这行是干什么的？
# if __name__ == "__main__":
#     # 这里面的代码，只有我直接运行这个文件时才执行！
#     print(add(1, 2))  # 测试一下加法对不对
# 如test2中的计算函数，只有当选中test2时才会运行if __name__ == "__main__":的代码
import pytest2
pytest2.calculate(2,2,2)
print(f"当前文件名叫：{__name__}")

# 包：包就是项目结构中的文件夹/目录
# 与普通文件夹的区别：包是含有__init.py__的文件夹
# 作用：将有联系的模块放到同一个文件夹下，避免命名冲突问题，让结构更清晰
# 右键项目名->新建->python package(python软件包)
# 普通文件夹是directory

# import导入包时，首先执行__init__.py文件的代码

import pp1
# 不建议在init文件中写大量代码,尽量保证init文件的内容简单（init控制导包行为）

# from pp1 import test1
# print(test1.rst)
# test1.你好()

#__all__变量
# 本质上是一个列表，可以控制要引入的东西（如变量，函数，类等）
# 包的本质仍是模块，包可以包含包
'''
一下是init中的代码
print('114514')
__all__ = ['test1']
'''

# from pp1 import *
# 这里表示调用__all__中的文件，若__all__中没有需调用的文件，则会报错
# __all__ 这个变量，本质上就是一个“白名单”。
# 它专门用来控制 from 包/模块 import * 这种写法到底能导入哪些东西。
# 你可以把它理解为商店里的“橱窗展示清单”：
# 你店里（包/模块里）其实有几十种商品（函数、类、变量）。
# 但如果顾客问“把你们店所有东西都拿出来看看”（import *）
# 你只会把 __all__ 清单上列出的那几样明星产品摆在柜台上。
# 清单上没有的，不是没有，而是“不推荐你直接拿”。
# 若写了3个函数，只希望被导入两个，则__all__中只填两个

# __name__：决定“我是主角（直接运行）还是嘉宾（被导入）”（控制代码执行逻辑）。
# __all__：决定“当客人要所有东西时（import *），我给他看哪几样”（控制公开接口）。

