# compute CDF
# (2, 2, 4, 6, 8)
# give 0, return 0%
# give 2, return 40%
# give 7, return 80%.

class CDF:
  def __init__(self, data):
    self.cdf = []
    data = sorted(data)
    for v in data:
      if len(self.cdf) == 0:
        self.cdf.append((v, 1))
      elif v == self.cdf[-1][0]:
        self.cdf[-1] = (v, self.cdf[-1][1]+1)
      else:
        self.cdf.append((v, self.cdf[-1][1]+1))
    self.total = self.cdf[-1][1]

  def lookup(self, value):
    start = 0
    end = len(self.cdf)-1
    while (start <= end):
      if start == end:
        if self.cdf[start][0] <= value:
          return self.cdf[start][1] * 1.0 / self.total
        else:
          return 0.0
      elif start + 1 == end:
        if self.cdf[end][0] <= value:
          return self.cdf[end][1] * 1.0 / self.total
        elif self.cdf[start][0] <= value:
          return self.cdf[start][1] * 1.0 / self.total
        else:
          return 0.0
      else:
        middle = (start + end) / 2
        if self.cdf[middle][0] <= value:
          start = middle
        else:
          end = middle - 1
    return 0.0

cdf = CDF([2, 2, 4, 6, 8])
print cdf.lookup(2)
print cdf.lookup(7)
