"""
crow7
2021年06月26日
"""
"""
在编写类的时候，可以使用继承
一个类继承另一个类是，它将在自动获得另一个类的所有属性和方法
原有的类称为父类，新类称为子类
子类继承父了父类的素有属性和方法，同时还可以定义自己的属性和方法
父类必须包含在当前文件中，并且必须在子类前面
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

    def fill_gas_tank(self):
        print("This car has a 30L's gas tank.")


"""
在使用代码模拟实物时，会发现类越来越多，属性和方法的清单以及文件都越来越长时，
可能需要将类的一部分作为一个独立的类提取出来，将大类拆分成很多个协同工作的小类
次数，创建一个名为Battery的类，作为一个实例用作ElectricCar类中的一个属性
"""


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


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_car = Car('audi', 'a8', '2016')
my_car.fill_gas_tank()
my_tesla.fill_gas_tank()
