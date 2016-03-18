# 2d array. iterator.
# hasNext(), next()

# while (i.has_next()):
#   d = i.next()
#   i.remove()

class Iterator2d:
  def __init__(self, data):
    self.data = data
    self.curr_pt = None
    self.advance(0, -1)

  def advance(self, x, y):
    self.next_pt = None
    for j in range(y+1, len(self.data[x])):
      self.next_pt = (x, j)
      break
    for i in range(x+1, len(self.data)):
      if self.next_pt is not None:
        break
      for j in range(len(self.data[i])):
        self.next_pt = (i, j)
        break

  def next(self):
    self.curr_pt = self.next_pt
    self.advance(self.curr_pt[0], self.curr_pt[1])
    return self.data[self.curr_pt[0]][self.curr_pt[1]]

  def hasNext(self):
    return True if self.next_pt is not None else False

  def remove(self):
    if self.next_pt is None:
      self.data[self.curr_pt[0]].pop(self.curr_pt[1])
    else:
      if self.curr_pt[0] == self.next_pt[0]: # same row.
        self.data[self.curr_pt[0]].pop(self.curr_pt[1])
        self.next_pt = self.curr_pt
      else:
        self.data[self.curr_pt[0]].pop(self.curr_pt[1])

m = [[], [1,2,3], [], [], [4,5], [], [6,7,8,9]]
it = Iterator2d(m)
while (it.hasNext()):
  print it.next()
  it.remove()
print m
