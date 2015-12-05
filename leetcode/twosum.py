# Given an arrya of integers, find two numbers such that they add up to a target value
# numbers={2, 7, 11, 15}, target=9.
# output: [1,2] index starting at one.
# Possibly a number might appear multiple times in the input.

from collections import defaultdict

def twosum(nums, target):
  # init index
  index = defaultdict(list)
  for i in range(len(nums)):
    index[nums[i]].append(i+1)
  # search for sum match
  for v in nums:
    r = target - v
    if (r == v):
      if len(index[r]) >= 2:
        return index[r][:2]
    else:
      if r in index:
        p1 = index[v] if index[v] < index[r] else index[r]
        p2 = index[r] if index[v] < index[r] else index[v]
        p1 = p1[0]
        p2 = p2[0]
        return [p1, p2]
  return None

def test():
  print twosum([2, 7, 11, 15], 9)
  print twosum([0, 1, 5, 0], 0)

test()
