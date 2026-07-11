# # 列表的基本格式：
# # 列表名 = [元素1,元素2,元素3,...]
# # 所有元素放在中括号内，元素与元素之间用逗号隔开
# # 元素之间的数据类型可以各不相同
# list = [1,2,"3",4,5]
# print(list,type(list))
# # 因为列表是有序的，所以可以根据下标查找，切片等操作
# print(list[1:5])
# # # 列表也是“可迭代对象”（可以for循环遍历取值）
# for i in list:
#     print(i)
# # 列表的常见操作
# # 一，新增，添加元素
# # append()，extend(),insert()
# list.append(114514) # 整体添加
# print(list)
# list.extend("QWQ") # 分散添加，必需是可迭代对象，而整型不是可迭代对象，所以不能直接填数字，直接填会报错
# print(list)
# list.insert(2,"123456") # 指定添加位置后整体添加，若此位置有元素则原元素往后移
# print(list) # 若不指定下标，则会报错
from os import remove
from xml.sax.handler import property_interning_dict

# # 二，修改元素，直接通过下标进行修改
# inf1 = int(input("第十个数"))
# li = [1,2,3,4,5,6,7,8,9,inf1]
# print(li,li[9])
# li[9]="114514"
# print(li,li[9])

# # 三，查找元素
# # in：判断指定元素师范存在列表中，若存在，则1返回Ture，不存在，则返回False
# # not in：与“in”相反
# list2 = ["A","B","C","D","E","F"]
# print("A" in list2)
# # 目标对象 in 列表
# # 应用：用户取名，若重复，则不能使用,知道用户取名合理才可结束程序
# # 先定义一个列表，其中是已有的名称
# # 在字符串中夹带变量：f-string
# list_3 = ["Algene","algene","Algene514","Algene？","algene514","genegene"]
# while True:
#     name = input("为坠落的人类命名")
#     if name in list_3:
#         print(f"{name}已经被占用")
#     else:
#         print(f"{name}命名成功！")
#     # 把昵称新增到列表
#         list_3.append(name)
#         break

# #index：返回指定元素所在的下标，若无该元素，则会报错
# #count：统计指定数据在当前列表出现的次数（两者与字符串的用法相同）
#
# # 四，删除元素
# # del：无返回值。它只负责删除，删除后元素直接消失，你无法获取被删元素的值。
# # pop()：返回被删除的元素。你可以将这个返回值赋给变量，以便后续使用。
# #  del
# list_5 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# del list_5[0] # del 列表[删除元素对应下标]
# print(list_5)
# remove = list_5.pop(1)
# print(remove,list_5)
# lst111 = [10, 20, 30]
# # del 无返回值
# del lst111[1]  # 列表变为 [10, 30]，无法拿到 20
# # pop 有返回值
# removed = lst111.pop(1)  # 列表变为 [10]，removed = 30
# print(removed)        # 输出 30
#
# # remove:根据元素的值进行删除
# li = [114514,111,114514,111,114514,111,114514,111]
# li.remove(114514)
# print(li)
# # 默认删除最开始出现的指定元素
# # 若想要将指定元素都删了
# while 114514 in li:
#     li.remove(114514)
# print(li)  # 输出 [2, 3]
# # 只要114514在li中，执行循环

# 五，排序
# .sort()按照从小到大的顺序排序
# .reverse()是倒序，而不是从大到小
# lst = [0,12,4,5,88,99,10,114514]
# lst.reverse()
# print(lst)
# lst.sort()
# print(lst)
# lst.reverse()
# print(lst)

#,列表推导式

# in 后不仅可以放列表，还可放range函数及可迭代对象
# lst1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# [print(i+1) for i in lst1]
# for i in range(1,9):
#     lst1.remove(i)
# print(lst1)
#
# [lst1.append(i) for i in range(1,9)]
# lst1.sort()
# print(lst1)

# [表达式 for 变量 in 列表 if条件]
# 将1-10中的奇数转移到列表中
list5 = []
[list5.append(i) for i in range(1,10) if i%2==1]
print(list5)

# 列表嵌套
# 一个列表里面还有一个列表
list6 = [1,2,3,4,list5]
print(list6[4])
# 若要取出子列表里的元素，则eg：
print(list6[4][0])























