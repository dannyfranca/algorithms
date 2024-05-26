# tags:
import unittest


class MaxStack(object):
    def __init__(self):
        self.stack = []
        self.maxes = []

    def push(self, val):
        self.stack.append(val)
        if self.maxes and self.maxes[-1] > val:
            self.maxes.append(self.maxes[-1])
        else:
            self.maxes.append(val)

    def pop(self):
        if self.maxes:
            self.maxes.pop()
        return self.stack.pop()

    def max(self):
        return self.maxes[-1]


class TestSolution(unittest.TestCase):
    def test_name(self):
        s = MaxStack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(2)
        self.assertEqual(s.max(), 3)
        s.pop()
        self.assertEqual(s.max(), 3)
        s.pop()
        self.assertEqual(s.max(), 2)
        s.pop()
        self.assertEqual(s.max(), 1)


if __name__ == "__main__":
    unittest.main()
