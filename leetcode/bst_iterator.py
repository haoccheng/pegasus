# https://leetcode.com/problems/binary-search-tree-iterator/
# iterator for BST
# initialize at root of BST.

class BSTIterator:
  def __init__(self, root):
    self.stack = []
    if root.left is not None:
      self.stack.append((root.left, 'node'))

  def has_next(self):
    return True if len(self.stack) > 0 else False

  def push(self, root):
    if root.left is not None:
      self.stack.append((root.left, 'node'))
    self.stack.append((root, 'value'))
    if root.right is not None:
      self.push(root.right)

  def next(self):
    top = self.stack.pop()
    while (top[1] == 'node'):
      self.push(top[0])
      top = self.stack.pop()
    return top[0].val

