# compare if a tree is symmetric.

def is_symmetic_base(left, right):
  if (left is None) and (right is None):
    return True
  elif (left is None) or (right is None):
    return False
  else:
    if (left.val != right.val):
      return False
    c1 = is_symmetic_base(left.left, right.right)
    c2 = is_symmetic_base(left.right, right.left)
    if (c1 == False) or (c2 == False):
      return False
    return True

def is_symmetric(root):
  if root is None:
    return True
  return is_symmetic_base(root.left, root.right)
