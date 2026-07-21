# # 类将函数和数据整洁地封装起来，使使用更高效
# # 类几乎可以模拟任何东西
# # 示例：创建琪露诺类
# class Chirno: #命名一个“琪露诺”类 在python中，首字母大写的是类
#     def __init__(self,name,age): #初始化属性name和age
#         #因为执行时无论如何都先执行这个，所有有“初始化”的含义
#         self.name = name #获取与形参name相关的值并赋给name,然后其被关联到相关实力
#         self.age = age # 这样通过示例访问的变量称为属性
#
#     def sit(self):
#         print(f"{self.name} is sitting now.")
#     def roll_over(self):
#         print(f"{self.name} is rolling over!")
# # 类中的函数称为方法
# # 其他方法中不需要其他额外信息,所以只用一个形参self
# # 方法__init__是一个特殊方法，当根据琪露诺类创建新实例时会被自动运行。
# # 这类方法的命名中左右都含有两个下划线，旨在避免与普通命名方法产生冲突
# # self能让实例访问类中的属性和方法，其必不可少
# # self会自动传递,只需要传递后两个形参提供值
#
# # 另外定义了两个方法,执行时不需要额外的信息,因为只有一个新参self,而其会自动传递
# # 所有琪露诺都会sit和roll_over了
# # 接下来创建一个琪露诺实例:
# my_slave = Chirno("BAKA",9)
# print(f"我的朋友的名字是{my_slave.name}") #访问slave的name属性
# print(f"我的朋友的年龄是{my_slave.age}")
# # 句点表示法:获悉属性的值
#
# # 调用方法:
# my_slave.sit()
# my_slave.roll_over()
#
# my_slave2 = Chirno("BEACH",99)
# my_slave2.roll_over()
# my_slave2.sit()
#
# # 动手试一试:
# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} restaurant is {self.cuisine_type}")
#     def open_restaurant(self):
#         print(f"{self.restaurant_name} restaurant is open")
#
# awsl = Restaurant("MMT","Chinese")
# awsl.describe_restaurant()
# awsl.open_restaurant()
#
# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password
#     def greet_user(self):
#         print(f"Hello {self.username}, welcome to my restaurant")
#     def describe_user(self):
#         print(f"{self.username} restaurant is {self.password}")
#
# mystia  = Restaurant("小摊","混杂")
# mystia.describe_restaurant()
# mystia.open_restaurant()
#
# # class Friends:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age
# #         self.weizhi = 114514
# #     def hello(self):
# #         print(f"Hello {self.name}, how are you?")
# #     def chat(self):
# #         print(f"Hello {self.name}, What is your age?Let me see...Is'{self.age} ?")
# #     def summary(self):
# #         print(f"Hello {self.name}, {self.age}，{self.weizhi}!")
#
# # bba = Friends("Bob","18")
# # bba.summary()
# # 创建实例时，有些属性无需定义 如上方的weizhi，但必需直接给其一个确定的值
#
# # 修改属性的值：
#
# # 1，对固定实例直接修改,即直接访问属性
# # bba.weizhi = 114
# # bba.summary()
#
# # 2，通过方法修改属性的值
# # class Friends:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age
# #         self.weizhi = 114514
# #     def hello(self):
# #         print(f"Hello {self.name}, how are you?")
# #     def chat(self):
# #         print(f"Hello {self.name}, What is your age?Let me see...Is'{self.age} ?")
# #     def summary(self):
# #         print(f"Hello {self.name}, {self.age}，{self.weizhi}!")
# #
# #     def update(self):   #这里，定义一个方法
# #         # 每个与实例相关联的方法都会自动传递实参self，起一个指向实例本身的引用作用
# #         date1 = int(input('上传更新数据'))
# #         if date1 > self.weizhi:
# #             self.weizhi = date1  #更新实例中的数据
# #         else:
# #             print("更新数据不能小于原数据")
# # bba = Friends("bba", "18")
# # bba.summary()
# # bba.update()
# # bba.summary()
#
# # 3,通过方法对属性的值进行递增
# class Friends:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.weizhi = 114514
#     def hello(self):
#         print(f"Hello {self.name}, how are you?")
#     def chat(self):
#         print(f"Hello {self.name}, What is your age?Let me see...Is'{self.age} ?")
#     def summary(self):
#         print(f"Hello {self.name}, {self.age}，{self.weizhi}!")
#
#     def update(self):   #这里，定义一个方法
#         # 每个与实例相关联的方法都会自动传递实参self，起一个指向实例本身的引用作用
#         date1 = int(input('上传更新数据'))
#         if date1 > self.weizhi:
#             self.weizhi = date1  #更新实例中的数据
#         else:
#             print("更新数据不能小于原数据")
#     def increase(self):
#         ics = int(input("输入增值"))
#         self.weizhi += ics
# bba = Friends("bba", "18")
# bba.summary()
# bba.update()
# bba.summary()
# bba.increase()
# bba.summary()
#
# # 继承:
# # 编写类时,并非总要从零开始,若要编写的类是另一个现成类的特殊版本,可以使用"继承"
# # 原有的类成为父类,而新类为子类
# # 子类继承了父类的所有属性和方法,同时还可以定义自己的属性和方法这将初始化在父类__init__方法中定义的所有属性,让子类包含他们
# # class Best_Friend(Friends): #创建子类时,必须在圆括号内指定父类名称
# #     # 子类的方法__init__通常要调用父类的方法__init__().
# #     def __init__(self,name, age):#初始化属性
# #         # super是个特殊函数,让你能调用父类的方法__init__,父类也称"superclss"超类
# #         super().__init__(name,age)
# #     def birthday(self):
# #         bd = str(input("输入生日"))
# #         print(f"好友的生日是{bd}")
# #         # 这样,初始化后就拥有了父类的所有功能
# # Alice = Best_Friend("514",18)
# # Alice.hello()
# # 当前,我们只想确认电动车具备普通汽车的行为
# # 之后,我们非子类添加特有属性
# # Alice.birthday()
#
# # 重写"父类的方法"
# # 若一个功能只想在父类中执行,而不想在子类中执行,那么要重写父类
# # 方法
# # 在子类中定义一个与要重写的父类的方法同名的方法,这样Python将不会考虑这个父类方法,只关注子类中定义的方法
# # class Best_Friend(Friends): #创建子类时,必须在圆括号内指定父类名称
# #     # 子类的方法__init__通常要调用父类的方法__init__().
# #     def __init__(self,name, age):#初始化属性
# #         # super是个特殊函数,让你能调用父类的方法__init__,父类也称"superclss"超类
# #         super().__init__(name,age)
# #     def birthday(self):
# #         bd = str(input("输入生日"))
# #         print(f"好友的生日是{bd}")
# #         # 这样,初始化后就拥有了父类的所有功能
# #     def increase(self):
# #         print("已经到顶了!")
# # Alice = Best_Friend("514",18)
# # Alice.hello()
# # Alice.increase()
#
# # 将实例作为属性
# class Exprience:
#     def __init__(self,happy = "happy",unhappy = "unhappy"):
#         self.happy = happy
#         self.unhappy = unhappy
#     def describe_happy(self):
#         self.happy = str(input("输入开心的事"))
#         print(f"{self.happy} is happy")
#     def describe_unhappy(self):
#        self.unhappy =str(input("输入不开心的事"))
#        print(f"{self.unhappy} is unhappy")
# class Best_Friend(Friends): #创建子类时,必须在圆括号内指定父类名称
#     # 子类的方法__init__通常要调用父类的方法__init__().
#     def __init__(self,name, age):#初始化属性
#         # super是个特殊函数,让你能调用父类的方法__init__,父类也称"superclss"超类
#         super().__init__(name,age)
#         self.exprience = Exprience()
#     def birthday(self):
#         bd = str(input("输入生日"))
#         print(f"好友的生日是{bd}")
#         # 这样,初始化后就拥有了父类的所有功能
#     def increase(self):
#         print("已经到顶了!")
# Alice = Best_Friend("514",18)
# Alice.hello()
# Alice.increase()
# Alice.exprience.describe_happy()

# 模拟实物:
# 需要以另一个境界:逻辑境界而非语法境界思考问题
