# Given 2d binary matrix filled with 0/1, find the largest square containing all 1, return area

def maximal_square(matrix):
  areas = []
  for i in range(len(matrix)):
    row = [None] * len(matrix[i])
    areas.append(row)
  for j in range(len(areas[0])):
    areas[0][j] = 1 if matrix[0][j] == '1' else 0
  for i in range(len(areas)):
    areas[i][0] = 1 if matrix[i][0] == '1' else 0
  for i in range(1, len(areas)):
    for j in range(1, len(areas[i])):
      if matrix[i][j] == '0':
        areas[i][j] = 0
      else:
        areas[i][j] = min(areas[i-1][j-1], areas[i-1][j], areas[i][j-1]) + 1
  print max(max(areas))
maximal_square([list('10100'), list('10111'), list('11111'), list('10010')])

