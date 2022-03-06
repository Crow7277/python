"""
crow7
2021年06月19日
"""


# 8-1
def display_message():
    print("123123")


display_message()


# 8-2
def favorite_book(title):
    print("One of my favorite books is " + title.title())


favorite_book("santi")


# 8-3
def make_shirt(size, t_type="I love python"):
    print("This t-shirt’s size is " + size)
    print("需要在T恤衫上打印 " + t_type)


make_shirt('middle size')

# 8-4
make_shirt("oversize")


# 8-5
def describe_city(city_name, city_country="china"):
    print(city_name.title() + ' is in ' + city_country.title())


describe_city("wuhan")
describe_city("shanghai")
describe_city("beijing")
describe_city("tokyo", 'japan')


# 8-6
def city_country(city_name, country_name):
    city = {
        'name': city_name,
        'country': country_name
    }
    city_1 = city['name'] + ' , ' + city['country']
    return city_1


city_1 = city_country("tokyo", 'japan')
print(city_1)


# 8-7
# def make_album(singer_name, album_name, count=''):
#     album = {
#         'name': singer_name,
#         'album': album_name
#     }
#     if count:
#         album['song_num'] = count
#     return album
#
#
# for i in range(3):
#     name = input("singer name is :")
#     albumname = input("album name is :")
#     num = input("输入歌曲数：")
#     al = make_album(name, albumname,num)
#     print(al)

# 8-9
def show_magicians(names):
    for name in names:
        print(name)


magician_name = ['刘谦', '大卫科波菲尔', '成林苏']
show_magicians(magician_name)

print('-------------------------')


# 8-10
def show_magicians(names):
    for name in names:
        print(name)


# def make_great(names):
#     great_magicians = []
#     while names:
#         great_magicians.append(names.pop() + 'the great')
#
#     for great_magician in great_magicians:
#         names.append(great_magician)


magician_name = ['刘谦', '大卫科波菲尔', '成林苏']
# show_magicians(magician_name)
#
# #make_great(magician_name)
# show_magicians(magician_name)

print('------------------------------')


# 8-11
def make_great(names):
    great_magicians = []
    while names:
        great_magicians.append(names.pop() + 'the great')

    for great_magician in great_magicians:
        names.append(great_magician)
    return great_magicians


great_magicianss = make_great(magician_name[:])
show_magicians(great_magicianss)
show_magicians(magician_name)


# 8-12
def sandwith(*food_list):
    print(food_list)


sandwith('火腿', '香肠')
sandwith('鸡蛋', '肉饼')
sandwith('三文鱼', '生菜')


# 8-13
# **形参表示创建一个空字典
def build_profile(first, last, **user_info):
    """创建一个字典，期中包含我们知道的有关用户的一切"""
    profile = {'first_name': first,
               'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('123', '456',
                             年龄='23',
                             性别='男',
                             学历='硕士')
print(user_profile)
print('----------------------------------')


# 8-14
def makecar(maker, cartype, **other):
    cars = {
        '品牌': maker,
        '类型': cartype,
    }
    for key, value in other.items():
        cars[key] = value
    return cars


car = makecar('subaru', 'outback', color='blue', tow_package=True)
print(car)
