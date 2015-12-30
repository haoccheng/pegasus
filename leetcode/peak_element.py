# https://leetcode.com/problems/find-peak-element/

def peak_element(nums):
  if len(nums) == 1:
    return 0
  else:
    if nums[0] > nums[1]:
      return 0
    if nums[-1] > nums[-2]:
      return len(nums)-1
    start = 0
    end = len(nums) - 1
    while (start <= end):
      mid = (int)((start + end) / 2)
      if (start == mid):
        break
      if (nums[mid] > nums[mid-1]) and (nums[mid] > nums[mid+1]):
        return mid
      if nums[mid] < nums[mid-1]:
        end = mid-1
      elif nums[mid] < nums[mid+1]:
        start = mid+1
    if nums[start] > nums[end]:
      return start
    else:
      return end

#print peak_element([1, 2, 3, 1])
#print peak_element([1, 2, 4, 5, 1])
print peak_element([3, 4, 3, 2, 1])
