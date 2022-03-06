"""
crow7
2021年07月03日
"""
"""
模块 json 可以将简单额Python书序结构转储到文件中，并在程序再次运行时加载该文件中的数据
还可以使用json在python之间分项数据

json：JavaScript Object Notation

json.dump()：存储数字列表
            有两个实参   1，要存储的数据
                        2，可用于存储数据的文件对象
"""
import json
"""导入json模块"""

numbers = [2, 3, 5, 7, 11, 13]
"""指定了数字列表存储到期中的文件的名称"""
filename = 'numbers.json'
"""以写入模式打开文件"""
with open(filename, 'w') as f_obj:
    """使用函数json.dump()将数字列表存储到文件中"""
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you cam back, " + username + '!')


# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)

except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")

