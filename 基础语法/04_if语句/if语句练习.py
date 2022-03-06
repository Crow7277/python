"""
crow7
2021年06月07日
"""
# 5-1
car = 'subaru'
print("Is car == 'subaru' ? I predict True")
if car == 'subaru':
    print("Car is subaru")
else:
    print("Car is not subaru")
if car == 'audi':
    print("Car is Audi")
else:
    car = "Audi"
    print(car == 'subaru')

# 5-2
alien_color = 'green'
if alien_color == 'green':
    print("You get 5 point!")

# 5-3
if alien_color == 'green':
    print("You get 5 point!")
else:
    print("You get 10 point!")

# 5-4
if alien_color == 'green':
    print("You get 5 point!")
elif alien_color == 'yellow':
    print("You get 10 point!")
elif alien_color == 'red':
    print("You get 15 point!")

# 5-5
age = 18
if age < 2:
    print("你是婴儿")
elif 2 <= age < 4:
    print("蹒跚学步")
elif 4 <= age < 13:
    print("你是儿童")
elif 13 <= age < 20:
    print("你是青少年")
elif 20 <= age < 65:
    print("你是成年人")
elif age >= 65:
    print("你是老年人")

# 5-6
favorite_fruits = ['苹果', '柚子', '西瓜']
if '苹果' in favorite_fruits:
    print("你真的很喜欢吃苹果耶！\n")
if '西瓜' in favorite_fruits:
    print("你真的很喜欢吃西瓜耶！\n")
if '柚子' in favorite_fruits:
    print("你真的很喜欢吃柚子耶！\n")

# 5-7
user_names = ['crow', 'hake', 'admin', 'dance', 'devi']
for user_name in user_names:
    if user_name == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello Eric,thank you for logging in again.")
print("---------------------------------")
# 5-8
user_names = ['crow', 'hake', 'admin', 'dance', 'devi']
if not user_names:
    print("We need to find some users!")
else:
    for user_name in user_names:
        if user_name == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello Eric,thank you for logging in again.")

current_users = ['crow', 'hake', 'admin', 'dance', 'devi']
new_users = ['core', 'crow', 'hawker', 'hake', 'Davi']
for new_user in new_users:
    if new_user in current_users:
        print(new_user + "已使用")
    else:
        print(new_user + "未使用")
