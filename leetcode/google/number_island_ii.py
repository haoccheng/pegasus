# number of island ii
# mxn grid initially filled with water.
# perform addLand operation which turns water at position (row, col) to a land.

class IslandII:
  def __init__(self, m, n):
    self.land = []
    for i in range(m):
      row = [-1] * n
      self.land.append(row)
    self.islands = {}

  def add_land(self, x, y):
    if self.land[x][y] == -1:
      l1 = -1 if (x - 1) < 0 else self.land[x-1][y]
      l2 = -1 if (x + 1) > len(self.land)-1 else self.land[x+1][y]
      l3 = -1 if (y - 1) < 0 else self.land[x][y-1]
      l4 = -1 if (y + 1) > len(self.land[x])-1 else self.land[x][y+1]
      c1 = -1 if l1 < 0 else self.islands[l1]
      c2 = -1 if l2 < 0 else self.islands[l2]
      c3 = -1 if l3 < 0 else self.islands[l3]
      c4 = -1 if l4 < 0 else self.islands[l4]
      c = max(c1, c2, c3, c4)
      if c == -1:
        self.land[x][y] = len(self.islands)
        self.islands[self.land[x][y]] = self.land[x][y]
      else:
        self.land[x][y] = c
        if l1 >= 0:
          self.islands[l1] = c
        if l2 >= 0:
          self.islands[l2] = c
        if l3 >= 0:
          self.islands[l3] = c
        if l4 >= 0:
          self.islands[l4] = c

  def count(self):
    return len(set([v for k,v in self.islands.items()]))

island = IslandII(3, 3)
island.add_land(0, 0)
print island.count()
island.add_land(0, 1)
print island.count()
island.add_land(1, 2)
print island.count()
island.add_land(2, 1)
print island.count()
island.add_land(2, 2)
print island.count()

