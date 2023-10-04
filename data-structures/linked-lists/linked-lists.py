class Node(object):
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    curr = self
    output = ''
    while curr:
      output += str(curr.value)
      curr = curr.next
    return output
  
def listToLinkedList(nums):
  head = None
  curr = None
  for n in nums:
    new_node = Node(n)
    if not head:
      head = new_node
    else:
      curr.next = new_node
    curr = new_node
  return head
  

ll = Node(1, Node(2, Node(3)))
print(ll)
print(listToLinkedList([1, 2, 3, 4, 5]))
