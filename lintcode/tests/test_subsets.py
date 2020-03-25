import unittest
from lintcode.subsets import Subsets


class SubsetsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Subsets()

    def tearDown(self):
        del self.obj

    def test_subsets(self):
        self.assertEqual(self.obj.subsets([]), [[]])
        self.assertEqual(self.obj.subsets([1]), [[], [1]])
        self.assertEqual(self.obj.subsets([1, 2]), [[], [1], [2], [1, 2]])
        self.assertEqual(self.obj.subsets([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

    def test_subsets_2(self):
        self.assertEqual(self.obj.subsets_2([]), [[]])
        self.assertEqual(self.obj.subsets_2([1]), [[], [1]])
        self.assertEqual(self.obj.subsets_2([1, 2]), [[], [1], [2], [1, 2]])
        self.assertEqual(self.obj.subsets_2([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

    def test_subsets_3(self):
        self.assertEqual(self.obj.subsets_3([]), [[]])
        self.assertEqual(self.obj.subsets_3([1]), [[1], []])
        self.assertEqual(self.obj.subsets_3([1, 2]), [[1, 2], [1], [2], []])
        self.assertEqual(self.obj.subsets_3([1, 2, 3]), [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []])

    def test_subsets_4(self):
        self.assertEqual(self.obj.subsets_4([]), [[]])
        self.assertEqual(self.obj.subsets_4([1]), [[], [1]])
        self.assertEqual(self.obj.subsets_4([1, 2]), [[], [1], [1, 2], [2]])
        self.assertEqual(self.obj.subsets_4([1, 2, 3]), [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])

if __name__ == '__main__':
    unittest.main()
