"""
crow7
2021年07月04日
"""
import unittest
from city_funcitions import city


class test_city_country(unittest.TestCase):

    def test_name(self):
        name = city('santiago', 'chile')
        self.assertEqual(name, 'Santiage,Chile')


unittest.main()

