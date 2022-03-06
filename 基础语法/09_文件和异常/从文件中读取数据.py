"""
crow7
2021年06月27日
"""
"""
读取整个文件
在同一个目录下创建了一个pi_digits.txt文件
读取这个文件
"""
"""
open()函数：
接受一个参数为要打开的文件名称
此时python会在当前模块所在目录中搜索参数里那个名称的文件

open()函数返回值一个表示文件的对象

因此open('pi_digits.txt')表示返回一个表示文件pi_digits.txt的对象，
python将这个对象存储在我们将后面使用的变量中

关键字with：
在不需要访问文件后将其关闭
因此在这个程序中我们使用了open函数但是却没有调用close()函数

可以调用open(),close()函数来打开和关闭文件，但是如果程序存在bug导致未妥善关闭文件的话，
会导致数据丢失或者受损
如果过早的是用close()，会发现需要使用文件时它已经关闭(无法访问)，会导致更多的错误
所以可以利用with 让python自动判断什么时候关闭

with 语句实质是上下文管理。
1、上下文管理协议。包含方法__enter__() 和 __exit__()，支持该协议对象要实现这两个方法。
2、上下文管理器，定义执行with语句时要建立的运行时上下文，负责执行with语句块上下文中的进入与退出操作。
3、进入上下文的时候执行__enter__方法，如果设置as var语句，var变量接受__enter__()方法返回值。
4、如果运行时发生了异常，就退出上下文管理器。调用管理器__exit__方法
"""
with open('pi_digits.txt') as file_object:
    """
    使用read方法读取这个文件的全部内容
    与原文件相比，输出的内容末尾多了一个空行
    这个空行是因为read()在到达文件末尾时会返回一个空字符串，将这个空字符串显示出来就是一个空行
    如果要删除，可以使用rstrip()
    """
    contents = file_object.read()
    print(contents)
    print(contents.rstrip())

"""
文件路径
打开不在程序文件所属目录的文件
在linux中
file_path = '/home/ehmatthes/other_files/text_files/filename.txt' 
with open(file_path) as file_object:

在Windows中
file_path = 'C:\cow\ehmatthes\other_files\text_files\filename.txt' 
with open(file_path) as file_object:

在linux中使用的是 '/'
在windows中使用的是 '\'
"""
print('----------------------------------------')
"""
逐行读取

读取文件时常常需要检查每一行
可以使用for循环进行逐行检查
"""
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

"""
创建一个包含文件各行内容后的列表
使用关键字with时，open()返回的文件对象只在with代码块内可用
如果要在With代码块外访问，可在with代码块内将文件的各行存储在一个列表中，
并在with代码块外使用该列表
"""
with open(filename) as file_object:
    """
    使用readlines()方法从文件中读取没上，并肩齐存储在一个列表之中
    之后，该列表被存储到变量lines中
    """
    lines = file_object.readlines()

for line in lines:
    print(str(line).rstrip())

"""使用文件的内容"""
pi_string = ''
for line in lines:
    pi_string += str(line).rstrip()
print(pi_string)
print(len(pi_string))

"""如果想要删除空格则需要使用strip()方法"""
pi_string = ''
for line in lines:
    pi_string += str(line).strip()
print(pi_string)
print(len(pi_string))
print('--------------------------')

"""包含以百万位的大型文件"""
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += str(line).strip()

print(pi_string[:52] + "...")
print(len(pi_string))

"""检查文件中包含的数据"""
birthday = input("Enter your birthday , in the form mmddyy :")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
