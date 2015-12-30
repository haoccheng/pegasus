# Given an array of integers, find if any duplicates.

def duplicate(nums):
  hit = {}
  for v in nums:
    if v in hit:
      return True
    else:
      hit[v] = 1
  return False
