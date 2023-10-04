class LinkedListNode<T> {
  constructor(public value: T, public next?: LinkedListNode<T>) {}

  toString = () => {
    let curr: LinkedListNode<T> | undefined = this
    let output = ''
    do {
      if (curr?.value) output += String(curr?.value)
      curr = curr?.next
    } while (curr)

    return output
  }
}

const arrayToLinkedList = <T>(arr: T[]) => {
  let head: LinkedListNode<T> | undefined
  let curr: LinkedListNode<T>

  for (const n of arr) {
    const newNode = new LinkedListNode(n)
    if (!head) {
      head = newNode
    } else {
      curr!.next = newNode
    }
    curr = newNode
  }

  return head
}

const ll = new LinkedListNode(1, new LinkedListNode(2, new LinkedListNode(3)))
console.log(ll.toString())
console.log(String(arrayToLinkedList([1, 2, 3, 4, 5])).toString())
