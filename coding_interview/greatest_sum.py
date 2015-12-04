# Given an integer array containing positive/negative numbers.
# Find the maximum sum its subarrays.
# Continuous numbers form a subarray of an array.
# {1,-2,3,10,-4,7,2,-5} -> {3,10,-4,7,2} = 18.

# dynamic programming.
# S[i, j] = maximum score of subarray within range [i,j] and end at j.
# Two choices:
# S[i+1, j] or S[i,j-1] + S[j,j]

def init_matrix(input):
  m = []
  for i in range(len(input)):
    row = []
    for j in range(len(input)):
      row.append(0.0)
    m.append(row)
  for i in range(len(input)):
    m[i][i] = input[i]
  return m

def update_matrix(matrix):
  for j in range(1, len(matrix[0])):
    for i in range(j-1, -1, -1):
      if (j - 1) >= 0:
        c0 = matrix[j][j]
        c1 = matrix[i+1][j]
        c2 = matrix[i][j-1] + matrix[j][j]
        matrix[i][j] = max(max(c0, c1), c2)
      else:
        c0 = matrix[j][j]
        c1 = matrix[i+1][j]
        matrix[i][j] = max(c0, c1)

def print_matrix(matrix):
  for i in range(len(matrix)):
    print matrix[i]

def find_max(matrix):
  s = 0
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] > s:
        s = matrix[i][j]
  return s

def great_sum(input):
  matrix = init_matrix(input)
  update_matrix(matrix)
  print_matrix(matrix)
  return find_max(matrix)

def test():
  print great_sum([1, -2, 3, 10, -4, 7, 2, -5])

test()

