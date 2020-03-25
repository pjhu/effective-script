import unittest
from lintcode.str_str import StrStr


class StrStrTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = StrStr()

    def tearDown(self):
        del self.obj

    def test_str_str(self):
        self.assertEqual(self.obj.str_str("abcdefghijk", "bcd"), 1)

    def test_str_str_2(self):
        self.assertEqual(self.obj.str_str_2("abcdefghijk", "bcd"), 1)


if __name__ == '__main__':
    unittest.main()
