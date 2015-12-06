# Find the first character in a stream that only appear once at any time while reading the stream
# go (first two character) -> g
# google (6th character) -> l

class FirstUniqCharStream:
  def __init__(self):
    self.candidates = []
    self.count = {}
    self.index = 0

  def accept(self, c):
    if c in self.count:
      self.count[c] = -1
    else:
      self.count[c] = self.index
      self.index += 1
      self.candidates.append(c)

  def min(self):
    while (len(self.candidates) > 0):
      h = self.candidates[0]
      if self.count[h] >= 0:
        return h
      else:
        self.candidates.pop(0)
    return None

def test():
  f = FirstUniqCharStream()
  for c in 'googlela':
  f.accept(c)
    print f.min()

test()
