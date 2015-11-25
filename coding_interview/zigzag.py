# print a binary tree by level in zigzag order.
# each level in a line.
# level 1: left to right; level 2: right to left; level 3: left to right ..

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = Node(left) if left is not None else None
    self.right = Node(right) if right is not None else None

  def zigzag(root):
    curr_level = []
    next_level = []
    curr_level.append(root)
    curr = 0
    while (len(curr_level) > 0):
      for e in curr_level:
        if e.left is not None:
          next_level.append(e.left)
        if e.right is not None:
          next_level.append(e.right)
      if curr % 2 == 0: # left -> right
        for i in range(len(curr_level)):
          print ' %d' % (curr_level[i].value),
        print
      else:
        for i in range(len(curr_level)-1, -1, -1):
          print ' %d' % (curr_level[i].value),
        print
      curr += 1
      curr_level = next_level
      next_level = []
  zigzag = staticmethod(zigzag)

def test():
  root = Node(8)
  l = Node(6, 5, 7)
  r = Node(10, 9, 11)
  root.left = l
  root.right = r
  Node.zigzag(root)

test()
