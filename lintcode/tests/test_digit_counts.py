import unittest
from lintcode.digit_ounts import DigitCounts


class DigitCountsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = DigitCounts()

    def tearDown(self):
        del self.obj

    def test_digit_counts(self):
        self.assertEqual(self.obj.digit_counts(1, 12), 5)


if __name__ == '__main__':
    unittest.main()
