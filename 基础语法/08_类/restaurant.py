"""
crow7
2021年06月27日
"""
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print('人数不能减少')

    def increment_number_served(self, num):
        self.number_served += num

    def describe_restaurant(self):
        print("这个餐厅的名字是：" + self.name)
        print("餐厅主营的菜品是：" + self.type)

    def open_restaurant(self):
        print(self.name + "餐厅正在营业")