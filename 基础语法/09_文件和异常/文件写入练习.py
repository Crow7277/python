"""
crow7
2021年07月02日
"""
filename = 'guest.txt'
with open(filename, 'w') as file_object:
    name = input('请输入姓名： \n')
    file_object.write(name)

with open(filename) as file_object:
    print("姓名: " + file_object.read().strip())

while True:
    with open(filename, 'a') as file_object:
        name = input("请输入姓名(输入n退出): ")
        if name == 'n':
            break
        file_object.write(name + '\n')
        print('欢迎您，' + name)

filename = '原因.txt'
while True:
    print("你为什么喜欢编程")
    with open(filename,'a') as file_object:
        reason = input("我喜欢编程是因为")
        if reason == 'n':
            break
        file_object.write(reason+'\n')
