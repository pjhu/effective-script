import unittest
from lintcode.ugly_number_2 import NthUglyNumber


class NthUglyNumberTestCase(unittest.TestCase):

    def setUp(self):
        self.obj = NthUglyNumber()

    def tearDown(self):
        del self.obj

    def test_find_next_ugly_number(self):
        self.assertEqual(self.obj._find_next_ugly_number([1, 2, 3]), 4)

    def test_nth_ugly_number(self):
        self.assertEqual(self.obj.nth_ugly_number(9), 10)


if __name__ == '__main__':
    unittest.main()
