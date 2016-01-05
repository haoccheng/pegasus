# next permutation.
# modify 

def next_permutation(input):
  nums = list(input)
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
  return nums

def permute(nums, k):
  index = 1
  while (True):
    if index == k:
      return nums
    n = next_permutation(nums)
    index += 1
    if n is None:
      break
    else:
      nums = n

def permute_k(n, k):
  nums = range(1, n+1)
  return permute(nums, k)

#print permute_k(3, 2)
print permute_k(9, 171669)
