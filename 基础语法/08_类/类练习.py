"""
crow7
2021年06月25日
"""


# 9-1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print('人数不能减少')

    def increment_number_served(self, num):
        self.number_served += num

    def describe_restaurant(self):
        print("这个餐厅的名字是：" + self.name)
        print("餐厅主营的菜品是：" + self.type)

    def open_restaurant(self):
        print(self.name + "餐厅正在营业")


restaurant = Restaurant('万福楼', '中餐')
print("我正打算去" + restaurant.name + '吃' + restaurant.type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(10)
restaurant.increment_number_served(4)
print("有" + str(restaurant.number_served) + '顾客来过这个商店')

print('-------------------------------------------------')

# 9-2
restaurant_1 = Restaurant('izumi', '台湾小吃')
restaurant_2 = Restaurant('炸鸡老太', '日式炸鸡')

print("我正打算去" + restaurant_1.name + '吃' + restaurant_2.type)
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

print("我正打算去" + restaurant_1.name + '吃' + restaurant_2.type)
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

print('--------------------------------------')


# 9-3
class User():
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print("用户的名称为" + self.firstname + ' ' + self.lastname)

    def greet_user(self):
        print("你好呀！" + self.firstname + ' ' + self.lastname)


user_1 = User('汤姆', '张三')
user_2 = User('尼古拉斯', '李四')

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print("登录次数为：" + str(user_1.login_attempts))
user_1.reset_login_attempts()
print("登录次数为：" + str(user_1.login_attempts))
user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()
print('----------------------------------')


# 9-6
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='冰淇淋'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_icecream(self):
        print("我在" + self.name + "吃" + self.type + ",他是" + self.flavors + "口味的")


ice_cream = IceCreamStand('喜茶')
ice_cream.flavors = '香草'
ice_cream.show_icecream()
print('--------------------------------')


# 9-7
class Admin(User):
    def __init__(self, first_name, last_name):
        super(Admin, self).__init__(first_name, last_name)
        self.privilege = Privilegs([])


# 9-8
class Privilegs():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        for pr in self.privileges:
            print('- ' + pr)


admin = Admin('crow', 'hawke')
admin.describe_user()
admin.privilege.privileges = {'can reset passwords',
                              'can moderate discussions',
                              'can suspend accounts', }
admin.privilege.show_privileges()
