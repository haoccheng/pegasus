# product of all elements in the array except itself.
# given [1,2,3,4], return [24,12,8,6].

def product(nums):
  if len(nums) == 0:
    return []
  left = [0] * len(nums)
  right = [0] * len(nums)
  left[0] = nums[0]
  for i in range(1, len(nums)):
    left[i] = left[i-1]*nums[i]
  right[-1] = nums[-1]
  for i in range(len(nums)-2, -1, -1):
    right[i] = right[i+1]*nums[i]
  ret = [0] * len(nums)
  for i in range(len(nums)):
    if i == 0:
      ret[i] = right[1]
    elif i == len(nums)-1:
      ret[i] = left[i-1]
    else:
      ret[i] = left[i-1]*right[i+1]
  print left
  print right
  print ret

product([1,2,3,4])
