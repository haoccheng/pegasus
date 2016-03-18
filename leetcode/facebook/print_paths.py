# print all paths in the tree from root to leave

def tree(root, prefix):
  prefix.append(root.val)
  if root.left is None and root.right is None:
    print prefix
  if root.left is not None:
    tree(root.left, prefix)
  if root.right is not None:
    tree(root.right, prefix)
  prefix.pop()
