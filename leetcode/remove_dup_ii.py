# remove duplicate from sorted array.
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# duplicates allow at most twice.

def remove_dup(nums):
  if len(nums) == 0:
    return 0
  start = 0
  prev_value = None
  prev_count = 0
  for i in range(len(nums)):
    if prev_value is None:
      start += 1
      prev_value = nums[i]
      prev_count = 1
    else:
      curr_value = nums[i]
      if curr_value == prev_value:
        prev_count += 1
        if prev_count <= 2:
          nums[start] = curr_value
          start += 1
      else:
        nums[start] = curr_value
        prev_value = curr_value
        prev_count = 1
        start += 1
  return start

x = [1,1,1,2,2,3]
print remove_dup(x)
print x
