import unittest
from survey import AnonymousSurvey

"""
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
"""


# 将测试用例命名为
# TestAnonymousSurvey，它也继承unittest.TestCase类
class TestAnonmyousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""

    def test_store_single_response(self):
        """测试单个答案会被妥善的存储"""
        """
        使用问题"What language did you first learn to speak?"
        创建了一个名为my_survey的实例，
        然后使用方法store_response()存储了单个答案English
        """
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        """
        我们检查English是否包含在列表my_survey.responses中，
        以核实这个答案是否被妥善地存储了
        """
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善的存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


unittest.main()
