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


def reverse_iterative(node):
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
