"""
crow7
2021年06月17日
"""

"""
用def告诉Python之后要定义一个函数
之后是函数名，函数名后的括号里面指出函数为了完成任务还需要其他什么信息
"""


# 定义函数
def greet_user():
    """显示简单的问候语"""
    print("hello")


greet_user()


# 向函数传递信息
def greet_user(username):
    # 显示简单的问候语
    print("Hello, " + username.title() + " !")


greet_user("johe")

"""
实参和形参
形参：函数完成其工作所需的一项信息
实参：调用函数时传递给函数的信息
"""

# 传递实参
# 位置实参
"""
在定义函数的时候可以直接给函数设置默认值,如果值设定一个默认值的话，需要设置默认值的参数需要放置最后
使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。
这让Python依然能够正确地解读位置实参。

函数调用
使用哪种调用方式无关紧要，只要函数调用能生成你希望的输出就行。使用对你来说最
容易理解的调用方式即可。
"""


def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + '.')
    print("My " + animal_type + "'s name is " + pet_name.title() + '.')


describe_pet("hamster", 'harry')

# 多次调用函数
describe_pet("dog", "willie")

"""
关键字实参
关键字实参是传递给函数的名称-值对
可以无需考虑函数中调运的实参顺序，并且可以清晰的指出函数调用中各个值的用途
"""
describe_pet(animal_type='hamster', pet_name='harry')

print('------------------------------------')
"""
返回值
函数可以返回一些数据，这些数据被称为返回值

实参也是可选的，可以将实参指定一个空字符串为默认值，并在函数内做出一定的处理
这样就可以让实参变成可选项
"""


def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name("jimi", 'hedrix', 'lee')
print(musician)

musician = get_formatted_name("jimi", 'hedrix')
print(musician)

print('-------------------------------------')


# 返回字典
def build_person(first_name, last_name, age=''):
    """返回一个字典，期中包含有关一个人的信息"""
    person = {
        'first': first_name,
        'last': last_name
    }
    if age:
        person['age'] = age

    print("\n------" + person + '\n-------------')
    return person


# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# 结合函数使用while循环
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("Frist name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#     age = input("age = ")
#     if str(age) == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name,l_name,age)
#     print(formatted_name)
#     print("\nHello"+formatted_name+'!')


"""
传递列表
函数也是可以传递列表的
"""

print('------------------------')


def greet_users(names):
    for name in names:
        msg = "hello, " + name.title() + '!'
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 在函数中修改列表
# 创建一个列表
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# # 模拟打印每个设计，知道没有未打印为止
# # 打印每个设计之后，都将其转移到打印列表中
# while unprinted_designs:
#     designs = unprinted_designs.pop()
#
#     print("Printing model : " + designs)
#     completed_models.append(designs)
#
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

print('-----------------------------------------')


def print_models(unprinted_designs, completed_models):
    """模拟打印每个设计，直到没有未打印为止"""
    while unprinted_designs:
        designs = unprinted_designs.pop()

        print("Printing model : " + designs)
        completed_models.append(designs)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print('-----------------------')
"""
禁止函数修改列表
有时候在需要保留列表的时候可以创建一个列表的备份
这个时候向函数传递的列表参数为备份参数，这样函数中做出的操作就会对原列表没有影响

传递副本方法如下:
function_name(list_name[:])

使用切片表示法[:]创建列表的副本
"""

"""
传递任意数量的实参
有时候预先不知道函数需要多少个实参，此时可以从调用语句
收集任意数量的实参

写法： *形参
形参名 *形参 表示让python创建一个名为toppings的空元组
并将所有的值都封装到这个元组中
"""


def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print('- ' + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
print('------------------------------------')
"""
如果让函数㝂不同类型的实参，必须在函数丁玉忠将接纳任意数量实参的形参放在最后
Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中
"""


# **形参表示创建一个空字典
def build_profile(first, last, **user_info):
    """创建一个字典，期中包含我们知道的有关用户的一切"""
    profile = {'first_name': first,
               'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             lacation='princeton',
                             field='physics')
print(user_profile)
