# Given a binary tree and target sum, find all root-to-leaf paths where path's sum equal to target.

def path_sum_base(root, accsum, path, target):
  if (root.left is None) and (root.right is None):
    if (accsum + root.val) == target:
      ret = []
      ret.append(path + [root.val])
      return ret
    else:
      return []
  else:
    ret = []
    accsum = accsum + root.val
    path.append(root.val)
    if root.left is not None:
      ret += path_sum_base(root.left, accsum, path, target)
    if root.right is not None:
      ret += path_sum_base(root.right, accsum, path, target)
    path.pop()
    return ret

def path_sum(root, target):
  if root is None:
    return []
  path = []
  accsum = 0
  return path_sum_base(root, accsum, path, target)
