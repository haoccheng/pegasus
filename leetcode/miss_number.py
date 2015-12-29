# Given an array of n distinct number from 0..n, find the one that is missing.

def miss_number(nums):
  n = len(nums)
  total = (int)(n * (n + 1) / 2)
  for v in nums:
    total -= v
  return total

print miss_number([0, 1, 3])
