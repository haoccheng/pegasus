# binary tree post-order traversal.
# iterative solution

def postorder_traversal(root):
  if root is None:
    return []
  ret = [root]
  while (True):
    start = None
    for i in range(len(ret)):
      if not isinstance(ret[i], int):
        start = i
        break
    if start is None:
      break
    node = ret[start]
    ret[start] = node.val
    if node.right is not None:
      ret.insert(start, node.right)
    if node.left is not None:
      ret.insert(start, node.left)
  return ret

