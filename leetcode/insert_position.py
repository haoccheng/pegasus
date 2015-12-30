# Given sorted array and target value
# Return the index if target is found.
# If not, return the index that would be inserted in order.

def insert_position(nums, target):
  if nums[0] == target:
    return 0
  elif nums[-1] == target:
    return len(nums)-1
  elif (nums[0] > target):
    return 0
  elif (target > nums[-1]):
    return len(nums)
  else:
    start = 0
    end = len(nums) - 1
    while (start <= end):
      mid = (int)((start + end) / 2)
      print start, end, mid
      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        start = mid + 1
      else:
        end = mid - 1
      if (start >= end):
        if nums[start] < target:
          return start+1
        else:
          return start
  
#print insert_position([1,3,5,6], 5)
#print insert_position([1,3,5,6], 2)
#print insert_position([1,3,5,6], 7)
#print insert_position([1,3,5,6], 0)
print insert_position([3,5,7,9,10], 8)

