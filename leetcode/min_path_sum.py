# mxn grid with non-negative numbes.
# find a path from top-left to bottom-right.
# minimize the sum of all numbers in the path.
# can only move down or right.

def min_path_sum(grid):
  scores = []
  for i in range(len(grid)):
    row = [0] * len(grid[0])
    scores.append(row)
  scores[0][0] = grid[0][0]
  for i in range(1, len(grid)):
    scores[i][0] = scores[i-1][0] + grid[i][0]
  for j in range(1, len(grid[0])):
    scores[0][j] = scores[0][j-1] + grid[0][j]
  for i in range(1, len(grid)):
    for j in range(1, len(grid[i])):
      s1 = scores[i-1][j] + grid[i][j]
      s2 = scores[i][j-1] + grid[i][j]
      scores[i][j] = min(s1, s2)
  return scores[-1][-1]
