# https://leetcode.com/problems/search-in-rotated-sorted-array/
# a sorted array is rotated at some pivot unknown to you beforehand.
# Given a target value to search. If found in the array return its index, otherwise return -1.

def pivot(nums):
  start = 0
  end = len(nums)-1
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
      return start
    if (start == end):
      return start
    elif (start + 1 == end):
      if nums[start] < nums[end]:
        return start
      else:
        return end

def search_base(nums, start, end, target):
  while (start <= end):
    if nums[start] == target:
      return start
    elif nums[end] == target:
      return end
    else:
      mid = (int)((start + end) / 2)
      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        start = mid
      else:
        end = mid
    if (start == end):
      return -1
    elif (start + 1 == end):
      return -1
  return -1

def search(nums, target):
  mi = pivot(nums)
  if nums[mi] == target:
    return mi
  if mi > 0:
    if (nums[0] <= target) and (target <= nums[mi-1]):
      return search_base(nums, 0, mi-1, target)
  if mi < len(nums)-1:
    if (nums[mi] <= target) and (target <= nums[len(nums)-1]):
      return search_base(nums, mi, len(nums)-1, target)
  return -1

print pivot([4,5,6,7,0,1,2])
print search([4,5,6,7,0,1,2], 4)
print search([4,5,6,7,0,1,2], 3)
print search([4,5,6,7,0,1,2], 1)
