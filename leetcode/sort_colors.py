# array of n objects in red/white/blue, sort them so that objects of same color
# are adjacent, in order red/white/blue.
# 0/1/2 represent red/white/blue.

def sort_color(nums):
  h0 = 0
  h1 = 0
  h2 = 0
  for v in nums:
    if v == 0:
      h0 += 1
    elif v == 1:
      h1 += 1
    elif v == 2:
      h2 += 1
  x = 0
  for i in range(h0):
    nums[x] = 0
    x += 1
  for i in range(h1):
    nums[x] = 1
    x += 1
  for i in range(h2):
    nums[x] = 2
    x += 1
