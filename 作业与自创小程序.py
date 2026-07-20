# ### 等比数列求和：
#
# # for循环版本：
# first_term = int(input("输入首项"))
# normal_diffrence = int(input("输入公比"))
# term_number = int(input("输入项数"))
# total_sum = 0
# for i in range(0,term_number):
#     total_sum += first_term * normal_diffrence ** i
# print(total_sum)
#
# #while循环版本：
# first_term_1 = int(input("输入首项"))
# normal_diffrence_1 = int(input("输入公比"))
# term_number_1 = int(input("输入项数"))
# _ = 1
# total_sum = 0
# while _ <= term_number_1:
#     total_sum += first_term_1
#     _ += 1
#     first_term_1 = first_term_1 * normal_diffrence_1
# print(total_sum)
#
# # 乘法表
# for e in range(1,10):
#     for f in range(1,e + 1): # （1，e + 1）目的是控制每行的计算式数量
#         print(f"{e}*{f} = {e*f}",end="\t") # 因为python会默认end=\n即换行符，为了制表，应该使用制表符\t
#     print() # 内循环结束后换行

# # 1
# # 2000-3200（包括在内）能被7整除但是不能被5整除的数,得到的数字用逗号分开，打印在一行上
# def task1 () :
#     list1 =[]
#     for i in range(2000,3201):
#         if i % 7 == 0 and i % 5 != 0 :
#             list1.append(str(i))
#     print(','.join(list1))
# task1()
#
# # 2
# # 可以给定数阶乘的程序
# def task2 () :
#     object_1 =int(input('输入数字'))
#     total = 1
#     for i in range(0,object_1):
#         total = object_1*total
#         object_1 = object_1-1
#     print(total)
# task2()
#
# # 三
# def task3 () :
#     ob = int(input('输入目标数字'))
#     dic = {}
#     for i in range(1,ob+1):
#         dic[int(i)] = i**2
#     print(dic)
# task3()

