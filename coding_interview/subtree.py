# Given two binary tree, check whether one is a substructure of the other.
#     8           8
#  8     7   ->  9 2  -> True.
#9   2
#   4 7

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = Node(left) if left is not None else None
    self.right = Node(right) if right is not None else None

  def subtree(root1, root2):
    if (root1.value == root2.value):
      if Node.check_subtree(root1, root2):
        return True
    if root1.left is not None:
      if Node.subtree(root1.left, root2):
        return True
    if root1.right is not None:
      if Node.subtree(root1.right, root2):
        return True
    return False
  subtree = staticmethod(subtree)

  def check_subtree(root1, root2):
    if (root1.value == root2.value):
      if (root2.left is not None):
        if (root1.left is None):
          return False
        else:
          if Node.check_subtree(root1.left, root2.left) == False:
            return False
      if (root2.right is not None):
        if (root1.right is None):
          return False
        else:
          if Node.check_subtree(root1.right, root2.right) == False:
            return False
      return True
    else:
      return False
  check_subtree = staticmethod(check_subtree)

def test():
  r1 = Node(8, 8, 7)
  r1.left.left = Node(9)
  x = Node(2, 4, 7)
  r1.left.right = x
  r2 = Node(8, 9, 2)
  print Node.subtree(r1, r2)

  r3 = Node(8, 8, 7)
  r3.left.left = Node(10)
  x = Node(2, 4, 7)
  r3.left.right = x
  r4 = Node(8, 9, 2)
  print Node.subtree(r3, r4)

test()
