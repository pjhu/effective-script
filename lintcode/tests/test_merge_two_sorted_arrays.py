import unittest
from lintcode.merge_two_sorted_arrays import MergeTwoSortedArrays


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = MergeTwoSortedArrays()

    def tearDown(self):
        del self.obj

    def test_merge_two_sorted_arrays(self):
        self.assertEqual(self.obj.merge_two_sorted_arrays([1, 2, 3, 4], [2, 4, 5, 6]), [1, 2, 2, 3, 4, 4, 5, 6])

    def test_array_is_small(self):
        self.assertEqual(self.obj.merge_two_sorted_arrays([1, 3, 5], [4]), [1, 3, 4, 5])

    def test_arrays_have_one_element(self):
        self.assertEqual(self.obj.merge_two_sorted_arrays([1], [1]), [1, 1])


if __name__ == '__main__':
    unittest.main()
