# design nxn matrix.
# setValue, getRowSum, getMatrixSum

class Matrix:
  def __init__(self, N):
    self.data = []
    for i in range(N):
      row = [0] * N
      self.data.append(row)
    self.rowsum = [0] * N
    self.matsum = 0

  def set_value(self, x, y, value):
    prev = self.data[x][y]
    self.data[x][y] = value
    self.rowsum[x] += (value - prev)
    self.matsum += (value - prev)

  def get_rowsum(self, x):
    return self.rowsum[x]

  def get_matsum(self):
    return self.matsum

  def pt(self):
    for row in self.data:
      print row

m = Matrix(4)
m.set_value(1, 1, 5)
m.set_value(2, 2, 4)
m.set_value(1, 0, 3)
m.set_value(1, 1, 3)
m.pt()
print m.rowsum
print m.matsum
