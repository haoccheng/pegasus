# print a binary tree from top level to bottom level.
# print nodes at the same level from left to right.

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = Node(left) if left is not None else None
    self.right = Node(right) if right is not None else None

  def bft(root):
    queue = []
    queue.append(root)
    ret = []
    while (len(queue) > 0):
      head = queue[0]
      ret.append(head.value)
      if head.left is not None:
        queue.append(head.left)
      if head.right is not None:
        queue.append(head.right)
      queue.pop(0)
    return ret
  bft = staticmethod(bft)

def test():
  root = Node(8)
  l = Node(6, 5, 7)
  r = Node(10, 9, 11)
  root.left = l
  root.right = r
  print Node.bft(root)

test()
