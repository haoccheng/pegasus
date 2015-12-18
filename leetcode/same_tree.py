# same binary tree.

def is_same_tree(p, q):
  if (p is None) and (q is None):
    return True
  elif (p is None) or (q is None):
    return False
  else:
    if p.val != q.val:
      return False
    if is_same_tree(p.left, q.left) == False:
      return False
    if is_same_tree(p.right, q.right) == False:
      return False
    return True

