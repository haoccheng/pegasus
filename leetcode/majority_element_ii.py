# Given an array of size n, find all elements that appear more than n/3 times.
# Linear time + O(1) space.

def majority(nums):
  major1 = None
  count1 = 0
  major2 = None
  count2 = 0
  for value in nums:
    if value == major1:
      count1 += 1
    elif value == major2:
      count2 += 1
    elif count1 == 0:
      major1 = value
      count1 += 1
    elif count2 == 0:
      major2 = value
      count2 += 1
    else:
      count1 -= 1
      count2 -= 1
  count1 = 0
  count2 = 0
  for value in nums:
    if value == major1:
      count1 += 1
    elif value == major2:
      count2 += 1
  result = []
  if count1 > len(nums)/3:
    result.append(major1)
  if count2 > len(nums)/3:
    result.append(major2)
  return result

print majority([1,1,1,2])
