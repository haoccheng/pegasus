# populate next right pointers in each node in complete binary tree.

def connect(left, right):
  if (left is None) and (right is None):
    return
  left.next = right
  if left.left is not None:
    connect(left.left, left.right)
    connect(left.right, right.left)
    connect(right.left, right.right)

def connect(root):
  if root is not None:
    connect(root.left, root.right)
