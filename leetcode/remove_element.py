# Given an array and a value, remove all instances of that value in place
# and return the new length.
# The order of elements can be changed.

def remove_elements(nums, val):
  if len(nums) == 0:
    return 0
  x = 0
  y = len(nums) - 1
  while (x < y):
    if nums[y] == val:
      y -= 1
    elif nums[x] == val:
      nums[x] = nums[y]
      x += 1
      y -= 1
    else:
      x += 1
  if nums[x] == val:
    x -= 1
  return min(y+1, x+1)

input = [1, 1, 1, 1]
print remove_elements(input, 1), input
input = [1, 2, 1, 2]
print remove_elements(input, 1), input
input = [4, 5]
print remove_elements(input, 4), input
input = [1]
print remove_elements(input, 1), input
