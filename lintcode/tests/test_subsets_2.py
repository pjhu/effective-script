import unittest
from lintcode.subsets_2 import Subsets


class SubsetsTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Subsets()

    def tearDown(self):
        del self.obj

    def test_subsets(self):
        self.assertEqual(self.obj.subsets([1, 2, 2]), [[1, 2, 2], [2, 2], [1, 2], [2], [1], []])

if __name__ == '__main__':
    unittest.main()
