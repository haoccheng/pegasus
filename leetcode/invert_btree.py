# invert btree

def invert_btree(root):
  if root is None:
    return None
  else:
    left = invert_btree(root.left)
    right = invert_btree(root.right)
    root.right = left
    root.left = right
    return root
