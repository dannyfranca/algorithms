class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        curr = self
        output = ""
        while curr:
            output += str(curr.value) + "->"
            curr = curr.next
        if output.endswith("->"):
            return output[:-2]
        return output


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


ll = Node(1, Node(2, Node(6, Node(3, Node(4, Node(5, Node(6)))))))
print(ll)
print(Solution(ll).remove_elements([6]))
