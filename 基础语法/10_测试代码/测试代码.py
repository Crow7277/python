"""
crow7
2021年07月03日
"""


def get_formatted_name(first, last,middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()


# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last = input("Please give me a last name: ")
#     if last == 'q':
#         break
#
#     formatted_name = get_formatted_name(first, last)
#     print("\tNeatly formatted name: " + formatted_name + '.')

"""
单元测试和测试用例

Python标准库中的模块unittest提供了代码测试工具

单元测试：用于核实函数的某个方面没有问题
测试用例：是一组单元测试，这些单元测试一起核实函数在各种情况下的行为都符合要求。
         良好的测试用例考虑到了函数可能受到的各种输入，包含针对所有这些情景的测试
全覆盖是测试：用力包含一整台测试单元，涵盖的各种可能的函数使用方式
            对于大型项目，要实现全覆盖可能很难
通常，最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖
"""

"""
可通过的测试

要为函数编写测试用例，可先导入模块 unittest 以及测试的函数，再创建一个 unittest.TestCase类
并编写一系列方法对函数行为的不同方法进行测试
"""
import unittest

"""
创建NamesTestCase类，继承unittest.TestCase类

NameTestCase只包含一个方法，用于测试get_formatted_name()的一个方面
我们将这个方法命名为test_last_name(),
因为我们要核实的是只有名和姓的姓名是否能被正确的格式化
"""


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        # 使用实参调用get_formatted_name()并将结果存储到变量中
        formatted_name = get_formatted_name('janis', 'joplin')
        """
        使用了unittest类最有用的功能之一：一个断言方法

        断言方法用来核实得到的结果是否与期望的结果一致
        调用unittest的方法assertEqual()，并传递变量和实参

        将formatted_name的值同字符串'Janis Joplin'进行比较，如果它们相等，就万事大吉，如果它
        们不相等，跟我说一声
        """
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name,
                         'wolfgang', 'mozart', 'amadeus')


unittest.main()
"""
输出
.
----------------------------------------------------------------------
Ran 1 tests in 0.000s


OK
第一行的句点表明有一个测试通过了
之后的Ran 0 tests in 0.000s表示测试用时
最后的OK表示所有单元测试都通过了


如果不能通过
则会显示

E 
====================================================================== 
ERROR: test_first_last_name (__main__.NamesTestCase) 
---------------------------------------------------------------------- 
Traceback (most recent call last): 
 File "test_name_function.py", line 8, in test_first_last_name 
 formatted_name = get_formatted_name('janis', 'joplin') 
TypeError: get_formatted_name() missing 1 required positional argument: 'last' 
---------------------------------------------------------------------- 
Ran 1 test in 0.000s 
FAILED (errors=1)

第一个字母E表示有一个单元测试导致了错误

之后ERROR处会显示出那个单元导致了错误
测试用例包含众多单元测试时，知道那个测试未通过十分重要

在Traceback处，指出了函数调用有问题，因为他缺少了一个必不可少的位置实参
之后会显示测试用时
以及FAILED (errors=1)表示整个测试用例未通过，因为运行该测试用例是发生了一个错误
"""