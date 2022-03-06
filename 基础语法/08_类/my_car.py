"""
crow7
2021年06月27日
"""
"""
Python可以将类存储在模块中
创建一个包含Car的类
"""

from car_1 import Car, ElectricCar

"""
此处的import语句让Python打开模块car，并导入期中的Car类
如果要导入多个类，需要用逗号分隔各个类，导入必要的类之后，
根据需要创建每个类的任意数量的实例

导入所有类的话可以使用 form 模块名 import * 

但是不推荐这种导入方式
1，看开头的import语句可以明白使用了哪些类，十分方便
2，可以避免名称方面的错误
"""

# import car
"""
这里也可以导入整个模块
此时创建实例时需要使用 模块名.类名
并且因为创建实例时习俗要用到模块名，所以不会与当前稳健使用的任何名称发生冲突
"""

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
