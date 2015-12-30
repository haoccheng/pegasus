# https://leetcode.com/problems/trapping-rain-water/

def trap(height):
  left_height = [0] * len(height)
  right_height = [0] * len(height)

  for i in range(len(height)):
    if i == 0:
      left_height[0] = height[0]
    else:
      left_height[i] = max(height[i], left_height[i-1])
  for i in range(len(height)-1, -1, -1):
    if i == len(height)-1:
      right_height[i] = height[i]
    else:
      right_height[i] = max(height[i], right_height[i+1])
  count = 0
  for i in range(len(height)):
    mh = min(left_height[i], right_height[i])
    count += (mh - height[i])
  return count

print trap([0,1,0,2,1,0,1,3,2,1,2,1])
