# tags:
import unittest


def findPythagoreanTriplets(nums):
    for a in nums:
        for b in nums:
            for c in nums:
                if a * a + b * b == c * c:
                    return True
    return False


def findPythagoreanTriplets2(nums):
    squares = set([n * n for n in nums])

    for a in nums:
        for b in nums:
            if a * a + b * b in squares:
                return True
    return False


class TestSolution(unittest.TestCase):
    def test_name(self):
        # prepare
        self.assertEqual(findPythagoreanTriplets([3, 5, 12, 5, 13]), True)
        self.assertEqual(findPythagoreanTriplets2([3, 5, 12, 5, 13]), True)


if __name__ == "__main__":
    unittest.main()
