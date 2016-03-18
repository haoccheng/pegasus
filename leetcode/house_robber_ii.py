# house robber ii.
# https://leetcode.com/problems/house-robber-ii/

def rob(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) == 1:
    return nums[0]
  r1_rob = [0] * len(nums)
  r1_norob = [0] * len(nums)
  nr1_rob = [0] * len(nums)
  nr1_norob = [0] * len(nums)
  r1_rob[0] = nums[0]
  for i in range(1, len(nums)):
    r1_norob[i] = max(r1_norob[i-1], r1_rob[i-1])
    r1_rob[i] = r1_norob[i-1] + nums[i]
  r1_rob[-1] = 0
  for i in range(1, len(nums)):
    nr1_norob[i] = max(nr1_norob[i-1], nr1_rob[i-1])
    nr1_rob[i] = nr1_norob[i-1] + nums[i]
  return max(r1_rob[-1], r1_norob[-1], nr1_rob[-1], nr1_norob[-1])

print rob([3, 5, 4, 1, 2])
  
