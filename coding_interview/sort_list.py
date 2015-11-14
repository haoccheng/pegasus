# implement a function to sort a given list.

# O(n2): each iteration locate the element that should have been placed in the specific position, swap.

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next = next_node

  def take(self):
    buffer = [self.value]
    if self.next is not None:
      buffer += self.next.take()
    return buffer

def create_linked_list():
  w = Node(3)
  x = Node(4)
  y = Node(2)
  z = Node(1)
  w.next = x
  x.next = y
  y.next = z
  return w

def sort_list(input):
  root = input
  curr = input
  while (curr is not None):
    min_v = curr.value
    min_p = curr
    pt = curr.next
    while (pt is not None):
      if (min_v > pt.value):
        min_v = pt.value
        min_p = pt
      pt = pt.next
    t = curr.value
    curr.value = min_v
    min_p.value = t
    curr = curr.next
  return root

input = create_linked_list()
print input.take()
sort = sort_list(input)
print sort.take()

