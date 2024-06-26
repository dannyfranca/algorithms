# tags: linked_list
import unittest


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __str__(self):
        n = self
        answer = ""
        while n:
            answer += str(n.val)
            n = n.next
        return answer


def remove_kth_from_linked_list(node, k):
    slow, fast = node, node
    for i in range(k):
        fast = fast.next
    if not fast:
        return node.next

    prev = None
    while fast:
        prev = slow
        fast = fast.next
        slow = slow.next
    prev.next = slow.next
    return node


class TestSolution(unittest.TestCase):
    def test_execute(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
        self.assertEqual(head, 12345)
        self.assertEqual(remove_kth_from_linked_list(head, 1), 1234)


if __name__ == "__main__":
    unittest.main()
