"""
crow7
2021年06月27日
"""

from car import Car


class Battery():
    """一次模拟电动汽车点评的简单常识"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条面熟电瓶容量的消息"""
        print("This car has a" + str(self.battery_size) + "-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

    def get_range(self):
        """打印一条信息，指出点评的续航里程"""
        if self.battery_size == 70:
            range_1 = 240
        elif self.battery_size == 85:
            range_1 = 270

        massage = "This car can go approximately " + str(range_1)
        massage += " miles on a full charge"
        print(massage)


# 定义子类，并在括号内指定父类的名称
class ElectricCar(Car):
    """
    电动汽车的独特之处
    创建子类的实例时，python首先需要完成的任务是给父类的所有属性赋值
    因此子类的方法__init__需要父类施以援手

    方法__init__接收创建Car实例所需要的信息
    """

    def __init__(self, make, model, year):
        """
        初始化父类的实型
        super()是一个特殊的函数，它可以帮助python将父类和子类关联起来

        这行代码让python调用ElectricCar父类的方法__init__()，
        也就是调用 Car类中的__init__()方法
        让ElectricCar实例包含父类的所有属性
        父类也成为超类（superclass）所以super也因此得名
        """
        super().__init__(make, model, year)

        # 创建一个电池容量的属性，并设置其初始值为70
        self.battery_size = 70
        # self.battery也可以调用别的类作为实例为自己使用
        # 将电池的属性都写在一个Battery的类中
        self.battery = Battery()

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    """
    重写父类方法
    对于父类的方法，只有他不符合子类模拟的事务的行为，都可以对他进行重写，因此
    可以在子类中定义一个这样的方法：
    他和要重写的父类的方法同名，这样python不会考虑父类的方法，只考虑子类中定义的方法
    """

    def fill_gas_tank(self):
        """重写父类的fill_gas_tank方法"""
        print("This car doesn't need a gas tank！") 