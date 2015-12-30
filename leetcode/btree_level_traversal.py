# Given a binary tree, return bottom-up level order traversal.

def level_order_bottom(root):
  if root is None:
    return []
  ret = []
  curr = [root]
  while len(curr) > 0:
    row = []
    next = []
    for node in curr:
      row.append(node.val)
      if node.left is not None:
        next.append(node.left)
      if node.right is not None:
        next.append(node.right)
    curr = next
    ret.insert(0, row)
  return ret
