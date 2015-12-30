# https://leetcode.com/problems/set-matrix-zeroes/
# constant space solution

def set_zeros(matrix):
  # check 1st row; need extra bit.
  matrix_r0 = False
  for i in range(len(matrix[0])):
    if matrix[0][i] == 0:
      matrix_r0 = True
      break
  matrix_c0 = False
  for i in range(len(matrix)):
    if matrix[i][0] == 0:
      matrix_c0 = True
      break
  for i in range(len(matrix)):
    for j in range(len(matrix[i][j])):
      if matrix[i][j] == 0:
        matrix[i][0] = 0
        matrix[0][j] = 0
  # set row first
  for i in range(1, len(matrix)):
    if matrix[i][0] == 0:
      for j in range(len(matrix[i])):
        matrix[i][j] = 0
  for j in range(1, len(matrix[0])):
    if matrix[0][j] == 0:
      for i in range(len(matrix)):
        matrix[i][j] = 0
  if matrix_r0 == True:
    for i in range(len(matrix[0])):
      matrix[0][i] = 0
  if matrix_c0 == True:
    for i in range(len(matrix)):
      matrix[i][0] = 0

