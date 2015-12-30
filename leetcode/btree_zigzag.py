# Given a binary tree, return zigzag level order traversal (from left to right, then right to left at next level..)

def zigzag(root):
  if root is None:
    return []
  ret = []
  curr = [root]
  direction = 'LEFT'
  while len(curr) > 0:
    # add to resutl
    row = []
    if direction == 'LEFT':
      for i in range(0, len(curr), 1):
        row.append(curr[i].val)
    else:
      for i in range(len(curr)-1, -1, -1):
        row.append(curr[i].val)
    ret.append(row)
    # populate the next level
    next = []
    for n in curr:
      if n.left is not None:
        next.append(n.left)
      if n.right is not None:
        next.append(n.right)
    curr = next
    direction = 'RIGHT' if direction == 'LEFT' else 'LEFT'
  return ret
