# determine whether an integer is a palindrome.
# No extra space.

import math

def ndigit(x, index):
  v = (int)(x / math.pow(10, index-1))
  v = v % 10
  return v

def is_palindrome(x):
  if x < 0:
    return False
  if x < 10:
    return True
  total = (int)(math.log(x) / math.log(10)) + 1
  i = total
  j = 1
  while (i > j):
    lv = ndigit(x, i)
    rv = ndigit(x, j)
    if lv != rv:
      return False
    i -= 1
    j += 1
  return True
  
for v in [1, 10, 11, 101, 10301, 1000021]:
  print v, is_palindrome(v)

