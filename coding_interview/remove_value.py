# Given an array and a value, remove all instances of that value in place.
# Return the new length of the array.
# Not need to keep the order. It does not matter what are left beyond the new length.
# [4,3,2,1,2,3,6] -> remove 2 -> [4,3,1,3,6]

def remove(input, value):
  newlen = len(input)
  x = 0
  y = len(input) - 1
  while (x < y):
    if input[x] == value:
      if input[y] == value:
        y -= 1
        newlen -= 1
      else:
        input[x] = input[y]
        y -= 1
        x += 1
        newlen -= 1
    else:
      x += 1
  if x == y:
    if input[x] == value:
      newlen -= 1
  return newlen

def test():
  x1 = [4, 3, 2, 1, 2, 3, 6]
  n1 = remove(x1, 2)
  print n1, x1[:n1]

  x2 = [1, 1, 1, 1]
  n2 = remove(x2, 1)
  print n2, x2[:n2]

test()
