# Write an efficient algorithm to search for a value in mxn matrix.
# integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of previous row.

def search_matrix(matrix, target):
  m = len(matrix)
  n = len(matrix[0])
  rs = 0
  re = m-1
  while (rs <= re):
    rm = (int)((rs + re) / 2)
    if (matrix[rs][0] <= target) and (target <= matrix[rm][n-1]):
      re = rm
    elif (rm == re):
      return False
    elif (matrix[rm+1][0] <= target) and (target <= matrix[re][n-1]):
      rs = rm+1
    else:
      return False
    if (rs == re):
      break
    elif (rs + 1 == re):
      if (matrix[rs][0] <= target) and (target <= matrix[rs][n-1]):
        rs = rs
      elif (matrix[re][0] <= target) and (target <= matrix[re][n-1]):
        rs = re
      else:
        return False
  cs = 0
  ce = n-1
  while (cs <= ce):
    cm = (int)((cs + ce) / 2)
    if (matrix[rs][cs] <= target) and (target <= matrix[rs][cm]):
      ce = cm
    elif (cm == ce):
      return False
    elif (matrix[rs][cm+1] <= target) and (target <= matrix[rs][ce]):
      cs = cm+1
    else:
      return False
    if (cs == ce):
      return True
    elif (cs + 1 == ce):
      if matrix[rs][cs] == target or matrix[rs][ce] == target:
        return True
      else:
        return False
  return False

#print search_matrix([[1,3]], 2)
print search_matrix([[1,3,5]], 4)
