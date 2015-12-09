# Given a sequence, find the longest increasing subsequence.
# {1,2,5,3,4,7,6} -> 5.

# matrix[i, j]: up till position i, maximum value no greater than j, the length of longest increase subsequence.

def init_matrix(input):
  matrix = []
  for i in range(len(input)+1):
    row = [0] * (len(input)+1)
    matrix.append(row)
  for j in range(len(input)+1):
    if j >= input[0]:
      matrix[1][j] = 1
  return matrix

def update_matrix(input, matrix):
  for i in range(2, len(matrix)):
    for j in range(1, len(matrix[i])):
      if j >= input[i-1]:
        v1 = matrix[i-1][j]
        v2 = matrix[i-1][input[i-1]-1] + 1
        matrix[i][j] = max(v1, v2)
      else:
        matrix[i][j] = matrix[i-1][j]

def print_matrix(matrix):
  for i in range(len(matrix)):
    print matrix[i]

input = [1, 2, 5, 3, 4, 7, 6]
matrix = init_matrix(input)
update_matrix(input, matrix)
print_matrix(matrix)
