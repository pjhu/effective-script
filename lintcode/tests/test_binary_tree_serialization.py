import unittest
from lintcode.binary_tree_serialization import BinaryTreeSerialization
from lintcode.binary_tree_serialization import TreeNode


class BinaryTreeSerializationTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = BinaryTreeSerialization()

    def tearDown(self):
        del self.obj

    # {1,2,3}
    def test_binary_tree_serialization_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        serialize = self.obj.serialize(root)
        deserialize = self.obj.deserialize(serialize)
        self.assertEqual(serialize, '1,2,3')
        self.assertEqual(deserialize.val, 1)
        self.assertEqual(deserialize.left.val, 2)
        self.assertEqual(deserialize.right.val, 3)

    # {1,2,3,#,#,4,5} full binary tree
    def test_binary_tree_serialization_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        serialize = self.obj.serialize(root)
        deserialize = self.obj.deserialize(serialize)
        self.assertEqual(serialize, '1,2,3,#,#,4,5')
        self.assertEqual(deserialize.val, 1)
        self.assertEqual(deserialize.left.val, 2)
        self.assertEqual(deserialize.right.val, 3)
        self.assertEqual(deserialize.right.left.val, 4)
        self.assertEqual(deserialize.right.right.val, 5)

    # {1,2,#,3,#,4} not full binary tree
    def test_binary_tree_serialization_3(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        serialize = self.obj.serialize(root)
        deserialize = self.obj.deserialize(serialize)
        self.assertEqual(serialize, '1,2,#,3,#,4')
        self.assertEqual(deserialize.val, 1)
        self.assertEqual(deserialize.left.val, 2)
        self.assertEqual(deserialize.left.left.val, 3)
        self.assertEqual(deserialize.left.left.left.val, 4)

    # {} no values
    def test_binary_tree_serialization_4(self):
        root = None
        serialize = self.obj.serialize(root)
        self.assertEqual(serialize, '')
        deserialize = self.obj.deserialize(serialize)
        self.assertEqual(deserialize, None)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(BinaryTreeSerializationTestCase("test_binary_tree_serialization_3"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

