"""
针对类的测试被称为测试类

在Python中提供个很多断言方法
断言方法检查认为应该满足的条件是否确实满足，如果不满足，将会引发异常
各种断言方法：
=============================================
方法                          用途
---------------------------------------------
tEqual(a, b)                核实a == b
assertNotEqual(a, b)        核实a != b
assertTrue(x)               核实x为True
assertFalse(x)              核实x为False
assertIn(item, list)        核实item在list中
assertNotIn(item, list)     核实item不在list中
=============================================

上面的这些断言方法可以核实返回的值等于或者不等于预期的值，返回的值为True或者False，
返回的值在列表中或者不在列表中
使用这些方法需要继承unittest.TestCase()的类
"""


class AnonymousSurvey():
    """收集匿名调查问卷"""

    def __init__(self, question):
        """存储一个问题，并为储存答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷"""
        print('Survey results: ')
        for response in self.responses:
            print('- ' + response)
