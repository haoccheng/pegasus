# triangle: find the minimum path sum from top to bottom.
# Each step, you may move to adjacent numbers on the row below.

def pathsum(triangle):
  if len(triangle) == 0:
    return 0
  curr = [-1] * len(triangle)
  curr[0] = triangle[0][0]
  for i in range(1, len(triangle)):
    print curr
    next = [-1] * len(triangle)
    for j in range(len(triangle[i])):
      p1 = max(j-1, 0)
      p2 = min(j, i-1)
      next[j] = min(curr[p1], curr[p2]) + triangle[i][j]
    curr = next
  print curr

triangle = [[2], [3,4], [6,5,7], [4,1,8,3]]
pathsum(triangle)
