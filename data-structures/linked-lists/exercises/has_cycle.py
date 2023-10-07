from node import LinkedList


def has_cycle(head: LinkedList):
    """Detects if a linked list has a cycle using Floyd's Tortoise and Hare algorithm."""
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
