"""
crow7
2021年06月30日
"""

print('打印整个文件')
filename = 'learning_python.txt'
memo_text = ''
with open(filename) as file_object:
    lines = file_object.readlines()
print(lines)

print('\n---------------------------\n打印时遍历文件\n')
for line in lines:
    print(line.rstrip())

print('\n---------------------------\n存储在一个列表中\n')
for line in lines:
    memo_text += line.strip() + '\n'
print(memo_text)

print('---------------------------')
for line in lines:
    line.replace('Python', 'c')
    memo_text += line.strip() + '\n'
print(memo_text)

