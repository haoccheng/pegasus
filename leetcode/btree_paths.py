# Given a binary tree, return root-to-leaf paths.
# https://leetcode.com/problems/binary-tree-paths/

def btree_paths_base(root, path):
  ret = []
  if (root.left is None) and (root.right is None):
    p = path + [str(root.val)]
    ret.append('->'.join(p))
  else:
    path = path.append(str(root.val))
    if root.left is not None:
      ret += btree_paths_base(root.left, path)
    if root.right is not None:
      ret += btree_paths_base(root.right, path)
    path.pop()
  return ret

def btree_path(root):
  if root is None:
    return []
  path = []
  return btree_paths_base(root, path)
