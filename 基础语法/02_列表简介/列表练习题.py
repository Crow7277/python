"""
crow7
2021年06月01日
"""
# 3-4
invite_list = ['张三', "李四", "王五", "赵六"]
print(invite_list)

# 3-5
absent_guest = invite_list.pop(2)
invite_list.insert(2, '钱六')
print("无法出席的人是" + absent_guest)
print("邀请宾客名单: " + str(invite_list))

# 3-6
invite_list.insert(0, "mark")
invite_list.insert(2, "jone")
invite_list.append("john")
print(invite_list)

# 3-7
print("我很抱歉" + invite_list.pop() + ",你不能来参加我的宴会了")
print("我很抱歉" + invite_list.pop() + ",你不能来参加我的宴会了")
print("我很抱歉" + invite_list.pop() + ",你不能来参加我的宴会了")
print("我很抱歉" + invite_list.pop() + ",你不能来参加我的宴会了")
print("我很抱歉" + invite_list.pop() + ",你不能来参加我的宴会了")
print(invite_list)
print(invite_list[0] + "，你还在，可以来")
print(invite_list[1] + "，你还在，可以来")
del invite_list[0]
del invite_list[0]
print(invite_list)
