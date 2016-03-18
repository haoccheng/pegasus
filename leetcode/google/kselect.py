# Given an array, evenly divide into k.
# Pick one element from each array, generate all possible combinations.

import math

def kselect_base(splits):
  if len(splits) == 1:
    return [[e] for e in splits[0]]
  first = splits[0]
  rest = kselect_base(splits[1:])
  return [[e1] + e2 for e1 in first for e2 in rest]

def kselect(input, k):
  splits = []
  piece = int(math.ceil(len(input) * 1.0 / k))
  start = 0
  while (start < len(input)):
    end = start + piece
    splits.append(input[start:end])
    start = end
  return kselect_base(splits)

print kselect(range(1,5), 2)
print kselect(range(1,10), 3)

