# Given a matrix mxn elements, return all elements of matrix in spiral order.
# 1 2 3
# 4 5 6
# 7 8 9
# -> 1 2 3 6 9 8 7 4 5



def spiral_order(matrix):
  rs = 0
  re = len(matrix) - 1
  if (re < 0):
    return []
  cs = 0
  ce = len(matrix[0]) - 1
  
  ret = []
  while (rs <= re) and (cs <= ce):
    for i in range(cs, ce+1):
      ret.append(matrix[rs][i])
    for i in range(rs+1, re):
      ret.append(matrix[i][ce])

    if (rs != re):
      for i in range(ce, cs-1, -1):
        ret.append(matrix[re][i])
    if (cs != ce):
      for i in range(re-1, rs, -1):
        ret.append(matrix[i][cs])
    rs += 1
    re -= 1
    cs += 1
    ce -= 1
  print ret

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
spiral_order(matrix)
matrix = [[1,2,3], [4,5,6], [7,8,9]]
spiral_order(matrix)
matrix = [[2], [3]]
spiral_order(matrix)
