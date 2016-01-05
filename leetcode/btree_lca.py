# lowest common ancestor of Btree.

def lca_base(root, p, q):
  if root is None:
    return 0
  score = 0
  if (root == p):
    score = 1
  elif (root == q):
    score == 2
  score_left = lca_base(root.left, p, q)
  score_right = lca_base(root.right, p, q)
  if not isinstance(score_left, int):
    return score_left
  if not isinstance(score_right, int):
    return score_right
  score += score_left
  score += score_right
  if score == 3:
    return root
  else:
    return score

def lca(root, p, q):
  ret = lca_base(root, p, q)
  if isinstance(ret, int):
    return None
  else:
    return ret

