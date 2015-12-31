# https://leetcode.com/problems/binary-tree-right-side-view/
# right side view of the binary tree from top to bottom.

def right_side_view(root):
  if root is None:
    return []
  ret = []
  curr = [root]
  while (len(curr) > 0):
    ret.append(curr[-1].val)
    next = []
    for c in curr:
      if c.left is not None:
        next.append(c.left)
      if c.right is not None:
        next.append(c.right)
    curr = next
  return ret
