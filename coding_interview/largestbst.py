# find the largest size of BST in a given binary tree.

# recursively..

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

  def largest(self):
    if (self.left is None) and (self.right is None):
      return (True, 1, (self.name, self.name))
    else:
      lc = self.left.largest() if (self.left is not None) else None
      rc = self.right.largest() if (self.right is not None) else None
      if (lc is not None) and (rc is not None):
        (lcbst, lcsize, lcrange) = lc
        (rcbst, rcsize, rcrange) = rc
        if (lcbst == True) and (rcbst == True):
          if (self.name > lcrange[1]) and (self.name < rcrange[0]):
            return (True, lcsize+rcsize+1, (lcrange[0], rcrange[1]))
        return (False, max(lcsize, rcsize), None)
      elif (lc is not None):
        (lcbst, lcsize, lcrange) = lc
        if (lcbst == True):
          if (self.name > lcrange[1]):
            return (True, lcsize+1, (lcrange[0], self.name))
        return (False, lcsize, None)
      elif (rc is not None):
        (rcbst, rcsize, rcrange) = rc
        if (rcbst == True):
          if (self.name < rcrange[0]):
            return (True, rcsize+1, (self.name, rcrange[1]))
        return (False, rcsize, None)

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

print toy_tree().largest()
print toy_tree2().largest()

