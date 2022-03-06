"""
crow7
2021年06月17日
"""
# 7-1
want_car = input("What do you want?")
print("Let me see if I can find you a " + want_car)

# 7-2
restaurant = input("有多少个人前来用餐：")
restaurant = int(restaurant)
if restaurant > 8:
    print("没有空桌子了")
else:
    print("请坐")

# 7-3
num = input("请输入一个数字 ： ")
if int(num) % 10 != 0:
    print("不是10的倍数")
else:
    print("是10的背书")
