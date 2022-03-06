"""
crow7
2021年06月17日
"""
# 7-4
# pizza = []
# while True:
#     peiliao = "请添加配料："
#     peiliaoadd = input(peiliao)
#     if peiliaoadd == 'quit':
#         break
#     else:
#         pizza.append(peiliaoadd)
#         print('添加了' + peiliaoadd)
# print(pizza)
#
# # 7-5
# while True:
#     add_age = "请输入年龄:"
#     age = input(add_age)
#     if age == 'quit':
#         break
#     age = int(age)
#
#     if age <= 3:
#         print("免费")
#     elif age > 3 & age <= 12:
#         print("10块钱")
#     elif age > 12:
#         print("15块钱")
#     else:
#         print("请输入争取的年龄！")

# 7-8
sandwich_orders = ['蔬菜', '火腿', '鸡蛋', '鸡蛋', '鸡蛋', '鸡蛋']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your tuna sandwich" + sandwich)
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)

# 7-9
sandwich_orders = ['蔬菜', '火腿', '鸡蛋', '鸡蛋', '鸡蛋', '鸡蛋']

while '鸡蛋' in sandwich_orders:
    sandwich_orders.remove('鸡蛋')
print(sandwich_orders)

# 7-10
drame = {}
while True:
    name = input("你叫什么名字？ ")
    drame_space = input("你的梦想之地是哪里？ ")
    drame[name] = drame_space

    active_r = input("还要继续调查么 ?(Y/N)")
    if active_r == 'N':
        break

for name, space in drame.items():
    print(name + '的梦想之地是' + space + '。')
