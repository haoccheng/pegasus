# binary tree preorder traversal
# iterative solution.

def preorder_traversal(root):
  if root is None:
    return []
  stack = [root]
  ret = []
  while (len(stack)) > 0:
    node = stack[0]
    stack.pop(0)
    ret.append(node.val)
    if node.right is not None:
      stack.insert(0, node.right)
    if node.left is not None:
      stack.insert(0, node.left)
  return ret



