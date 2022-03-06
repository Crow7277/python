"""
crow7
2021年06月17日
"""
# while
current_num = 1
while current_num <= 5:
    print(current_num)
    current_num += 1

print('-----------------')

# for
for i in range(1, 6):
    print(i)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)

# 使用标志退出循环
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# 使用break退出循环
# Python任何循环都可以用break退出
while True:
    city = input(prompt)

    if city == 'quit':
        break

# 在循环中使用continue
# 可以使用continue语句可以返回到循环的开头，并根据条件测试结果决定是否继续执行循环
current_num = 0
while current_num < 10:
    current_num += 1
    if current_num % 2 == 0:
        continue
    print(current_num)
