"""
crow7
2021年06月04日
"""
# 4-1
foods = ['小笼包', '小米粥', '大米粥']
for food in foods:
    print("我最喜欢的早餐是" + food)
print("每天早上一定要吃早餐！")

# 4-2
animals = ['cut', 'dog', 'elephant']
for animal_name in animals:
    print("The animal name is {0}".format(animal_name))
print("The are animals")

"""
解析列表 数字列表
"""
# 4-3
num_1 = [value for value in range(1, 21)]
print(num_1)

# 4-4
num_2 = [value for value in range(1, 10000001)]
# print(num_2)

# 4-5
print(max(num_2), sum(num_2), min(num_2))

# 4-6
for value in range(1, 21, 2):
    print(value)

# 4-7
for value in range(3, 31, 3):
    print(value)

# 4-8
lifang = []
for value in range(1, 11):
    lifang.append(value ** 3)
print(lifang)

# 4-9
value = [values ** 3 for values in range(1, 11)]
print(value)

"""
列表切片
"""
# 4-10
my_food = ['pizza', 'falafel', 'carrot cake', 'ice cream', 'pancake', 'chocolate']
print("The first three items in the list are:")
first_food = my_food[0:3]
print(first_food)

print("\nThree items from the middle of the list are:")
middle_food = my_food[1:4]
print(middle_food)

print("\nThe last three items in the list are:")
last_food = my_food[-3:]
print(last_food)

# 4-11
friend_pizzas = foods[:]
print(friend_pizzas)
friend_pizzas.append("大米粥")
foods.append("油条")
print("My favorite food are:")
for Pfood in foods:
    print(Pfood)
print("My friend favorite food are:")
for Pfood_1 in friend_pizzas:
    print(Pfood_1)

# 4-12
for Pfood_2 in my_food:
    print(Pfood_2)
for Pfood_3 in first_food:
    print(Pfood_3)

"""
元组
"""
# 4-13
buffets = ('牛排', '意大利面', '寿司', '炒饭', '蛋糕', '螃蟹', '龙虾')
for buffet in buffets:
    print(buffet)
buffets = ('牛排', '意大利面', '烧烤', '炒饭', '蛋糕', '牡蛎', '龙虾')
for buffet in buffets:
    print(buffet)
