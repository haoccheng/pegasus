# maximum sum submatrix

def maxsum(matrix):
  candidate = None
  for i in range(len(matrix)): # row i ~ row j
    colsum = [0] * len(matrix[i])
    for j in range(i, len(matrix)):
      for k in range(len(matrix[i])):
        colsum[k] += matrix[j][k]
      optsum = [0] * len(colsum)
      optsum[0] = colsum[0]
      for k in range(1, len(optsum)):
        optsum[k] = max(colsum[k], colsum[k]+optsum[k-1])
      if candidate is None:
        candidate = max(optsum)
      elif max(optsum) > candidate:
        candidate = max(optsum)
  print candidate

maxsum([[0, -2, -7, 0], [9, 2, -6, 2], [-4, 1, -4, 1], [-1, 8, 0, -2]])
