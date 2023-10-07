from node import LinkedList, LinkedListWithCycle


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


def create_cycle(head: LinkedList | LinkedListWithCycle):
    if has_cycle(head):
        return head
    curr = head
    while curr:
        if not curr.next:
            curr.next = head
            break
        curr = curr.next
    return head
