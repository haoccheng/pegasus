# Given an array of numbers and a sliding window size.
# Compute the maximum numbers in a sliding window.
# {2,3,4,2,6,2,5,1}, window=3, {4,4,6,6,6,7}

class WindowMax:
  def __init__(self, window):
    self.candidates = []
    self.index = 0
    self.window = window

  def accept(self, value):
    # remove invalid candidates.
    candidates = []
    for (v, i) in self.candidates:
      if ((self.index - i) < self.window) and (v > value):
        candidates.append((v, i))
    # add the current candidate 
    candidates.append((value, self.index))
    self.candidates = candidates
    # advance index
    self.index += 1

  def max(self):
    return self.candidates[0][0]

wm = WindowMax(3)
for v in [2,3,4,2,6,2,5,1,7,0,7,1,2,3]:
  wm.accept(v)
  print wm.max()
