import unittest
from lintcode.permutations import Permutations


class PermutationsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Permutations()

    def tearDown(self):
        del self.obj

    def test_permute(self):
        self.assertEqual(self.obj.permute([1]), [[1]])
        self.assertEqual(self.obj.permute([0, 1]), [[0, 1], [1, 0]])
        self.assertEqual(self.obj.permute([0, 1, 2]),
                         [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])

    def test_permute_2(self):
        self.assertEqual(self.obj.permute_2([0, 1, 2]),
                         [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])

    def test_permute_toos(self):
        self.assertEqual(self.obj.permute_tools_1([0, 1, 2]),
                         [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])
        self.assertEqual(self.obj.permute_tools_2([0, 1, 2]),
                         [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])

    def test_permute_recursion(self):
        self.assertEqual(self.obj.permute_recursion_1([0, 1, 2]),
                         [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])
        self.assertEqual(self.obj.permute_recursion_2([0, 1, 2]),
                         [[0, 1, 2], [0, 2, 1], [1, 2, 0], [1, 0, 2], [2, 0, 1], [2, 1, 0]])
        self.assertEqual(self.obj.permute_recursion_3([0, 1, 2]),
                         [[2, 1, 0], [1, 2, 0], [2, 0, 1], [0, 2, 1], [1, 0, 2], [0, 1, 2]])

    # http://stackoverflow.com/questions/11483060/stdnext-permutation-implementation-explanation
    def test_permute_unique(self):
        self.assertEqual(self.obj.permute([1, 2, 2]),
                         [[1, 1, 2], [1, 2, 1], [2, 1, 1]])

if __name__ == '__main__':
    unittest.main()
