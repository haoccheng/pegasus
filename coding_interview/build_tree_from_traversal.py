# build a binary tree with pre-order traversal sequence and in-order sequence.
# All elements are unique.
# pre-order {1,2,4,7,3,5,6,8} and in-order {4,7,2,1,5,3,8,6}

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = Node(left) if left is not None else None
    self.right = Node(right) if right is not None else None

  def build(pre_order, in_order):
    if len(pre_order) == 0:
      return None
    if len(pre_order) == 1: # 1 node left.
      return Node(pre_order[0])
    else:
      root_value = pre_order[0]
      root_index = in_order.index(root_value)
      left_child = in_order[:root_index]
      right_child = in_order[root_index+1:]

      left_pre_order = [e for e in pre_order if e in left_child]
      left_in_order = [e for e in in_order if e in left_child]
      right_pre_order = [e for e in pre_order if e in right_child]
      right_in_order = [e for e in in_order if e in right_child]
      l = Node.build(left_pre_order, left_in_order)
      r = Node.build(right_pre_order, right_in_order)
      root = Node(root_value)
      root.left = l
      root.right = r
      return root
  build = staticmethod(build)

  def pre_order(self):
    ret = []
    ret.append(self.value)
    if self.left is not None:
      ret += self.left.pre_order()
    if self.right is not None:
      ret += self.right.pre_order()
    return ret

  def in_order(self):
    ret = []
    if self.left is not None:
      ret += self.left.in_order()
    ret.append(self.value)
    if self.right is not None:
      ret += self.right.in_order()
    return ret

def test():
  pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
  in_order = [4, 7, 2, 1, 5, 3, 8, 6]
  root = Node.build(pre_order, in_order)
  print pre_order
  print root.pre_order()
  print in_order
  print root.in_order()

test()
