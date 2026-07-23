class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def give_raise(self,add_value=5000):
        self.salary += add_value

