# Given a node in a binary tree, implement a function to retrieve its next node in
# the in-order traversal sequence. There is a pointer to the parent node in each node.

class Node:
  def __init__(self, name):
    self.name = name
    self.left = None
    self.right = None
    self.parent = None

  def add_child(self, lname=None, rname=None):
    if (lname is not None):
      lc = Node(lname)
      lc.parent = self
      self.left = lc
    if (rname is not None):
      rc = Node(rname)
      rc.parent = self
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

  def leftmost(self):
    if self.left is None:
      return self
    else:
      return self.left.leftmost()

  # at each point, be aware that which direction it recurisvely climb up.
  def inorder_next(self, prev=None):
    if (self.parent is None):
      if prev == 'LEFT':
        return self
      elif prev == 'RIGHT':
        return None
      elif self.right is not None:
        return self.right.leftmost()
      else:
        return None
    else:
      leftright = 'LEFT' if (self.parent.left == self) else 'RIGHT'
      if prev == 'LEFT':
        return self
      elif prev == 'RIGHT':
        return self.parent.inorder_next(leftright)
      else: # prev=None
        if (self.right is not None):
          return self.right.leftmost()
        return self.parent.inorder_next(leftright)

def toy_tree():
  root = Node('a')
  root.add_child(lname='b', rname='c')
  root.left.add_child(lname='d', rname='e')
  root.right.add_child(lname='f', rname='g')
  root.left.right.add_child(lname='h', rname='i')
  return root

root = toy_tree()
print root.inorder()
p = root; print p.name, p.inorder_next().name
p = root.left; print p.name, p.inorder_next().name
p = root.right; print p.name, p.inorder_next().name
p = root.left.right.right; print p.name, p.inorder_next().name
p = root.right.right; print p.name, p.inorder_next()
