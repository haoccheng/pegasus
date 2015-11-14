# implement a function to merge two sorted lists.

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next = next_node

  def take(self):
    buffer = [self.value]
    if self.next is not None:
      buffer += self.next.take()
    return buffer

  def create_linked_list(values):
    root = None
    curr = None
    for v in values:
      n = Node(v)
      if root is None:
        root = n
        curr = n
      else:
        curr.next = n
        curr = n
    return root
  create_linked_list = staticmethod(create_linked_list)

  def merge(node1, node2):
    root = None
    curr = None
    pt1 = node1
    pt2 = node2
    while (pt1 is not None) and (pt2 is not None):
      if (pt1.value < pt2.value):
        if root is None:
          root = pt1
          curr = root
        else:
          curr.next = pt1
          curr = pt1
        pt1 = pt1.next
      else:
        if root is None:
          root = pt2
          curr = root
        else:
          curr.next = pt2
          curr = pt2
        pt2 = pt2.next
    if pt1 is not None:
      curr.next = pt1
    if pt2 is not None:
      curr.next = pt2
    return root
  merge = staticmethod(merge)

def test1():
  x = Node.create_linked_list([1, 3, 5, 7])
  y = Node.create_linked_list([2, 4, 8, 10])
  z = Node.merge(x, y)
  print z.take()

def test2():
  x = Node.create_linked_list([100, 200, 300, 400])
  y = Node.create_linked_list([1, 2, 3, 4])
  z = Node.merge(x, y)
  print z.take()

def test3():
  x = Node.create_linked_list([100, 200])
  y = Node.create_linked_list([110, 120, 190])
  z = Node.merge(x, y)
  print z.take()

test1()
test2()
test3()

