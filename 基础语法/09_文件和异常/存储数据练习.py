"""
crow7
2021年07月03日
"""
import json


def get_number():
    filename = 'favoritenumber.json'
    try:
        with open(filename) as f_boj:
            f_num = json.load(f_boj)

    except FileNotFoundError:
        return None
    else:
        return f_num


def get_new_number():
    f_num = input("请输入你喜欢的数字： ")
    filename = 'favoritenumber.json'
    with open(filename, 'w') as f_obj:
        json.dump(f_num, f_obj)
    return f_num


def f_number():
    f_num = get_number()
    if f_num:
        print("Your favorite number! It’s " + f_num)
    else:
        f_num = get_new_number()
        print("I know your favorite number! It’s " + f_num)


f_number()
