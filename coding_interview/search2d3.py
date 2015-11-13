# In 2-D matrix:
# Every row is increasingly sorted from left to right.
# Every column is increasing sorted from top to bottom.

# 1 2 8 9
# 2 4 9 12
# 4 7 10 13
# 6 8 11 15

# Either start at top-right corner or bottom-left corner.
def search2d(matrix, target):
  rs = len(matrix)-1 # bottom-left corner.
  cs = 0
  out = []
  while (rs >= 0) and (rs < len(matrix)) and (cs >= 0) and (cs < len(matrix[0])):
    if (matrix[rs][cs] == target):
      out.append((rs, cs))
    if (matrix[rs][cs] >= target):
      rs -= 1
    else:
      cs += 1
  return out

def test():
  m1 = [[1,3,5], [7,9,11], [13,15,17]]
  for target in [7, 9, 11]:
    print m1, target, search2d(m1, target)
  m2 = [[1,3,7], [7,9,11], [13,15,17]]
  for target in [7, 9, 11]:
    print m2, target, search2d(m2, target)
  m3 = [[1,2,8,9], [2,4,9,12], [4,7,10,13], [6,8,11,15]]
  for target in [7, 5]:
    print m3, target, search2d(m3, target)

test()
