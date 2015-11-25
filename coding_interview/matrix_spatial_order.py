# print a matrix in spatial order, clockwise from outer rings to inner rings.
#  1  2  3  4
#  5  6  7  8
#  9 10 11 12
# 13 14 15 16
#
# spatial order: 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10

# one way is to keep a separate visit matrix to record the cells that have been visited.
# instead, keep track of the direction and the number of steps to advance in that direction.

def spatial_order(matrix):
  horizon = len(matrix[0])
  vertical = len(matrix) - 1
  mode = 'LEFT-RIGHT'
  x = 0
  y = -1
  while (True):
    if (mode == 'LEFT-RIGHT'):
      for i in range(0, horizon):
        y = y + 1
        print matrix[x][y]
      horizon -= 1
      mode = 'TOP-BOTTOM'
    elif (mode == 'TOP-BOTTOM'):
      for i in range(0, vertical):
        x = x + 1
        print matrix[x][y]
      vertical -= 1
      mode = 'RIGHT-LEFT'
    elif (mode == 'RIGHT-LEFT'):
      for i in range(0, horizon):
        y = y - 1
        print matrix[x][y]
      horizon -= 1
      mode = 'BOTTOM-TOP'
    elif (mode == 'BOTTOM-TOP'):
      for i in range(0, vertical):
        x = x - 1
        print matrix[x][y]
      vertical -= 1
      mode = 'LEFT-RIGHT'
    if (horizon <= 0) and (vertical <= 0):
      break

def test():
  m2 = []
  m2.append([1, 2, 3, 4])
  m2.append([5, 6, 7, 8])
  m2.append([9, 10, 11, 12])
  m2.append([13, 14, 15, 16])
  spatial_order(m2)

test()
