# tags: hash_map
import unittest


class Solution(object):
    def twoSum(self, nums, target):
        for i1, a in enumerate(nums):
            for i2, b in enumerate(nums):
                if a == b:
                    continue
                if a + b == target:
                    return [i1, i2]
        return []

    def twoSumB(self, nums, target):
        values = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in values:
                return [values[diff], i]
            values[num] = i
        return []


class TestSolution(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 18), [1, 2])
        self.assertEqual(Solution().twoSumB([2, 7, 11, 15], 18), [1, 2])


if __name__ == "__main__":
    unittest.main()
