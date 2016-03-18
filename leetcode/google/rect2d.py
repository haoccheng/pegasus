# given two dimensional array with 0/1.
# find a rectangle such that 4 corners are 1.

# essentially, if we look from the x-axis, we just need to continuously keep track of
# all the horizontal lengths (the two corners are 1), if later there is match, rectangle can be formed.

def rect2d(matrix):
  hit = set()
  for i in range(len(matrix)):
    bit1 = []
    for j in range(len(matrix[i])):
      if matrix[i][j] == 1:
        bit1.append(j)
    for i1 in range(len(bit1)):
      for i2 in range(i1+1, len(bit1)):
        if (bit1[i1], bit1[i2]) in hit:
          return True
        else:
          hit.add((bit1[i1], bit1[i2]))
  return False

print rect2d([[1,0,1], [0,1,1], [1, 0, 1]])
print rect2d([[1,0,1], [0,1,1], [1, 0, 0]])
