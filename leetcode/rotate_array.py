# rotate an array of n elements to the right by k steps.
# n=7, k=3 [1,2,3,4,5,6,7] -> [5,6,7,1,2,3,4]

def rotate(nums, k):
  k = k % len(nums)
  for i in range(k):
    v = nums[-1]
    for j in range(len(nums)):
      p = nums[j]
      nums[j] = v
      v = p
  print nums

def rotate2(nums, k):
  k = k % len(nums)
  start = 0
  end = len(nums) - k - 1
  while (start < end):
    t = nums[end]
    nums[end] = nums[start]
    nums[start] = t
    start += 1
    end -= 1
  start = len(nums) - k
  end = len(nums) - 1
  while (start < end):
    t = nums[end]
    nums[end] = nums[start]
    nums[start] = t
    start += 1
    end -= 1
  start = 0
  end = len(nums) - 1
  while (start < end):
    t = nums[end]
    nums[end] = nums[start]
    nums[start] = t
    start += 1
    end -= 1
  print nums

rotate([1,2,3,4,5,6,7], 3)
rotate2([1,2,3,4,5,6,7], 3)
