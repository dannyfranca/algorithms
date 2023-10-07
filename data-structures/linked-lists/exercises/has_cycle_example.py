from node import LinkedListWithCycle
from has_cycle import has_cycle, create_cycle


ll = LinkedListWithCycle(
    1, LinkedListWithCycle(2, LinkedListWithCycle(3, LinkedListWithCycle(4)))
)
print(has_cycle(ll))
print(ll)

# Create cycle
create_cycle(ll)
print(has_cycle(ll))
print(ll)
