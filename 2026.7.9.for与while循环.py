# # while循环基本语法：
# #定义初始1变量
# # while 条件:
# #     循环体
# #     改变变量
#
#
# num = int(input("输出初始值")) # 先定义一个变量确定初始“次数”
# while num <=10: # 翻译：当num小于等于10时，执行下方指令
#     print("哦哦哦哦哦哦吼吼吼吼吼吼吼吼吼哼哼哼啊啊啊啊！！!")
#     num += 1 # 即num = num + 1
#
#
# # 死循环：
# # while True : # 表示条件一直为真，所以就一直在运行
# #     print(num)
# # 同理，若为False，条件就一直为假，不会执行
# # while False:
# #     print("???")
# # while后只要不是0或者False都会进入死循环，条件一直成立(布尔值：Ture：整数1，False：整数0)
#
# """实战！！！计算等差数列的和！！！"""
#
# # print("这是一个等差数列求和工具，你现需要输入首项，公差和项数来求和")
# # basic = 1 #这个初始值用来记录循环次数
# # a1 = int(input("输入首项")) #接下来两步用来定义等差数列
# # d1 = int(input("输入公差"))
# # n1 = int(input("输入项数"))
# # S1 = 0 # 定义输出的初始值，肯定是0的啦！！！
# # while basic <= n1 :
# #     S1 = S1 + a1
# #     a1 = a1 + d1
# #     basic += 1
# # print("\n求和为",S1)
#
# """
# 成功！！！，接下来类比一下等比数列求和
# """
#
# print("这次是等比数列求和")
# basic = 1
# #等比数列求和实战！！！
# b1 = int(input("输入首项"))
# q1 = int(input("输入公比"))
# n2 = int(input("输入项数"))
# S2 = 0
# while basic <= n2 :
#     S2 = S2 + b1
#     b1 = b1 * q1
#     basic += 1
# print("\n求和为",S2)
#
# """
# 成功！！！
# """
#
# """
# 将变量名可以更"专业"一点，用有意义的英文单词
# 尝试一些更"程序员思维"的改进,优化如下
# """
#
# print("这是一个等差数列求和工具，你现需要输入首项，公差和项数来求和")
# counter = 1 # 从第1项开始累加，直到达到指定的项数
# first_term = int(input("输入首项")) #接下来定义等差数列
# common_difference = int(input("输入公差"))
# num_terms = int(input("输入项数"))
# total_sum = 0 # 定义输出的初始值，肯定是0的啦！！！
# if num_terms <= 0:# 这里用来讨论”边际情况“当次数<=0时，肯定是无意义的呀！！！
#     print("项数必须是正整数，请重新运行程序")
# else:
#     while counter <= num_terms :
#         total_sum += first_term
#         first_term += common_difference
#         counter += 1
#     print("\n求和为",total_sum)
#
# #  while循环嵌套：
# # 循环里面夹带循环
# # while条件1
# # 	条件1满足时段做的事情1
# # 	条件1满足时段做的事情2
# # 	.......
# # 	while条件2
# # 		条件2满足时段做的事情1
# # 		条件2满足时段做的事情2
# # 		......
# """
# 注意：缩进决定层级，每执行一次外循环，内循环在条件满足时就一直循环
# """
#
#
#
# awsl = 1
# while awsl < 10:
#     awsl = awsl + 1
#     print("外循环",awsl)
#     while awsl < 5:
#         awsl = awsl + 1
#         print("内循环",awsl)
#
#
#
# # for循环（迭代循环）多用于依次取出对象中的元素，与while相比更加“自动”且不会死循环
# # 基本格式：
# # for 临时变量 in 可迭代对象：（可迭代对象就是要去遍历取值的整体）(临时变量可以任取，常规是写成i)
# #   循环体
# # eg：
# # ob1 ="1451454188!!!"
# # for i in ob1:
# #     print(i)
# # 看，这里ob1中的字符串被一个个拆开了！！！
# # 字符串是可迭代对象，但是整型和浮点型字不是可迭代对象！！！搞上去会报错！！！
# # range()可以用来充当计数器的功能，对for循环进行修饰。其中有3个参数，与print类比
# # 有start,stop,step(步子)
# for numx in range(1,10):
#     print(numx)
# # 这里输出的只有123456789，因为其遵循“包前不包后”原则，类似数学中左闭右开区间[1,10)
# # 若只写一个数的话，该数字默认是循环的次数，且会默认从零开始
# for num in range(1,10,2):
#     print(num)
# # 应用练习：用for循环去求1-100的和
# s1 = 0 #定义一个变量来保存计算结果
# for i in range(1,101):
#     s1 += i
# print(s1)
# # 这比while循环简洁多了
#
# # break与continue
# # 前者是中途推出，结束当前循环，后者是结束当前循环后进入下一循环
# # 都是专门在循环中使用的关键字，且只能放在循环内！不然会报错！
# # break：使某一 条件满足时推出循环
# # eg
# num5 = 1
# while num5 < 10:
#     print(f"幽幽子吃了第{num5}个苹果")
#     num5 += 1
#     if num5 == 5:
#         print("吃饱了！！！")
#         break
# # 这里，如果想在字符串里添加变量，在开头加f后用{}包裹变量
# 数字 = 1
# while 数字 <= 10:
#     if 数字 == 5:
#         # 在continue之前一定要修改计数器，否则会进入死循环
#         print("力竭了欸")
#         数字 += 1  # 先递增再跳过本次打印，不然数字会一直为5，从而一直循环
#         continue
#     print(f"灵梦进行了第{数字}场play")
#     数字 += 1
print("欢迎使用等比数列求和for语句版本,需依次输入首项，公比与项数")
b1 = int(input("输入首项"))
q = int(input("输入公比"))
n = int(input("输入项数"))
S = 0
if q == 0:
    print("公比不能为零，请重新运行程序")
else:
    for i in range(1,n+1):
        S = S + b1**i
    print(S)























