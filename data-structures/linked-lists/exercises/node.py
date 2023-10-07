from weakref import WeakKeyDictionary


class LinkedList:
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


class LinkedListWithCycle:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        curr = self
        output = ""
        read_dict = WeakKeyDictionary()
        while curr:
            if read_dict.get(curr):
                output += "(" + str(curr.value) + "...)"
                break
            output += str(curr.value) + "->"
            read_dict[curr] = True
            curr = curr.next
        if output.endswith("->"):
            return output[:-2]
        return output
