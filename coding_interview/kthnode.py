# implement a function to get the kth node from tail of a single linked list.
# [1,2,3,4,5,6] -> 3rd node from tail -> node 4.

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def create(values):
    root = None
    curr = None
    for v in values:
      n = Node(v)
      if root is None:
        root = n
        curr = n
      else:
        curr.next = n
        curr = curr.next
    return root
  create = staticmethod(create)

  def str(self):
    ret = []
    ret.append(self.value)
    if self.next is not None:
      ret += self.next.str()
    return ret

  def kth(root, k):
    curr = root
    next = root
    for i in range(k):
      if next.next is not None:
        next = next.next
      else:
        return None
    while (next is not None):
      curr = curr.next
      next = next.next
    return curr
  kth = staticmethod(kth)

def test():
  root = Node.create([1,2,3,4,5,6])
  print root.str()
  k = Node.kth(root, 3)
  print k.value

test()
