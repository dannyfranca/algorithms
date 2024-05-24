# tags: xor
import unittest


class Solution(object):
    def singleNumber(self, nums):
        occurrence = {}

        for n in nums:
            occurrence[n] = occurrence.get(n, 0) + 1

        for key, value in occurrence.items():
            if value == 1:
                return key

    def singleNumber2(self, nums):
        unique = 0
        for n in nums:
            unique ^= n
        return unique


class TestSolution(unittest.TestCase):
    def test_name(self):
        # prepare
        self.assertEqual(Solution().singleNumber([4, 3, 2, 4, 1, 3, 2]), 1)
        self.assertEqual(Solution().singleNumber2([4, 3, 2, 4, 1, 3, 2]), 1)


if __name__ == "__main__":
    unittest.main()
