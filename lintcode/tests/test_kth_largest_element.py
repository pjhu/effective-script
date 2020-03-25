import unittest
from lintcode.kth_largest_element import KthLargestElement


class KthLargestElementTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = KthLargestElement()

    def tearDown(self):
        del self.obj

    def test_kth_largest_element(self):
        self.assertEqual(self.obj.kth_largest_element(3, [9, 3, 2, 4, 8]), 4)

    def test_kth_largest_element_2(self):
        self.assertEqual(self.obj.kth_largest_element(3, [9, 3, 2, 4, 8]), 4)

    def test_kth_largest_element_3(self):
        self.assertEqual(self.obj.kth_largest_element(3, [9, 3, 2, 4, 8]), 4)


if __name__ == '__main__':
    unittest.main()
