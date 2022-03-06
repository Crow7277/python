"""
crow7
2021年06月17日
"""
# 函数input()可以让程序展厅，等待用户输入文本
# massage = input('Tell me something , and I will repeat it back to you: ')
# print(massage)

# name = input("Please enter tour name: ")
# print("Hello " + name)

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "'\nWhat is your first name?"

# name = input(prompt)
# print("\nHello," + name)

# 使用int()获取数值输入,python会将用户的输入理解为字符串，当输入的是数字时，可以使用int()将其转换为int型变量
# height = input("How tall are you , in inches ?")
# height = int(height)
# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

"""
求模运算
运算符：%
将两个数相除兵返回余数
"""
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number %2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")