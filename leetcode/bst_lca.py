# LCA of BST.
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

def lca(root, p, q):
  if root is None:
    return None
  small = p.val if p.val < q.val else q.val
  large = p.val if p.val > q.val else q.val

  pcurr = root
  while pcurr is not None:
    if (small < pcurr.val) and (pcurr.val < large):
      return pcurr
    elif (pcurr.val == small) or (pcurr.val == large):
      return pcurr
    elif (large < pcurr.val):
      pcurr = pcurr.left
    elif (small > pcurr.val):
      pcurr = pcurr.right
    else:
      pcurr = None
  return pcurr
