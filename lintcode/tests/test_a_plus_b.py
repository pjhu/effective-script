# -*- coding utf-8 -*-

import unittest
from lintcode.a_plus_b import IntegerPlus


class IntegerPlusTestCase(unittest.TestCase):

    def setUp(self):
        self.obj = IntegerPlus()

    def tearDown(self):
        del self.obj

    def test_aplusb(self):
        a, b = 100, -100
        self.assertEqual(self.obj.aplusb(a, b), 0)

    def test_aplusb2(self):
        a, b = 100, 50
        self.assertEqual(self.obj.aplusb2(a, b), 150)


if __name__ == '__main__':
    unittest.main()
