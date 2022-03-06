"""
crow7
2021年06月27日
"""
from restaurant import Restaurant
from 类练习 import Admin

my_restaurant = Restaurant('kfc','洋快餐')
my_restaurant.describe_restaurant()

admin = Admin('tom','hanks')
admin.describe_user()
admin.privilege.show_privileges()