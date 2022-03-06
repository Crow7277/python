"""
crow7
2021年07月03日
"""
"""
代码可以正确运行，但是可以做进一步的改进
        -- 将代码划分为一系列完成具体工作的函数
        这样的过程称为重构
"""
import json


def greet_user():
    """问候用户，并指出名字"""
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you came back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")


greet_user()


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_new_user():
    username = input("What is your name ")
    filename = "username.json"
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        p = input("The user name is right？(Y/N)")
        if p == 'N':
            username = greet_new_user()
        print("Welcome back, " + username + "!")
    else:
        print("We'll remember you when you come back, " + username + "!")


greet_user()
