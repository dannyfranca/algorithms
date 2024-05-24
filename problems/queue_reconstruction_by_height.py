# tags: linked_list
import unittest


class Solution:
    def reconstructQueue(self, input):
        input.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for person in input:
            res.insert(person[1], person)
        return res


class TestSolution(unittest.TestCase):
    def test_name(self):
        # prepare
        self.assertEqual(
            Solution().reconstructQueue(
                [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
            ),
            [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
        )


if __name__ == "__main__":
    unittest.main()
