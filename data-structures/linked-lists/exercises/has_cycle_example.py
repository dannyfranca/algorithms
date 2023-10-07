from node import LinkedListWithCycle
from has_cycle import has_cycle


ll = LinkedListWithCycle(
    1, LinkedListWithCycle(2, LinkedListWithCycle(3, LinkedListWithCycle(4)))
)
print(has_cycle(ll))

# Create cycle
ll.next.next.next.next = ll
print(has_cycle(ll))

# Print cycle
print(ll)
