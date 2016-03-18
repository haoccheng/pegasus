# quadtree structure
# struct QuadNode {
#   QuadNode(int num_ones=0): ones(num_ones){}
#   int ones{ 0 }
#   QuadNode* child[4]{ null }
# }
# build a quadtree to represent 0/1 matrix.
# assume matrix is square and dimension is power of 2.
# Given two quadtree with same depth, write a function to calculate how many 1s are overlapped.

class QuadNode:
  def __init__(self, ones=0):
    self.ones = ones
    self.child = [None] * 4

  def update(self):
    if self.child[0] is not None:
      for i in range(len(self.child)):
        self.child[i].update()
      self.ones = sum([self.child[i].ones for i in range(len(self.child))])

  def overlap(qt1, qt2):
    if qt1.ones == 0 or qt2.ones == 0:
      return 0
    if qt1.child[0] is None: # leaf
      if qt1.ones == 1 and qt2.ones == 1:
        return 1
      else:
        return 0
    else:
      return sum([QuadNode.overlap(qt1.child[i], qt2.child[i]) for i in range(4)])
  overlap = staticmethod(overlap)

x = QuadNode()
x.child[0] = QuadNode(0)
x.child[1] = QuadNode(1)
x.child[2] = QuadNode(1)
x.child[3] = QuadNode(1)
x.update()
print x.ones

y = QuadNode()
y.child[0] = QuadNode(0)
y.child[1] = QuadNode(0)
y.child[2] = QuadNode(1)
y.child[3] = QuadNode(1)
y.update()
print y.ones

print QuadNode.overlap(x, y)
