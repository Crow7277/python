"""
crow7
2021年06月27日
"""


class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        # 给属性设定默认值
        self.odometer_reading = 0

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止就里程表的值往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer! ")

    def increment_odometer(self, miles):
        """将里程碑读书增加指定的量"""
        self.odometer_reading += miles

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印出一条指出汽车里程的信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it")

