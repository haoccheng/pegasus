# convert a binary search tree into a sorted double-linked list without creating new nodes.

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = Node(left) if left is not None else None
    self.right = Node(right) if right is not None else None
    self.prev = None
    self.next = None

  def build_list(self):
    head = None
    tail = None
    if self.left is not None:
      (left_head, left_tail) = self.left.build_list()
      head = left_head
      left_tail.next = self
      self.prev = left_tail
      tail = self
    else:
      head = self
      tail = self
    if self.right is not None:
      (right_head, right_tail) = self.right.build_list()
      tail.next = right_head
      right_head.prev = tail
      tail = right_tail
    return (head, tail)

  def next_order(self):
    ret = []
    ret.append(self.value)
    if self.next is not None:
      ret += self.next.next_order()
    return ret

  def prev_order(self):
    ret = []
    ret.append(self.value)
    if self.prev is not None:
      ret += self.prev.prev_order()
    return ret

def test():
  root = Node(5)
  x = Node(4, 2)
  y = Node(8, 6, 9)
  root.left = x
  root.right = y
  (head, tail) = root.build_list()
  print head.next_order()
  print tail.prev_order()

test()
