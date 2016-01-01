# search 2D matrix (row/column sorted).

def search(matrix, target):
  x = 0
  y = len(matrix[0])-1
  while (x >= 0) and (x <= len(matrix)-1) and (y >= 0) and (y <= len(matrix[0])-1):
    if matrix[x][y] == target:
      return True
    elif matrix[x][y] > target:
      y -= 1
    else:
      x += 1
  return False
