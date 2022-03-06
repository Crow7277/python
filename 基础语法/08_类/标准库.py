"""
crow7
2021年06月27日
"""
"""
Python的标准库是一组模块，安装的Python都包含它

模块collections中的一个类OrderedDict
这个模块类似于字典，字典可以让信息关联起来，但是不记录添加的键值对的顺序
这个实例的行为几乎与字典相同但是他可以记录添加顺序
"""

# 从模块collections中导入OrderedDict类
from collections import OrderedDict

# 创建OrderedDict类的一个实例
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')

# 练习 9-13
program_word = OrderedDict()
program_word['title'] = '首字母大写'
program_word['append'] = '在列表最后添加元素'
program_word['insert'] = '在列表指定位置插入元素'
program_word['dir'] = '删除'
program_word['pop'] = '弹出'
for key, value in program_word.items():
    print("关键字" + key + '表示' + value)

# 练习 9-14
from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        self.sides = randint(1, self.sides)
        print("骰子表示的数为:" + str(self.sides))


touzi_1 = Die()
touzi_1.roll_die()

touzi_1.sides = 10
touzi_1.roll_die()

touzi_1.sides = 20
touzi_1.roll_die()
