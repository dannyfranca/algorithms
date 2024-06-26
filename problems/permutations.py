import unittest


# tags: brute_force
class Solution(object):
    def _permuteHelper(self, nums, start=0):
        if start == len(nums) - 1:
            return [nums[:]]

        result = []
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            result += self._permuteHelper(nums, start + 1)
            nums[start], nums[i] = nums[i], nums[start]
        return result

    def permute(self, nums):
        return self._permuteHelper(nums)

    def permute2(self, nums, values=[]):
        if not nums:
            return [values]
        result = []
        for i in range(len(nums)):
            result += self.permute2(nums[:i] + nums[i + 1 :], values + [nums[i]])
        return result

    def permute2Iterative(self, nums):
        results = []
        stack = [(nums, [])]
        while len(stack):
            nums, values = stack.pop()
            if not nums:
                results += [values]
            for i in range(len(nums)):
                stack.append((nums[:i] + nums[i + 1 :], values + [nums[i]]))
        return results


print(Solution().permute([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

print(Solution().permute2([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

print(Solution().permute2Iterative([1, 2, 3]))
# [[3, 2, 1], [3, 1, 2], [2, 3, 1], [2, 1, 3], [1, 3, 2], [1, 2, 3]]


class TestSolution(unittest.TestCase):
    def permute(self):
        self.assertEqual(
            Solution().permute([1, 2, 3]),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]],
        )
        self.assertEqual(
            Solution().permute2([1, 2, 3]),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]],
        )
        self.assertEqual(
            Solution().permute2Iterative([1, 2, 3]),
            [[3, 2, 1], [3, 1, 2], [2, 3, 1], [2, 1, 3], [1, 3, 2], [1, 2, 3]],
        )
