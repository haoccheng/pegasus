# Given an array of non-negative integers, initially positioned at first index of the array.
# Each element represents the maximum jump length at that position.
# Determine if you can reach the last index.
# A = [2,3,1,1,4], return true. 
# A = [3,2,1,0,4], return false. 

def jump_game(nums):
  max_index = 0 # keep track of the maximum point that can reach.
  for i in range(len(nums)):
    if max_index < i:
      break
    v = nums[i]
    mv = i + v
    if mv > max_index:
      max_index = mv
  return True if (max_index >= len(nums) - 1) else False

print jump_game([2,3,1,1,4])
print jump_game([3,2,1,0,4])
