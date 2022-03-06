"""
crow7
2021年06月12日
"""
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

"""
在Python中，字典是一系列的 键-值 对
每个键都与一个值相关联
可以使用键来访问对应的值
与键关联的值可以使数字，字符串，列表，乃至字典
"""

# 访问字典中的值
print(alien_0['color'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + "points!")

# 添加 键-值 对
print("--------------------------")
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

# 修改字典中的值
print('-----------------------------------')
alien_2 = {'color': 'green'}
print("This alien is " + alien_2['color'] + '.')
alien_2['color'] = 'yellow'
print("This alien is " + alien_2['color'] + '.')

print('------------------------------------')
alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_2['x_position']))
# 向右移动
# 根据速度决定移动多远
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_2['x_position'] = alien_2['x_position'] + x_increment
print("New x-position:" + str(alien_2['x_position']))

# 删除键-值
alien_3 = {'color': 'green', 'points': 5}
print('----------------------------')
print(alien_3)
del alien_3['points']
print(alien_3)

# 由类似对象组成的字典
# 最后一个键值对后面也可以加上逗号，为以后添加键值做准备
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah\'s favorite language is {0}.".format(favorite_languages['sarah'].title()))

# 遍历字典 利用 items()方法返回一个键值对中的键和值
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print("Key :" + key + '\nValue :' + value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print('--------------------------')
for name, language in favorite_languages.items():
    print(
        name.title() + "'s favorite language is " +
        language.title() + '.'
    )

# 遍历字典中的所有键 使用 key()方法,这个方法只能提取键不能提取值
for name in favorite_languages.keys():
    print(name.title())
print('-------------------------------')
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(' Hi' + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + '!')

# 按顺序遍历字典中所有的键
# 可以在for循环中使用 sorted方法进行排序
print('-------------------------------')
for name in sorted(favorite_languages.keys()):
    print(name.title() + ",thank tou for taking the poll.")

# 遍历字典中的所有值 可以用values()方法
print('--------------------------------')
print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language)
# 使用 set()方法可以剔除重复值
print('---------------------------------')
for language in set(favorite_languages.values()):
    print(language)

# 嵌套
print('---------------------------------')
# 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 创建一个空列表
print('-------------------------')
aliens = []
# 创建30个绿色的外星人字典
for alien_number in range(30):
    new_alien = {
        'number': alien_number + 1,
        'color': 'green',
        'points': 5,
        'speed': 'slow',
    }
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print('...')
print("Total number of aliens:" + str(len(aliens)))

# 在字典中存储列表
print('--------------------------------------')
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print("You ordered a " + pizza['crust'] + "-crust pizza" +
      "with the following toppings:")
for topping in pizza['toppings']:
    print('\t' + topping)

print('-----------------------------------')
favorite_languages = {
    'jen': ['python', 'c'],
    'tom': ['java', 'c++'],
    'jack': ['ruby', 'go'],
    'rose': ['java', 'c#'],
}
for name, language in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are :")
    for languages in language:
        print('\t' + languages.title())

# 字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}
for username, user_info in users.items():
    print("\nUsername:" + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print('\tFull name: ' + full_name.title())
    print('\tlocation: ' + location.title())

