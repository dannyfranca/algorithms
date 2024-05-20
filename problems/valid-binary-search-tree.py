# tags: binary_tree
import unittest


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def _isValidBSTHelper(self, n, low, high):
        if not n:
            return True
        val = n.val
        if (
            (val > low and val < high)
            and self._isValidBSTHelper(n.left, low, n.val)
            and self._isValidBSTHelper(n.right, n.val, high)
        ):
            return True
        return False

    def isValidBST(self, n):
        return self._isValidBSTHelper(n, float("-inf"), float("inf"))


class TestSolution(unittest.TestCase):
    def test_is_valid_bst_true(self):
        node = Node(5)
        node.left = Node(4)
        node.right = Node(7)
        self.assertTrue(Solution().isValidBST(node))

    def test_is_valid_bst_false(self):
        node = Node(5)
        node.left = Node(4)
        node.right = Node(7)
        node.right.left = Node(2)
        self.assertFalse(Solution().isValidBST(node))


if __name__ == "__main__":
    unittest.main()
