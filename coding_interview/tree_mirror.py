# Given a binary tree, how to get its mirrored tree?

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = Node(left) if left is not None else None
    self.right = Node(right) if right is not None else None

  def str(self):
    ret = []
    ret.append(self.value)
    if self.left is not None:
      ret += self.left.str()
    if self.right is not None:
      ret += self.right.str()
    return ret

  def mirror(self):
    prev_left = self.left
    if prev_left is not None:
      prev_left.mirror()
    prev_right = self.right
    if prev_right is not None:
      prev_right.mirror()
    self.left = prev_right
    self.right = prev_left

def test():
  root = Node(8)
  root.left = Node(6, 5, 7)
  root.right = Node(10, 9, 11)
  print root.str()
  root.mirror()
  print root.str()

test()

