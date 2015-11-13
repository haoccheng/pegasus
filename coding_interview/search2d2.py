# In 2-D matrix:
# Every row is increasingly sorted from left to right.
# Every column is increasing sorted from top to bottom.

# 1 2 8 9
# 2 4 9 12
# 4 7 10 13
# 6 8 11 15

def search2d_base(matrix, target, rs, re, cs, ce):
  out = []
  if (target >= matrix[rs][cs]) and (target <= matrix[re][ce]):
    rm = (rs + re) / 2
    cm = (cs + ce) / 2
    if (target == matrix[rm][cm]):
      return [(rm, cm)]
    else:
      out += search2d_base(matrix, target, rs, rm, cs, cm)
      if (cm + 1 <= ce):
        out += search2d_base(matrix, target, rs, rm, cm+1, ce)
      if (rm + 1 <= re):
        out += search2d_base(matrix, target, rm+1, re, cs, cm)
      if (cm + 1 <= ce) and (rm + 1 <= re):
        out += search2d_base(matrix, target, rm+1, re, cm+1, ce)
  else:
    return []
  return out

def search2d(matrix, target):
  return search2d_base(matrix, target, 0, len(matrix)-1, 0, len(matrix[0])-1)

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
