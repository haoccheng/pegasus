# Given an integer n, generate a square matrix filled with elements 1~n^2.
# n=3
# 1 2 3
# 8 9 4
# 7 6 5

def generate_matrix(n):
  # init matrix.
  matrix = []
  for i in range(n):
    row = [0] * n
    matrix.append(row)
  value = 1
  step = n - 1
  for i in range(n):
    x = i
    y = i
    if (step < 0):
      break
    elif (step == 0):
      matrix[x][y] = value
      break
    for j in range(step):
      matrix[x][y] = value
      y += 1
      value += 1
    for j in range(step):
      matrix[x][y] = value
      x += 1
      value += 1
    for j in range(step):
      matrix[x][y] = value
      y -= 1
      value += 1
    for j in range(step):
      matrix[x][y] = value
      x -= 1
      value += 1
    step = step - 2

  for i in range(n):
    print ' '.join(['%2d' % e for e in matrix[i]])
  return matrix
generate_matrix(3)
generate_matrix(4)
