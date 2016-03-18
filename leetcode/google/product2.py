# given an array with integers, find the maximum product of two numbers.

# non-negative: 0, 99, 100
# negative: -100, -99

import sys

def product2(input):
  nonnegative = []
  negative = []
  for value in input:
    if value >= 0:
      if len(nonnegative) < 3:
        nonnegative.append(value)
        nonnegative = sorted(nonnegative)
      else:
        nonnegative.append(value)
        nonnegative = sorted(nonnegative)
        nonnegative.pop(1)
    else:
      if len(negative) < 3:
        negative.append(value)
        negative = sorted(negative)
      else:
        negative.append(value)
        negative = sorted(negative)
        negative.pop(2)
  candidate = -sys.maxint -1 
  if len(nonnegative) >= 2:
    candidate = max(candidate, nonnegative[-2] * nonnegative[-1])
  if len(negative) >= 2:
    candidate = max(candidate, negative[0] * negative[1])
  if candidate > -sys.maxint -1:
    return candidate
  else:
    return nonnegative[0] * negative[0]

print product2([1, 2, 3, 4])
print product2([-5, -6, 1, 3, 4])
print product2([-1, 2])
