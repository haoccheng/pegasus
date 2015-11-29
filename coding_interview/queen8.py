# How many distinct ways are available to place 8 queens on a chessboard.
# No two queens tha can attack each other (no two queens at same row/column/diagonal).

# backtracking.

class State:
  def __init__(self):
    self.queens = [] # coordination of queens. (row, col)

  def pt(self):
    print self.queens

  def candidates(self):
    # consider all positions at row.
    row = len(self.queens)
    ret = []
    for col in range(8):
      # examine feasibility.
      valid = True
      for q in self.queens:
        if row == q[0]: # same row
          valid = False
          break
        if col == q[1]: # same column
          valid = False
          break
        for i in range(-7, 8): # diagonal.
          dx = q[0] + i
          dy = q[1] + i
          if (row == dx) and (col == dy):
            valid = False
            break
        for i in range(-7, 8):
          dx = q[0] - i
          dy = q[1] + i
          if (row == dx) and (col == dy):
            valid = False
            break
      if (valid == True):
        ret.append((row, col))
    return ret

  def explore(self):
    if len(self.queens) == 8:
      print self.queens
      return 1
    else:
      next = self.candidates()
      if len(next) == 0:
        return 0
      else:
        count = 0
        for n in next:
          q = list(self.queens)
          q.append(n)
          c = State()
          c.queens = q
          count += c.explore()
        return count

s = State()
print s.explore()

