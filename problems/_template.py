# tags:
import unittest


class Solution:
    def versionRecursive(self):
        return None

    def versionIterative(self):
        return None


class TestSolution(unittest.TestCase):
    def test_execute(self):
        # prepare
        self.assertEqual(Solution().versionIterative(), None)
        self.assertEqual(Solution().versionRecursive(), None)


if __name__ == "__main__":
    unittest.main()
