# 类将函数和数据整洁地封装起来，使使用更高效
# 类几乎可以模拟任何东西
# 示例：创建琪露诺类
class Chirno: #命名一个“琪露诺”类 在python中，首字母大写的是类
    def __init__(self,name,age): #初始化属性name和age
        self.name = name #获取与形参name相关的值并赋给name,然后其被关联到相关实力
        self.age = age # 这样通过示例访问的变量称为属性

    def sit(self):
        print(f"{self.name} is sitting now.")
    def roll_over(self):
        print(f"{self.name} is rolling over!")
# 类中的函数称为方法
# 方法__init__是一个特殊方法，当根据琪露诺类创建新实例时会被自动运行。
# 这类方法的命名中左右都含有两个下划线，旨在避免与普通命名方法产生冲突
# self能让实例访问类中的属性和方法，其必不可少
# self会自动传递,只需要传递后两个形参提供值

# 另外定义了两个方法,执行时不需要额外的信息,因为只有一个新参self,而其会自动传递
# 所有琪露诺都会sit和roll_over了
# 接下来创建一个琪露诺实例:
my_slave = Chirno("BAKA",9)
print(f"我的朋友的名字是{my_slave.name}") #访问slave的name属性
print(f"我的朋友的年龄是{my_slave.age}")
# 句点表示法:获悉属性的值

# 调用方法:
my_slave.sit()
my_slave.roll_over()

my_slave2 = Chirno("BEACH",99)
my_slave2.roll_over()
my_slave2.sit()

# 动手试一试:
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} restaurant is {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is open")

awsl = Restaurant("MMT","Chinese")
awsl.describe_restaurant()
awsl.open_restaurant()

class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def greet_user(self):
        print(f"Hello {self.username}, welcome to my restaurant")
    def describe_user(self):
        print(f"{self.username} restaurant is {self.password}")
    