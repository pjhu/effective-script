import unittest
from lintcode.rotate_string import RotateString


class RotateStringTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = RotateString()

    def tearDown(self):
        del self.obj

    # empty string
    def test_rotate_string(self):
        self.assertEqual(self.obj.rotate_string(list(''), 10), [])

    # out of string length
    def test_rotate_string(self):
        self.assertEqual(self.obj.rotate_string(list('timelimiterror'), 1000000000), list('terrortimelimi'))


if __name__ == '__main__':
    unittest.main()
