"""
crow7
2021年07月02日
"""
"""
写入文件：关闭包含程序的终端出口，这些输出仍然存在，可以在程序结束运行后查看这些输出，分享输出文件
还可以编写输出读取到内存中进行处理
"""

"""写入空文件"""

filename = 'programming.txt'
"""
调用open()时，提供了两个实参，
第一个是要打开文件的名称
第二个 w 是告诉python，要以写入模式打开这个文件

打开文件时，我可以指定：（r）-> 读取模式
打开文件时，我可以指定：（w）-> 写入模式
打开文件时，我可以指定：（a）-> 附加模式
打开文件时，我可以指定：（r+）-> 读取写入模式

如果没有定义，则python按照默认的只读模式打开
如果写入的文件不存在，会自动创建，
如果已经存在并且以 w 写入模式打开，则将在返回文件对象前清空该文件

注：Python只能将字符串写入文本文件，要将数值存储到文本问家长必须先用str将其转换为字符串格式
"""
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

"""写入多行"""
print("------写入多行-------")
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love game.\n")
    file_object.write("I love create game.\n")

with open(filename) as file_object:
    print(file_object.read().strip())

"""
附加到文件

如果要给文件附加内容而不是覆盖能扔，可以用附加模式打开文件件
python不会在返回文件对象前清空文件，而是将写入的文件行都添加到文件末尾
如果没有这个文件会创建新的空文件
"""
print("------附加到文件-------")
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

with open(filename) as file_object:
    print(file_object.read().strip())
