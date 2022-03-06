"""
crow7
2021年06月14日
"""
# 6-1
person_0 = {
    'first_name': 'crow',
    'last_name': 'tom',
    'age': '28',
    'city': 'tokyo',
}
for person, value in person_0.items():
    print(str(value))

# 6-2
favorite_number = {
    'tom': 10,
    'june': 14,
    'dan': 0,
    'jack': 14,
    'ross': 23,
    'peter': 11,
}
for name, number in favorite_number.items():
    print(name.title() + ' favorite number is ' + str(number))

# 6-3
program_word = {
    'title': '首字母大写',
    'append': '在列表最后添加元素',
    'insert': '在列表指定位置插入元素',
    'dir': '删除',
    'pop': '弹出',
}
for word, meaning in program_word.items():
    print(word + '的意思是：' + meaning + '。')

# 6-4
print('------------------------')
program_word['print'] = '打印输出'
program_word['for'] = 'for循环'
program_word['if'] = '判断语句'
program_word['while'] = "while循环"
for word, meaning in program_word.items():
    print(word + '的意思是：' + meaning + '。')

# 6-5
print('------------------------')
river_country = {
    "长江": '中国',
    "黄河": '中国',
    "鸭川": '日本',
    "思密达河": '韩国',
    "横河": '印度',
}
for river, name in sorted(river_country.items()):
    print(river + '流过' + name + '。')

# 6-6
print('-----------------------------')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
name_list = {'jen', 'tom', 'phil'}
for name in name_list:
    if name in favorite_languages.keys():
        print('thank'.title())
    else:
        print(name + ',请尽快参加调查')

# 6-7
person_1 = {
    'first_name': 'crow',
    'last_name': 'tom',
    'age': '28',
    'city': 'tokyo',
}
person_2 = {
    'first_name': 'asf',
    'last_name': 'jon',
    'age': '30',
    'city': 'kyoto',
}
person_3 = {
    'first_name': 'jojo',
    'last_name': 'ken',
    'age': '17',
    'city': 'osaka',
}
persons = [person_1, person_2, person_3]
print(persons)

print('----------------------')
# 6-8
pet_0 = {
    '名字': 'jojo',
    '品种': '柯基',
    '主人': '空条承太郎',
    '年龄': '2',
}
pet_1 = {
    '名字': 'dio',
    '品种': '哈士奇',
    '主人': '吊爷',
    '年龄': '4',
}
pet_2 = {
    '名字': '卡兹',
    '品种': '柱之男',
    '主人': '二乔',
    '年龄': '1000000',
}
pets = [pet_0, pet_1, pet_2]
print(pets)

# 6-9
favorite_place = {
    'jojo': ['河南', '黑龙江', '广西'],
    'tom': ['东京', '京都', '大阪'],
    'join': ['莫斯科', '浙江', '湖南'],
}
for name, place in favorite_place.items():
    print(name + "喜欢" + str(place))

# 6-10
favorite_number = {
    'tom': [10, 20, 30],
    'june': [20, 123, 12],
    'dan': [123, 5431, 125],
    'jack': [1, 4, 6],
    'ross': [12, 451, 123, 151, 123],
    'peter': [123, 123, 511],
}
for name, number in favorite_number.items():
    print(name.title() + ' favorite number is ')
    for num in number:
        print(str(num))

# 6-11
cities = {
    '洛阳': {
        '人口': 123123123,
        '所属国家': '中国',
    },
    '郑州': {
        '人口': 123123142123,
        '所属国家': '中国',
    },
    '开封': {
        '人口': 12312123123,
        '所属国家': '中国',
    },
}
print('------------------------------')
for name, massage in cities.items():
    print(name + ' 人口：' + str(massage['人口']) + '国家：' + massage['所属国家'])