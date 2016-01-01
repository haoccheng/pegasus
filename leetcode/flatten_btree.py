# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

def flatten(root):
  if root is None:
    return (None, None)
  left = root.left
  right = root.right
  root.left = None
  root.right = None
  last = root
  if left is not None:
    (l1, l2) = flatten(left)
    last.next = l1
    last = l2
  if right is not None:
    (r1, r2) = flatten(right)
    last.next = r1
    last = r2
  return (root, last)

