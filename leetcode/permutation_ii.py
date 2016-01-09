# permutation with duplicate
# [1, 1, 2]

def nextseq(nums):
  pivot = len(nums) - 1
  while (pivot > 0):
    if nums[pivot-1] >= nums[pivot]:
      pivot -= 1
    else:
      break
  if pivot == 0:
    return None # end..
  prepivot = nums[pivot-1]
  for i in range(len(nums)-1, pivot-1, -1):
    if nums[i] > prepivot:
      nums[pivot-1] = nums[i]
      nums[i] = prepivot
      break
  start = pivot
  end = len(nums) - 1
  while (start < end):
    t = nums[end]
    nums[end] = nums[start]
    nums[start] = t
    start += 1
    end -= 1
  return nums

def permute(nums):
  if len(nums) == 0:
    return []
  nums = sorted(nums)
  ret = []
  while (nums is not None):
    ret.append(list(nums))
    nums = nextseq(nums)
  print ret

#nextseq([1,1,2,2,4,3])
permute([1,1,2])
