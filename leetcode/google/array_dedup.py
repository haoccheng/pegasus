# given array, remove duplicate
def dup1(input):
  return list(set(input))

print dup1([1, 1, 2, 2, 2, 3])

# if the index is within k, value is same, dedup.
from collections import defaultdict
def dup2(input, k):
  output = []
  hitk = defaultdict(int)
  for i in range(len(input)):
    v = input[i]
    if v not in hitk:
      output.append(v)
      hitk[v] += 1
    vk = input[i-k] if i-k >= 0 else None
    if vk in hitk:
      hitk[vk] -= 1
      if hitk[vk] == 0:
        del hitk[vk]
  return output

print dup2([1, 2, 3, 4, 1, 2, 3, 4, 1], 6)

# if the index is within k, value absolute difference is within d, remove duplicate.
# time complexity O(n).
# I consider the time complexity would be O(nd).
# Basically, for each value, [x-d, x+d] range index.
