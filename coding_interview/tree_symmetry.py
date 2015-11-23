# Implement a function to verify whether a binary tree is symmetrical.
# A tree is symmetrical if its mirroed image looks the same as the tree itself.
#     8             8           8
#  6    6         6   9       6   6
# 5 7  7 5       5 7 7 5     5 7 7

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

  def symmetric_base(left, right):
    if (left is None) and (right is None):
      return True
    elif (left is not None) and (right is not None):
      if (left.value == right.value):
        c1 = Node.symmetric_base(left.left, right.right)
        c2 = Node.symmetric_base(left.right, right.left)
        if (c1 == True) and (c2 == True):
          return True
        else:
          return False
      else:
        return False
    else:
      return False
  symmetric_base = staticmethod(symmetric_base)

  def symmetric(self):
    return Node.symmetric_base(self.left, self.right)

def test():
  root = Node(8)
  root.left = Node(6, 5, 7)
  root.right = Node(6, 7, 5)
  print root.str()
  print root.symmetric()

  root = Node(8)
  root.left = Node(6, 5, 7)
  root.right = Node(9, 7, 5)
  print root.str()
  print root.symmetric()

  root = Node(8)
  root.left = Node(6, 5, 7)
  root.right = Node(9, left=7)
  print root.str()
  print root.symmetric()

test()

