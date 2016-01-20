def build_tree(inorder, postorder):
  if len(inorder) == 0:
    return None
  root_value = postorder[-1]
  root = TreeNode(root_value)
  postorder.pop()
  root_index = inorder.index(root_value)
  root.right = build_tree(inorder[root_index+1:], postorder)
  root.left = build_tree(inorder[:root_index], postorder)
  return root
