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
