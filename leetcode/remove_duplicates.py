# Given a sorted array, remove duplicates in place such that each element appears only once.
# Return the new length.
# Do not matter what are left beyond the new length in the original array.

def remove_duplicates(nums):
  x = 0
  curr = None
  for i in range(len(nums)):
    v = nums[i]
    if curr is None:
      curr = v
      nums[x] = v
      x += 1
    else:
      if curr == v:
        continue
      else:
        curr = v
        nums[x] = v
        x += 1
  return x

input = [1, 1, 2]
print remove_duplicates(input), input
input = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4]
print remove_duplicates(input), input
