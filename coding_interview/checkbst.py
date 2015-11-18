# verify whether a binary tree is a binary search tree.

class Node:
  def __init__(self, name):
    self.name = name
    self.left = None
    self.right = None

  def add_child(self, lname=None, rname=None):
    if (lname is not None):
      lc = Node(lname)
      self.left = lc
    if (rname is not None):
      rc = Node(rname)
      self.right = rc

  def inorder(self):
    # inorder: left, root, right
    ret = []
    if self.left is not None:
      ret += self.left.inorder()
    ret += [self.name]
    if self.right is not None:
      ret += self.right.inorder()
    return ret

  def check_bst(self, minv = None, maxv = None):
    # check root first.
    if (minv is not None):
      if (self.name < minv):
        return False
    if (maxv is not None):
      if (self.name > maxv):
        return False
    if (self.left is not None):
      if self.left.check_bst(minv, self.name) == False:
        return False
    if (self.right is not None):
      if self.right.check_bst(self.name, maxv) == False:
        return False
    return True

def toy_tree():
  root = Node(10)
  root.add_child(lname=6, rname=14)
  root.left.add_child(lname=4, rname=8)
  root.right.add_child(lname=12, rname=16)
  return root

def toy_tree2():
  root = Node(10)
  root.add_child(lname=6, rname=11)
  root.left.add_child(lname=4, rname=8)
  root.right.add_child(lname=12, rname=16)
  return root

root = toy_tree()
print root.inorder()
print root.check_bst()

root = toy_tree2()
print root.check_bst()

