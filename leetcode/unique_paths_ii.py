# https://leetcode.com/problems/unique-paths-ii/
# mxn matrix.
# How many unique paths from top-left to bottom-right obstacles..

def unique_paths(obstacle):
  m = len(obstacle)
  n = len(obstacle[0])
  rows = []
  for i in range(m):
    row = [0] * n
    rows.append(row)
  for i in range(m):
    if obstacle[i][0] == 1:
      break
    rows[i][0] = 1
  for j in range(n):
    if obstacle[0][j] == 1:
      break
    rows[0][j] = 1
  for i in range(1, m):
    for j in range(1, n):
      if obstacle[i][j] == 1:
        continue
      rows[i][j] = rows[i-1][j] + rows[i][j-1]
  return rows[-1][len(rows[-1])-1]

