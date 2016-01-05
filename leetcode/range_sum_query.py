# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:
  def __init__(self, nums):
    self.cache = [0] * len(nums)
    self.cache[0] = nums[0]
    for i in range(1, len(nums)):
      self.cache[i] = self.cache[i-1]+nums[i]

  def sum_range(self, i, j):
    si = 0
    if i > 0:
      si = self.cache[i-1]
    sj = self.cache[j]
    return sj - si

