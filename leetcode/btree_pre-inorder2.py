# build binary tree from preorder/inorder traversal sequences.

def build_base(preorder, inorder):
  if len(preorder) == 0:
    return None
  elif len(preorder) == 1:
    return TreeNode(preorder[0])
  root_value = preorder[0]
  root_index = inorder.index(root_value)
  root = TreeNode(root_value)
  preorder.pop(0)
  inorder_left = inorder[:root_index]
  inorder_right = inorder[root_index+1:]
  next_value = preorder[0]
  if len(inorder_left) > 0 and next_value in inorder_left:
    root.left = build_base(preorder, inorder_left)
  if len(preorder) == 0:
    return root
  next_value = preorder[0]
  if len(inorder_right) > 0 and next_value in inorder_right:
    root.right = build_base(preorder, inorder_right)
  return root

