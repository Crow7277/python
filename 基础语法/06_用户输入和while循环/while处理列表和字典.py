"""
crow7
2021年06月17日
"""
# 在列表之间移动元素

# 首先创建一个待验证用户列表和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有验证用户位置
# 将每个经过验证的列表都移到已验证列表中
while unconfirmed_users:
    cunfirmed_user = unconfirmed_users.pop()
    print("Verifying user: " + cunfirmed_user.title())
    confirmed_users.append(cunfirmed_user)

# 显示所有已验证用户
print("\nThe following users have been confirmed:")
for confirmend_user in confirmed_users:
    print(confirmend_user.title())

print('------------------------------------')

# 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 使用用户输入填充字典
responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
print(responses)
for name, mountain in responses.items():
    print(name.title() + "would like to climb " + mountain.title() + '.')
