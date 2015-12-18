# valid BST.

def is_valid_bst_base(root):
  if root is None:
    return (True, None, None)
  else:
    (valid_left, min_left, max_left) = is_valid_bst_base(root.left)
    (valid_right, min_right, max_right) = is_valid_bst_base(root.right)
    if (valid_left == False) or (valid_right == False):
      return (False, None, None)
    else:
      if max_left is not None:
        if max_left >= root.val:
          return (False, None, None)
      if min_right is not None:
        if min_right <= root.val:
          return (False, None, None)
      min_left = root.val if min_left is None else min_left
      max_right = root.val if max_right is None else max_right
      return (True, min_left, max_right)

 
