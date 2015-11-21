# reverse a linked list

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

  def reverse(root):
    first = root
    rest = first.next
    if (rest is None):
      return (first, first) # head, tail.
    else:
      (rest_head, rest_tail) = Node.reverse(rest)
      first.next = None
      rest_tail.next = first
      return (rest_head, first)
  reverse = staticmethod(reverse)

  # How about if not using recursive.
  def reverse_iterative(root):
    # 1,2,3 -> 21, 3
    # 21,3,4 -> 321, 4
    # 321,4,5 -> 4321, 5
    p1 = root
    p2 = p1.next if p1.next is not None else None
    p3 = p2.next if (p2 is not None) and (p2.next is not None) else None
    p1.next = None
    while (p3 is not None):
      p2.next = p1
      p1 = p2
      p2 = p3
      p3 = p3.next
    if (p2 is not None):
      p2.next = p1
      p1 = p2
    return p1
  reverse_iterative = staticmethod(reverse_iterative)

def test():
  root = Node.create([1,2,3,4,5,6])
  print root.str()
  (rr_head, rr_tail) = Node.reverse(root)
  print rr_head.str()

  root = Node.create([1,2,3,4,5,6])
  print root.str()
  rr_head = Node.reverse_iterative(root)
  print rr_head.str()

test()
