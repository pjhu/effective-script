import unittest
from lintcode.trailing_zeros import TrailingZero


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.obj = TrailingZero()
        pass

    def tearDown(self):
        del self.obj
        pass

    def test_trailing_zeros(self):
        self.assertEqual(self.obj.trailing_zeros(100), 24)


if __name__ == '__main__':
    unittest.main()
