"""
crow7
2021年06月07日
"""

"""
每条if语句的核心都是一个值为 Ture 和 False 的表达式，
如果为Ture则执行if语句后面的代码，
如果为False则忽略这些代码

Python在检查是否相等时，区分大小写
"""
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

print("-------------------------------")

"""
逻辑判断语句
and ：如果两个都为Ture，则可以用And合并返回Ture，否则返回False
or：如果有一个为Ture则返回True，否则返回False
not：检查是否存在，存在返回False，不存在返回True
"""
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print("两个都大于21")
else:
    print('不确定是否大于21')

if age_0 >= 21 or age_1 >= 21:
    print("两个有一个大于21")
else:
    print('都小于21')

user = 'marie'
requested_topping = ['mushrooms', 'onions', 'pineapple']
if user not in requested_topping:
    print(user.title() + ', you can post a response if you wish')

"""
if语句
if 判断语句:
    do something
elif 判断语句:
    do something
。。。

else:
    do something
"""
age = 19
if age >= 18:
    print("You are old enough to vote!")
elif age < 18:
    print("123132132")
else:
    print("Sorry,you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 64:
    price = 10
else:
    price = 19
print("Your admission cost is " + str(price) + ".")

requested_toppings = ["mushrooms", "extra cheese"]
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
else:
    requested_toppings.insert(0, 'pepperoni')
print(requested_toppings)
print("\nFinished making your pizza!")

"""
利用if语句处理列表
"""
requested_toppings = {"mushrooms", "extra cheese", "green peppers"}
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we are out of green peppers right now")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making you pizza!")

# 判空
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")

# 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = {"mushrooms", "extra cheese", "french fries"}

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + '.')
    else:
        print("Sorry we are out of green peppers right now.")
