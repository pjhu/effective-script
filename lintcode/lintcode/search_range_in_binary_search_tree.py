# -*- utf-8 -*-
"""
eleventh
http://www.lintcode.com/en/problem/search-range-in-binary-search-tree/
"""
import profile
import queue


# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class SearchRangeInBinarySearchTree(object):
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """
    def search_range_in_binary_search_tree(self, root, k1, k2):
        if not root:
            return []
        q = queue.Queue()
        q.put(root)
        l = []
        if k1 <= root.val <= k2:
            l.append(root.val)
        while not q.empty():
            node = q.get()
            if node.left:
                q.put(node.left)
                if k1 <= node.left.val <= k2:
                    l.append(node.left.val)
            if node.right:
                q.put(node.right)
                if k1 <= node.right.val <= k2:
                    l.append(node.right.val)
        return sorted(l)

if __name__ == '__name__':
    obj = SearchRangeInBinarySearchTree()
    root = TreeNode(1)
    print(profile.run("obj.search_range_in_binary_search_tree(root, 1, 10)"))
