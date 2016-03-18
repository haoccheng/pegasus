# compute integral image
# [i,j]: sum of values from [0,0] to [i,j]

def integral(matrix):
  scores = []
  for i in range(len(matrix)):
    row = [0] * len(matrix[i])
    scores.append(row)
  tmp = 0
  for j in range(len(matrix[0])):
    tmp += matrix[0][j]
    scores[0][j] = tmp
  for i in range(len(matrix)):
    tmp = 0
    for j in range(len(matrix[i])):
      tmp += matrix[i][j]
      scores[i][j] = scores[i-1][j] + tmp
  for row in matrix:
    print row
  print '==============='
  for row in scores:
    print row

integral([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
