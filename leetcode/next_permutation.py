# next permutation.
# modify 

def next_permutation(nums):
  pivot = len(nums) - 1
  pivot_val = nums[pivot]
  while (pivot >= 0):
    if pivot == 0:
      break
    elif nums[pivot-1] >= pivot_val:
      pivot -= 1
      pivot_val = nums[pivot]
    else:
      break
  if pivot == 0:
    w = sorted(nums)
    for i in range(len(w)):
      nums[i] = w[i]
    return
  prev_pivot = pivot - 1
  swap_pivot = None
  for i in range(len(nums)-1, pivot-1, -1):
    if nums[i] <= nums[prev_pivot]:
      continue
    else:
      swap_pivot = i
      break
  t = nums[swap_pivot]
  nums[swap_pivot] = nums[prev_pivot]
  nums[prev_pivot] = t
  start = pivot
  end = len(nums) - 1
  while (start < end):
    t = nums[start]
    nums[start] = nums[end]
    nums[end] = t
    start += 1
    end -= 1

#x = [1, 2, 3, 4, 5]
#print x
#for i in range(10):
#  next_permutation(x)
#  print x
x = [1, 1]
next_permutation(x)
print x
