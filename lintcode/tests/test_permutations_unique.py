import unittest
from lintcode.permutations_unique import PermutationsUnique


class PermutationsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = PermutationsUnique()

    def tearDown(self):
        del self.obj

    def test_permute_unique(self):
        self.assertEqual(self.obj.permute_unique([1, 1, 2]),
                         [[1, 1, 2], [1, 2, 1], [2, 1, 1]])
        self.assertEqual(self.obj.permute_unique_2([1, 1, 2]),
                         [[1, 1, 2], [1, 2, 1], [2, 1, 1]])

if __name__ == '__main__':
    unittest.main()
