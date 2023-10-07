from has_cycle import has_cycle


ll = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4))))
print(has_cycle(ll))

## Create cycle
ll.next.next.next.next = ll
print(has_cycle(ll))
