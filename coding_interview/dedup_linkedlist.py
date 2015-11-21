# Given a sorted linked list, delete duplicated numbers and leave only distinct numbers
# from the original list.
# [1,2,3,3,4,4,5] -> [1,2,5]

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def str(self):
    out = []
    out.append(self.value)
    if self.next is not None:
      out += self.next.str()
    return out

  def create(values):
    root = None
    curr = None
    for v in values:
      x = Node(v)
      if root is None:
        root = x
        curr = x
      elif curr is not None:
        curr.next = x
        curr = curr.next
    return root
  create = staticmethod(create)

  # in-place modification.
  def dedup(linked):
    root = None
    pcurr = linked
    new_curr = None

    while (pcurr is not None):
      hit = 0
      pnext = pcurr.next
      while (pnext is not None):
        if (pcurr.value == pnext.value):
          pnext = pnext.next
          hit = 1
        else:
          break
      if hit == 0: # no duplicate.
        pcurr.next = None
        if root is None:
          root = pcurr
          new_curr = pcurr
        else:
          new_curr.next = pcurr
          new_curr = pcurr
        pcurr = pnext
      else: # duplicate
        pcurr = pnext
    return root
  dedup = staticmethod(dedup)

def test():
  root = Node.create([1,2,3,3,4,4,5])
  print root.str()
  dedup = Node.dedup(root)
  print dedup.str()

  root = Node.create([1,1,2,2])
  print root.str()
  dedup = Node.dedup(root)
  print dedup

  root = Node.create([1,1,2,2,3])
  print root.str()
  dedup = Node.dedup(root)
  print dedup.str()

  root = Node.create([1,1,3,2,2])
  print root.str()
  dedup = Node.dedup(root)
  print dedup.str()

test()
