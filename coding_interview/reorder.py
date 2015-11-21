# reorder input array to place all odds before evens.
# [1,2,3,4,5] -> [1,5,3,4,2]
# The result is not unique.

def oddeven(value):
  b = value & 1
  if (b == 0):
    return 0 # even
  else:
    return 1 # odd.

def reorder(input):
  x = 0
  y = len(input) - 1
  while (x < y):
    xf = oddeven(input[x])
    yf = oddeven(input[y])
    swap = 1
    if xf == 1:
      x += 1
      swap = 0 
    if yf == 0:
      y -= 1
      swap = 0
    if (swap == 1):
      t = input[x]
      input[x] = input[y]
      input[y] = t
      x += 1
      y -= 1

def test():
  i1 = [1,2,3,4,5]
  reorder(i1)
  print i1

  i2 = [2,4,1,3,6]
  reorder(i2)
  print i2

test()
