# Given an array of non-negative integers, initially positioned at first index of the array.
# Each element represents maximum jump length at the position.
# Goal is to reach the last index in the minimum jumps.
# [2,3,1,1,4] -> 2 jumps.

import sys
def min_jump(nums):
  jumps = [sys.maxsize] * len(nums)
  jumps[0] = 0
  for i in range(len(nums)):
    curr = jumps[i]
    s = nums[i]
    for j in range(1, s+1):
      n = i+j
      if n > len(nums)-1:
        continue
      jumps[n] = min(jumps[n], jumps[i]+1)
  return jumps[-1]

min_jump([2,3,1,1,4])
