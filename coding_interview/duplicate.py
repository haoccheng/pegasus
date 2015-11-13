# An array contains n numbers ranging from 0 to n-2.
# There is exactly one number duplicated in the array.
# How to find the duplicate.
# [0,2,1,3,2], duplicate number is 2.

# Exploit the fact that no missing and exactly 1 duplicate.

def duplicate(numbers):
  nnumbers = len(numbers) - 2 # 0 does not count, 1 duplicate.
  expect = (1 + nnumbers) * nnumbers / 2
  actual = sum(numbers)
  diff = actual - expect
  return diff

def test():
  print duplicate([0, 2, 1, 3, 2])
  print duplicate([0, 2, 1, 3, 4, 5, 1])
  print duplicate([0, 2, 1, 3, 4, 5, 0])
  print duplicate([0, 0])
  print duplicate([0, 1, 1])

test()
