# given mxn 2D grid initialized with 3 possible values.
# -1: wall/obstacle
# 0: gat
# INF: empty room. 2147483647
# Fill each room with distance to its nearest gate. If it is impossible to reach a gate; filled with INF.

#INF  -1  0  INF
#INF INF INF  -1
#INF  -1 INF  -1
#  0  -1 INF INF
# --> -->
# 3  -1   0   1
# 2   2   1  -1
# 1  -1   2  -1
# 0  -1   3   4

# BFS traversal starting from all gates.
def walls_gates(matrix):
  candidates = []
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == 0:
        candidates.append((i, j))
  step = 0
  while len(candidates) > 0:
    new_candidates = []
    for (x, y) in candidates:
      if (x - 1) >= 0 and (matrix[x-1][y] == 2147483647):
        new_candidates.append((x-1, y))
      if (x + 1) <= len(matrix)-1 and (matrix[x+1][y] == 2147483647):
        new_candidates.append((x+1, y))
      if (y - 1) >= 0 and (matrix[x][y-1] == 2147483647):
        new_candidates.append((x, y-1))
      if (y + 1) <= len(matrix[x])-1 and (matrix[x][y+1] == 2147483647):
        new_candidates.append((x, y+1))
    step += 1
    for (x, y) in new_candidates:
      matrix[x][y] = step
    candidates = new_candidates
  for row in matrix:
    print row

walls_gates([[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]])
