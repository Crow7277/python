"""
crow7
2021年06月02日
"""
# 列表中可以利用 sort方法进行排序，如果是字符的话，可以按照字母顺序升序排列
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# 利用reverse = True 实现倒叙排列
cars.sort(reverse=True)
print(cars)

# sorted函数对列表进行临时排序
# 可以保留原来顺序，只进行临时的排序
print("Here is the original list :")
print(cars)
print("\nHere is the sorted list :")
print(sorted(cars))
print("Here is the original list :")
print(cars)

# 将列表倒着打印，不是倒序，而是单纯的翻转列表，可以使用 reverse方法
print(cars)
cars.reverse()
print(cars)

# 使用len函数可以获得列表的长度
len(cars)
