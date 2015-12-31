# https://leetcode.com/problems/unique-paths/
# mxn matrix.
# How many unique paths from top-left to bottom-right.

def unique_paths(m, n):
  rows = []
  for i in range(m):
    row = [0] * n
    rows.append(row)
  for i in range(m):
    rows[i][0] = 1
  for j in range(n):
    rows[0][j] = 1
  for i in range(1, m):
    for j in range(1, n):
      rows[i][j] = rows[i-1][j] + rows[i][j-1]
  return rows[-1][len(rows[-1])-1]

print unique_paths(3, 3)
