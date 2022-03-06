"""
crow7
2021年06月03日
"""
magicians = ['alice', 'david', 'carolia']
for magician in magicians:
    print(magician)
    print(magician.title())
print("-----------")

for magician in magicians:
    print(magician.title())

print("-----------")

for magician in magicians:
    print(magician.title())

print("-----------")

"""
for循环：for 变量 in 列表：
如果想要实现循环可以使用数字列表 range（开始数字，结束数字后一位）
"""
for value in range(1, 10):
    print(value)

"""
list()的参数，输出将为一个数字列表
"""
print("----------")
numbers = list(range(1, 6))
print(numbers)
"""
range(开始数字，结束数字前后一位，步长)
比如说设置步长为2，则会+2，+2这样输出
"""
even_numbers = list(range(1, 15, 2))
print(even_numbers)

print("----------")

squares = []  # 创建一个空列表
for value in range(1, 11):  # 使用函数range让python遍历1 - 10 的值
    square = value ** 2  # 计算当前值的平方，并将参数带入square
    squares.append(square)  # 将square插入列表squares
print(squares)

# 优化处理
squares_a = []
for value in range(1, 11):
    squares_a.append(value ** 2)
print(squares_a)

# 数字列表的最大最小值
digits = range(0, 10)
print("min = " + str(min(digits)))
print("max = " + str(max(digits)))
print("sum = " + str(sum(digits)))

# 列表解析
"""
列表解析
首先传建一个列表名，然后指定方括号，在放方括号中写 在这个例子中，
values**2 计算平方值
for循环 此时的for循环没有用冒号，在这里相当于讲值1 - 10提供给了表达式 values**2
"""
squares_b = [values ** 2 for values in range(1, 11)]
print(squares_b)
print("----------------")
# 切片
"""
切片是指处理列表中的部分元素
要创建切片可以指定要使用的第一个元素的索引到最后一个元素的索引加一
与函数range一样，会在第二个索引前面的元素后停止
比如要输出前三个元素，则需要指定索引 0 - 3，这将分别输出为 0 1 2的元素
"""
players = ['charles', 'martina', 'florence', 'michael', 'eli']
print(players[0:3])
print(players[1:4])
# 如果没有指定第一个索引将从头开始，如果没有指定后面的索引则会提取到列表的末尾
print(players[:3])
print(players[1:])
# 负数索引可以返回距离列表末尾响应距离的元素
print(players[-3:])  # 返回后三位

