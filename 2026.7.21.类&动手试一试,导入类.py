# # 冰激凌小店
# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#     def greeting(self):
#         print(f'欢迎光临!!!这里是{self.restaurant_name},我们有{self.cuisine_type}')
#     def cuisine(self):
#         print(f"我们提供{self.cuisine_type}")
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type,flavor):
#         super().__init__(restaurant_name,cuisine_type)
#         self.flavor = flavor
#     def ice_cream(self):
#         print("这里的ice都是琪露诺产的")
#     def flavors(self):
#         print(f"你选中的口味为{self.flavor}")
#
# Cirno_ice = IceCreamStand('Cirno','ice',"ice")
# Cirno_ice.ice_cream()
# Cirno_ice.flavors()
# Cirno_ice.greeting()

# 导入类
# 将类储存在模块中，然后在主程序中导入所需的模块
from Restaurant import Restaurant as R
my_restaurant =  R(
    '彬彬',
    "特色菜"
)
my_restaurant.greeting()
# 在同一个模块中储存多个类时，类之间应具有关联性
# Python标准库:
# 其是一组模块，我们安装的Python都包含它，其中含有许多有用的函数，以random模块示例
from random import randint
print(randint(1,6))
# 其是在指定范围内随机取数并返回那个数
from random import choice
# 将一个列表或元组作为参数并返回其中的一个随机值
from random import choice
lis =[1,2,3,4,5,6,7]
print(choice(lis))
# 创建与安全相关的应用程序时，请不要使用模块random
# 类命名应采用驼峰命名法即每个单词的首字母都大写且不使用下划线
# 对于每个类，都应紧跟在类定义后加一个描述
# 可以用空行组织代码，但不要滥用，在类中，可以用空行来分隔方法；在模块中，可以用两个空行来分隔类

