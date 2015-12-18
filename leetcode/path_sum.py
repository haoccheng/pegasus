# Given a binary tree and a sum, determine if the tree has root-to-leaf path
# such that the sum of values along the path equals to the target sum.
# negative value as well..

def has_path_sum(root, sum):
  if (root is None):
    return False
  r = sum - root.val
  if (r == 0) and (root.left is None) and (root.right is None):
    return True
  else:
    lc = has_path_sum(root.left, r)
    if lc == True:
      return True
    rc = has_path_sum(root.right, r)
    if rc == True:
      return True
  return False
