# tags:
import unittest


class Solution:
    def productExceptSelf(self, nums):
        right = [1] * len(nums)
        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            right[i] = prod

        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i - 1]
            right[i] *= prod

        return right


class TestSolution(unittest.TestCase):
    def test_execute(self):
        # prepare
        self.assertEqual(Solution().productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])


if __name__ == "__main__":
    unittest.main()
