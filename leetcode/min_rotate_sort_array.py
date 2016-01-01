# find minimum of rotated sorted array.
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def pivot(nums):
  start = 0
  end = len(nums) - 1
  while (start <= end):
    mid = (int)((start + end) / 2)
    v1 = nums[start]
    v2 = nums[mid]
    v3 = nums[end]
    if v1 > v2:
      end = mid
    elif v2 > v3:
      start = mid
    else:
      return nums[start]
    if (start == end):
      return nums[start]
    elif (start + 1 == end):
      if nums[start] < nums[end]:
        return nums[start]
      else:
        return nums[end]

