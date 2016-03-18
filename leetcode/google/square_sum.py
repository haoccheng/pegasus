# Given a target, find the minimum number of integers such that,
# the sum of squares of these integers equal to target.
# 14 = 1^2 + 2^2 + 3^2

# This is like the minimum number of coins to sum to a target amount.

import math

def square_sum(target):
  root = int(math.sqrt(target))
  coins = [i*i for i in range(1, root+1)]
  com = [0] * (target + 1)
  for v in range(1, len(com)):
    opt = None
    for c in coins:
      if v - c >= 0:
        if opt is None:
          opt = com[v - c] + 1
        else:
          opt = min(opt,  com[v - c] + 1)
      else:
        break
    com[v] = opt
  return com[-1]

for target in range(1, 21):
  print target, square_sum(target)

