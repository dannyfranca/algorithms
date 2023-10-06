class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        curr = self
        output = ""
        while curr:
            output += str(curr.value) + "->"
            curr = curr.next
        output += "NULL"
        return output


def has_cycle(head: Node) -> bool:
    """Detects if a linked list has a cycle using Floyd's Tortoise and Hare algorithm."""
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def reverse_iterative(node: Node):
    if has_cycle(node):
        raise ValueError("Linked list has a cycle. Cannot be reversed.")
    curr = node
    head = Node(curr.value)
    while curr:
        next = curr.next
        if next:
            prev = head
            head = Node(next.value, prev)
        curr = next
    return head


def reverse_iterative_mutation(node):
    if has_cycle(node):
        raise ValueError("Linked list has a cycle. Cannot be reversed.")
    prev = None
    curr = node
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def reverse_recursive(node):
    head = Node


ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(ll)
print(reverse_iterative(ll))
print(ll)
print(reverse_iterative_mutation(ll))
