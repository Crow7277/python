"""
crow7
2021年07月02日
"""
"""
异常

Python使用被称为异常的特殊对象来管理程序执行期间发生的错误
每当发生让Python不知所措的错误时，可以建立一个异常对象

如果编写了处理该异常对象的代码，程序将继续运行

异常是使用 try-except代码块处理的
try-except让Python执行指定的操作，同时告诉Python发生异常时怎么办
使用该代码块，即使出现异常，程序也能继续运行：显示编写好的友好的错误信息，而不是traceback
"""

"""
print(5/0)
Traceback (most recent call last):
  File "D:....
    print(5/0)
ZeroDivisionError: division by zero

此处的zeroDivisionError是一个异常对象
Python无法按你的要求做时，就会创建这种对象。
在这种情况下，Python将停止运行程序，并指出引发了哪种异常，
而我们可根据这些信息对程序进行修改
"""

"""
使用try-except代码块
"""
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print('------简单的计算器-----')
# 简单的计算器
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nFirst number: ")
    if second_number == 'q':
        break
    """
        此时如果第二个数字为零，就会出bug，因为除数不能为零
        所以同try-except来进行异常处理
    """
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

print("------------处理FileNOtFoundError---------------")
"""
使用文件时如果找不到文件会出现FileNOtFoundError错误，此时也可以使用
try-except进行处理
"""
filename = 'alice.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + ' does not exist.'
    print(msg)


# 分析文本
# title = "Alice in Wonderland"
# print(str(title).split())
# """split方法：以空格为分隔符将字符串分炒成多个部分，并将其存储在一个列表中"""
# filename = 'alice.txt'
# try:
#     with open(filename) as file_object:
#         contents = file_object.read()
# except FileNotFoundError:
#     msg = 'Sorry, the file ' + filename + ' does not exist.'
#     print(msg)
# else:
#     words = contents.split()
#     num_word = len(words)
#     print("The file " + filename + " has about " + str(num_word) + " words.")
#

# 分析多本书 可以创建函数
def count_words(filename):
    """计算一个文件大概包含多少个单词"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = 'Sorry, the file ' + filename + ' does not exist.'
        print(msg)
    else:
        words = contents.split()
        num_word = len(words)
        print("The file " + filename + " has about " + str(num_word) + " words.")


# filename = 'learning_python.txt'
# count_words(filename)
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

"""如果想要在失败时正常运行，而且程序不做提示的话，可以在expect中加上pass就可以"""