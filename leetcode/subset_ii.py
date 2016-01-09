# Given a collection of integers that might contain duplicates.
# return all possible subsets.

def subset(nums):
  ret = []
  if len(nums) == 0:
    ret = [[]]
  elif len(nums) == 1:
    ret = [[], [nums[0]]]
  else:
    for i in range(len(nums)):
      if i != 0 and nums[i] == nums[i-1]:
        continue
      ret += [[nums[i]] + e for e in subset(nums[i+1:])]
    ret += [[]]
  return ret

print subset([1,1,2])

