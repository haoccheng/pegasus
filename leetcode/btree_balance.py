# balance of btree

def tree_depth(root):
  if root is None:
    return 0
  elif (root.left is None) and (root.right is None):
    return 1
  else:
    d1 = tree_depth(root.left)
    d2 = tree_depth(root.right)
    if (d1 < 0) or (d2 < 0):
      return -1
    else:
      diff = d1 - d2 if d1 >= d2 else d2 - d1
      if diff <= 1:
        return max(d1, d2) + 1
      else:
        return -1

