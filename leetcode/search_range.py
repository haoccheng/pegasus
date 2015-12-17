# Given a sorted array of integers, find start/end position of a target value.
# runtime O(logn).
# If target is not found, return [-1, -1]
# [5, 7, 7, 8, 8, 10], target=8, return [3,4]

def search_range(nums, target):
  i = 0
  j = len(nums) - 1
  while (i < j):
    if i + 1 == j:
      break
    else:
      mid = int((i + j) / 2)
      if nums[mid] < target:
        i = mid
      else:
        j = mid
  if (nums[i] != target) and (nums[j] != target):
    return [-1, -1]
  i = i if nums[i] == target else j
  j = j if nums[j] == target else i
  xi = 0
  while (xi < i):
    mid = (int)((xi + i) / 2)
    if nums[mid] == target:
      i = mid
    else:
      xi = mid
    if xi + 1 == i:
      if nums[xi] == target:
        i = xi
      break
  xj = len(nums) - 1
  while (j < xj):
    mid = (int)((j + xj) / 2)
    if nums[mid] == target:
      j = mid
    else:
      xj = mid
    if j + 1 == xj:
      if nums[xj] == target:
        j = xj
      break
  return [i, j]

print search_range([5, 7, 7, 8, 8, 10], 8)
