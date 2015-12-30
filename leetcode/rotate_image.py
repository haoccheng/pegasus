# Given nxn 2D matrix, rotate the image by 90 degree (clockwise).

def rotate(matrix):
  start = 0
  end = len(matrix) - 1
  while (start < end):
    step = end - start
    for i in range(step):
      x1 = matrix[start][start+i]
      x2 = matrix[start+i][end]
      x3 = matrix[end][end-i]
      x4 = matrix[end-i][start]
      matrix[start+i][end] = x1
      matrix[end][end-i] = x2
      matrix[end-i][start] = x3
      matrix[start][start+i] = x4
    start += 1
    end -= 1

x = [[1,2,3], [4,5,6], [7,8,9]]
rotate(x)
print x
