# tags: hash_map
from collections import defaultdict
import unittest


class Solution(object):
    def canSpell(self, magazine, note):
        letters = defaultdict(int)
        for c in magazine:
            letters[c] += 1

        for c in note:
            if letters[c] <= 0:
                return False
            letters[c] -= 1

        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_can_spell_true(self):
        self.assertTrue(self.solution.canSpell(["a", "b", "c", "d", "e", "f"], "bed"))

    def test_can_spell_false(self):
        self.assertFalse(self.solution.canSpell(["a", "b", "c", "d", "e", "f"], "cat"))


if __name__ == "__main__":
    unittest.main()
