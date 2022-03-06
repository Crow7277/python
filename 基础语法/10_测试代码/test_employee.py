"""
crow7
2021年07月05日
"""
import unittest
from employee import Employee


class employee_test(unittest.TestCase):
    def setUp(self):
        """创建一个对象"""
        self.my_employees = Employee('Tom','Morty',10000)

    def test_give_default_raise(self):
        self.my_employees.give_raise()
        self.assertEqual(self.my_employees.annual_salary,15000)

    def test_give_custom_raise(self):
        self.my_employees.give_raise(10000)
        self.assertEqual(self.my_employees.annual_salary,30000)


unittest.main()
