from node import Node


def has_cycle(head: Node):
    """Detects if a linked list has a cycle using Floyd's Tortoise and Hare algorithm."""
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


ll = Node(1, Node(2, Node(3, Node(4))))
print(has_cycle(ll))

## Create cycle
ll.next.next.next.next = ll
print(has_cycle(ll))
