"""
crow7
2021年07月03日
"""
# # 10-6
# while True:
#     print("输入n退出")
#     try:
#         first_number = input("请输入一个数字：")
#         if first_number == 'n':
#             break
#         first_number = int(first_number)
#
#         second_number = input("请输入一个数字：")
#         if second_number == 'n':
#             break
#         second_number = int(second_number)
#
#     except ValueError:
#         print("请输入一个数字哦！")
#     else:
#         sum_number = first_number + second_number
#         print(str(first_number) + " + "
#               + str(second_number) + " = "
#               + str(sum_number))


# 10-8


def creattext(filename):
    i = 0
    with open(filename, 'w') as f_ob:
        while True:
            print("----现在打开的是"+filename)
            name = input("请输入一个名字：")
            f_ob.write(name+'\n')
            i = i + 1
            if i == 3:
                break


creattext('cat.txt')
creattext('dog.txt')
