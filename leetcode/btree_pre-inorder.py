def build_tree(preorder, inorder):
  if len(preorder) == 0:
    return None
  elif len(preorder) == 1:
    return TreeNode(preorder[0])
  else:
    root = preorder[0]
    inorder_root = inorder.index(root)
    left_inorder = inorder[:inorder_root]
    right_inorder = inorder[inorder_root+1:]
    left_preorder = [e for e in preorder if e in left_inorder]
    right_preorder = [e for e in preorder if e in right_inorder]
    left = build_tree(left_preorder, left_inorder)
    right = build_tree(right_preorder, right_inorder)
    r = TreeNode(root)
    r.left = left
    r.right = right
    return r

