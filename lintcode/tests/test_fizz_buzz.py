import unittest
from lintcode.fizz_buzz import FizzBuzz


class FizzBuzzTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = FizzBuzz()

    def tearDown(self):
        del self.obj

    def test_fizz_buzz(self):
        self.assertEqual(self.obj.fizz_buzz(7), ["1", "2", "fizz", "4", "buzz", "fizz", "7"])


if __name__ == '__main__':
    unittest.main()
