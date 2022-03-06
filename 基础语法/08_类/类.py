"""
crow7
2021年06月24日
"""
"""
面向对象编程是最有效的比那些方法之一
在面向对象编程中，编写表示现实世界中的事务和清净的类，并基于这些类来创建对象

基于类创建对象时，每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独特的个性

根据类创建对象被称为实例化
"""

"""
创建Dog类
包含这个小狗的名字和年龄
并赋予小狗蹲下和打滚的能力

在Python中，首字母大写的名称指的是类
"""


class Dog():
    """一次模拟小狗的简单尝试"""
    """
    init__方法是一个特殊的方法，每当在类中穿件新的实例时
    python会自动运行这个方法
    在这个方法的名称中，开头和末尾有两个下划线，
    这是一种约定，避免python默认方法与普通方法名称发生冲突
    
    在这个类中，init方法定义了三个形参：self，name，age
    在方法的定义中，self形参必不可少，并且必须位于其他形参的前面
    因为在python调用init方法来创建Dog实例时，将自动传入实参self，
    每个与类相关联的方法调用都自动传递实参self，他是个指向实例本身的引用，
    让实例能够访问类中的属性和方法
    
    以self为前缀的比那两都可以供类中所有的方法使用，我们也可以通过类的实例访问这些变量
    
    """

    def __init__(self, name, age):
        """初始化属性name和age"""
        # self.name = name获取存储在形参name中的值,并将其存储到变量name中
        # 可以通过实例访问的变量称为属性
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗的蹲下命令"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗打滚的命令"""
        print(self.name.title() + " rolled over!")


"""
根据类创建实例
根据Dog类创建一个特定小狗的实例
"""

"""
Python使用实参'willie'和6调用Dog方法中的__init__()
方法__init__创建一个表示特定小狗的示例，并使用我们提供的值来设置属性name和age

方法__init__并未显示的包含return语句，但是python会自动返回一个表示这条小狗的实例
我们将这个实例存储在变量my_dog中
"""
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)
print("Your dog's name is " + your_dog.name.title() + '.')
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()

