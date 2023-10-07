from node import LinkedList
from has_cycle import has_cycle


def reverse_iterative_clone(node: LinkedList):
    if has_cycle(node):
        raise ValueError("Linked list has a cycle. Cannot be reversed.")
    head = LinkedList(node.value)
    curr = node.next
    while curr:
        head = LinkedList(curr.value, head)
        curr = curr.next
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


def reverse_recursive(node, prev=None):
    next_node = node.next
    node.next = prev
    if next_node:
        return reverse_recursive(next_node, node)
    return node


ll = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))
print(ll)
print(reverse_iterative_clone(ll))
print(ll)
print(reverse_iterative_mutation(ll))

ll = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5)))))
print(ll)
print(reverse_recursive(ll))
