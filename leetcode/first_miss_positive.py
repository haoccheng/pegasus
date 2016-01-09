# first missing positive. O(n) complexity + O(1).
# [1,2,0] -> 3
# [3,4,-1,1] -> 2

def miss_positive(nums):
  for i in range(len(nums)):
    if nums[i] == i+1:
      continue
    while (True):
      v = nums[i]
      if (v > len(nums)) or (v <= 0): # if beyond bound.
        nums[i] = -1
        break
      p = nums[v-1]
      nums[v-1] = v
      if v == p: # if duplicate, endless loop.
        nums[i] = -1
        break
      nums[i] = p
      if nums[i] == i+1:
        break
  for i in range(len(nums)):
    if nums[i] != i+1:
      return i+1
  return len(nums)+1

print miss_positive([1,2,0])
print miss_positive([3,4,-1,1])
print miss_positive([1,2,3,4])
print miss_positive([4,1,2,3])
print miss_positive([1,1])
