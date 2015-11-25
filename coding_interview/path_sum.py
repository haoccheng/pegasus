# Given a binary tree and an integer value, print all paths where the sum of node values equal to given integer.
# All nodes from root to leaf compose a path.

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = Node(left) if left is not None else None
    self.right = Node(right) if right is not None else None

  def is_leaf(self):
    return (self.left is None) and (self.right is None)

  def path_sum(self, value):
    if self.is_leaf():
      if (self.value == value):
        return [[self.value]]
      else:
        return []
    else:
      if (value > self.value):
        ret = []
        if (self.left is not None):
          ret = ret + self.left.path_sum(value - self.value)
        if (self.right is not None):
          ret = ret + self.right.path_sum(value - self.value)
        if len(ret) > 0:
          return [[self.value] + e for e in ret]
      else:
        return []

def test():
  root = Node(10)
  l = Node(5, 4, 7)
  r = Node(12)
  root.left = l
  root.right = r
  print root.path_sum(22)

test()
