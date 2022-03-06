"""
crow7
2021年06月01日
"""
print("hello python")

massage = "hello python world"
print(massage)

massage = "hello python crash course world!"
print(massage)

# title方法：将字符串中每个单词首字母大写
name = "ada lovelace"
print(name.title())

# upper方法：字符串字母全部大写
# lower方法：字符串字母全部小写
print(name.upper())
print(name.lower())

# python可以用+拼接字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + last_name
print(full_name.title())

# 换行和添加空白可以用 \t 与 \n
print("\tpython")
print("languages :\npython\nc++\njava")

# strip方法：删除空白
# rstrip:删除右边的空白 lstrip：删除左边的空白
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())

practise_name = "Tom"
print("Hello " + practise_name + ",would you like to learn some python today?")

practise_name_2 = "albret einstein"
practise_senten = "A person who never made a mistake never tried anything new."
print(practise_name_2.title() + " once said," + "“" + practise_senten + "”")
