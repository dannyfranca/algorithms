from node import LinkedListWithCycle
from has_cycle import create_cycle
from weakref import WeakKeyDictionary


class Solution:
    def remove_elements(self, node, values):
        head = node
        prev = None
        curr = node
        read_dict = WeakKeyDictionary()
        values_dict = dict.fromkeys(values, True)
        while curr:
            next_node = curr.next
            if read_dict.get(curr):
                break
            if values_dict.get(curr.value):
                if curr == head:
                    head = next_node
                if prev:
                    prev.next = next_node
            else:
                prev = curr
            read_dict[curr] = True
            curr = curr.next
        return head


def create_linked_list():
    return LinkedListWithCycle(
        1,
        LinkedListWithCycle(
            2,
            LinkedListWithCycle(
                6,
                LinkedListWithCycle(
                    3,
                    LinkedListWithCycle(
                        4, LinkedListWithCycle(5, LinkedListWithCycle(6))
                    ),
                ),
            ),
        ),
    )


ll = create_linked_list()

print("Remove element:")
print(ll)
print(Solution().remove_elements(ll, [6]))

print("\nWith cycle:")
ll = create_cycle(create_linked_list())
print(ll)
print(Solution().remove_elements(ll, [6]))

print("\nRemove first element in a cycle:")
ll = create_cycle(create_linked_list())
print(ll)
print(Solution().remove_elements(ll, [1, 6]))
