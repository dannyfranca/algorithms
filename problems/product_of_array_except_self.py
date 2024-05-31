# tags:
import unittest


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        left_prod = 1
        for i, num in enumerate(nums):
            answer[i] *= left_prod
            left_prod *= num

        right_prod = 1
        for i, num in enumerate(reversed(nums)):
            answer[-i - 1] *= right_prod
            right_prod *= num

        return answer


class TestSolution(unittest.TestCase):
    def test_execute(self):
        # prepare
        self.assertEqual(Solution().productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])


if __name__ == "__main__":
    unittest.main()
