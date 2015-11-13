# In 2-D matrix, every row is increasingly sorted from left to right.
# The last number if each row is no grater than the first number of the next row.
# Implement a function to check whether a number is in such a matrix or not.

# 1 3 5
# 7 9 11
# 13 15 17

# This is just like one-dimensional array sorted and zip-zap into a two-dimensional matrix.

def search2d(matrix, target):
  rs = 0
  re = len(matrix) - 1
  cs = 0
  ce = len(matrix[0]) - 1
  # STAGE 1: update rs/re till rs == re.
  while (rs < re):
    if (matrix[rs][cs] <= target) and (target <= matrix[re][ce]): # within the search region.
      rm = (rs + re) / 2
      if (target <= matrix[rm][ce]):
        re = rm
      else:
        rs = rm + 1
    else:
      return None
  # STAGE 2: update cs/ce till cs == ce.
  while (cs <= ce):
    if (matrix[rs][cs] <= target) and (target <= matrix[rs][ce]): # within.
      cm = (cs + ce) / 2
      if (target == matrix[rs][cm]):
        return (rs, cm)
      elif (target < matrix[rs][cm]):
        ce = cm - 1
      else:
        cs = cm + 1
    else:
      return None
  return None

def test():
  m1 = [[1,3,5], [7,9,11], [13,15,17]]
  for target in [7, 9, 11]:
    print m1, target, search2d(m1, target)
  m2 = [[1,3,5], [7,9,11], [13,15,17], [18,19,20], [100,200,300]]
  for target in [7, 15, 100, 400]:
    print m2, target, search2d(m2, target)

test()
