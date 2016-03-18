# mxn 2d array
# unique numbers from 1..mxn are shuffled and filled in the 2d array.
# now, find the longest consecutive sequences.

def search2d_base(matrix, scores, x, y):
  value = matrix[x][y]
  (nx, ny) = (None, None)
  if x-1 >= 0 and matrix[x-1][y] == value+1:
    (nx, ny) = (x-1, y)
  elif x+1 <= len(matrix)-1 and matrix[x+1][y] == value+1:
    (nx, ny) = (x+1, y)
  elif y-1 >= 0 and matrix[x][y-1] == value+1:
    (nx, ny) = (x, y-1)
  elif y+1 <= len(matrix[x])-1 and matrix[x][y+1] == value+1:
    (nx, ny) = (x, y+1)
  if nx is not None:
    if scores[nx][ny] > 0:
      scores[x][y] = scores[nx][ny] + 1
    else:
      s = search2d_base(matrix, scores, nx, ny)
      scores[x][y] = s + 1
  else:
    scores[x][y] = 1
  return scores[x][y]

def search2d(matrix):
  scores = []
  for i in range(len(matrix)):
    row = [0] * len(matrix[i])
    scores.append(row)
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if scores[i][j] == 0:
        search2d_base(matrix, scores, i, j)
  for row in matrix:
    print row
  for row in scores:
    print row
  return max(max(scores))

print search2d([[1, 2, 3], [6, 5, 4], [7, 8, 9]])
print search2d([[4, 2, 3], [5, 1, 9], [6, 8, 7]])

