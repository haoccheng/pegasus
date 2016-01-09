# [2,3,1,1,4] -> 2.

def jump(nums):
  if (len(nums) == 0) or (len(nums) == 1):
    return 0
  prev_max = 0
  curr_step = 1
  curr_max = nums[0]
  while (curr_max < len(nums)-1):
    next = 0
    for s in range(curr_max, prev_max, -1):
      next = max(next, s + nums[s])
    if next >= len(nums)-1:
      return curr_step + 1
    if curr_max == next:
      return 0
    curr_step += 1
    prev_max = curr_max
    curr_max = next
  return curr_step

print jump([2,3,1,2,4])
print jump([2,0,0,2,4])
