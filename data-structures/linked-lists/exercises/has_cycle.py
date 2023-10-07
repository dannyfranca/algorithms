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


ll = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4))))
print(has_cycle(ll))

## Create cycle
ll.next.next.next.next = ll
print(has_cycle(ll))
