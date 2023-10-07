from node import LinkedList


class Solution:
    def __init__(self, head):
        self.head = head

    def remove_elements(self, values):
        self.curr = self.head
        self.prev = None
        values_dict = dict.fromkeys(values, True)
        while self.curr:
            if values_dict.get(self.curr.value):
                self._remove_current_element()
            else:
                self.prev = self.curr
            self.curr = self.curr.next
        return self.head

    def _remove_current_element(self):
        next_node = self.curr.next
        if self.prev:
            self.prev.next = next_node
        if self.head == self.curr:
            self.head = next_node


ll = LinkedList(
    1,
    LinkedList(
        2, LinkedList(6, LinkedList(3, LinkedList(4, LinkedList(5, LinkedList(6)))))
    ),
)
print(ll)
print(Solution(ll).remove_elements([6]))
