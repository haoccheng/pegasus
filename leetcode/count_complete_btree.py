# https://leetcode.com/problems/count-complete-tree-nodes/

import math

def count_btree(root):
  if root is None:
    return 0
  curr = [root]
  depth = 0
  while len(curr) > 0:
    if curr[0].left is None and curr[0].right is None:
      break
    else:
      depth += 1
      next = []
      for c in curr:
        if c.left is not None:
          next.append(c.left)
        if c.right is not None:
          next.append(c.right)
      curr = next
  count = (int)(math.pow(2, depth)) + len(curr)
  return count
