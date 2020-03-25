import unittest
from lintcode.search_range_in_binary_search_tree import SearchRangeInBinarySearchTree
from lintcode.search_range_in_binary_search_tree import TreeNode


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = SearchRangeInBinarySearchTree()

    def tearDown(self):
        del self.obj

    # empty tree
    def test_search_range_in_binary_search_tree(self):
        self.assertEqual(self.obj.search_range_in_binary_search_tree(None, 1, 10), [])


    # empty tree
    def test_search_range_in_binary_search_tree_2(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        self.assertEqual(self.obj.search_range_in_binary_search_tree(root, 0, 4), [1, 2])


if __name__ == '__main__':
    unittest.main()
