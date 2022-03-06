"""
crow7
2021年06月01日

列表相关
"""

"""
访问列表元素
"""
bicycles = ["trek", "cannondale", 'redline']
print(bicycles)
print(bicycles[0])
print(bicycles[1])
print(bicycles[0].title())

# 负数索引可以返回距离列表末尾响应距离的元素，因此将索引指定为 -1 则可表示最后一列的元素
print(bicycles[-1])

massage = "My first bicycle was a " + bicycles[0].title() + "."
print(massage)

"""
修改，添加和删除元素
"""
# 修改列表元素
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# 在列表中添加元素
# 可以使用append方法，首先需要定义一个列表空间，之后可以使用append方法在列表添加元素，不过添加是按照顺序添加的
motorcycles.append('honda')
print(motorcycles)

# 在列表中插入元素
# 利用insert方法，可以在列表任意位置插入元素   insert(索引，值)
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 从列表中删除元素
# 使用del语句
del motorcycles[0]
print(motorcycles)
print("\n")

# 使用pop方法删除语句
# pop方法可以删除列表末尾的元素，而且删除后也可以接着使用他
# 如下的例所示，相当于讲列表末尾删除并保存在popped_motorcycles
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

last_owned = motorcycles.pop()
print("The last motorcycle I owned a " + last_owned.title() + ".")
print(motorcycles)

# 弹出列表中任意位置的元素
# pop(索引)
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# 根据值删除元素
# 使用remove方法，只需要知道列表中的值就可以删除
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('suzuki')
print(motorcycles)
# remove方法只能删除第一个指定的值，如果列表中存在多个，则需要用循环判断
motorcycles.remove('suzuki')
print(motorcycles)
