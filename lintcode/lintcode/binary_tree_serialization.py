# -*- utf-8 -*-
"""
seventh
http://www.lintcode.com/en/problem/binary-tree-serialization/
"""
import queue


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class BinaryTreeSerialization:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, tree_root):
        # write your code here
        if not tree_root:
            return ''
        l = []
        q = queue.Queue(0)
        q.put(tree_root)
        l.append(str(tree_root.val))
        while not q.empty():
            node = q.get()
            if node.left:
                q.put(node.left)
                l.append(str(node.left.val))
            else:
                l.append('#')
            if node.right:
                q.put(node.right)
                l.append(str(node.right.val))
            else:
                l.append('#')
        return ','.join(l).strip(',#')

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        if not data:
            return None
        tree_data = data.split(',')
        q = queue.Queue()
        node_root = TreeNode(int(tree_data[0]))
        is_left_child = True
        node_parent = node_root
        for i in tree_data[1:]:
            if i != '#':
                node = TreeNode(int(i))
                if is_left_child:
                    node_parent.left = node
                    q.put_nowait(node_parent.left)
                else:
                    node_parent.right = node
                    q.put_nowait(node_parent.right)
            if not is_left_child:
                node_parent = q.get_nowait()
            is_left_child = not is_left_child
        return node_root

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    obj = BinaryTreeSerialization()
    serialize = obj.serialize(root)
    print(serialize)
    deserialize = obj.deserialize(serialize)
    print(deserialize.right.val)
