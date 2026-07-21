class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def greeting(self):
        print(f'欢迎光临!!!这里是{self.restaurant_name},我们有{self.cuisine_type}')
    def cuisine(self):
        print(f"我们提供{self.cuisine_type}")
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type,flavor):
        super().__init__(restaurant_name,cuisine_type)
        self.flavor = flavor
    def ice_cream(self):
        print("这里的ice都是琪露诺产的")
    def flavors(self):
        print(f"你选中的口味为{self.flavor}")

if __name__ == '__main__':
    Cirno_ice = IceCreamStand('Cirno','ice',"ice")
    Cirno_ice.ice_cream()
    Cirno_ice.flavors()
    Cirno_ice.greeting()