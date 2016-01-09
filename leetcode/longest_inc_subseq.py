# longest increasing subsequences.

def lis(nums):
  if len(nums) == 0:
    return 0
  scores = [1] * len(nums)
  for i in range(len(nums)-1, -1, -1):
    vi = nums[i]
    s = 1
    for j in range(i+1, len(nums)):
      vj = nums[j]
      if vi < vj:
        sj = 1 + scores[j]
        s = max(s, sj)
    scores[i] = s
  return max(scores)

def lis2(nums):
  if len(nums) == 0:
    return 0
  scores = [-1] * len(nums)
  scores[0] = nums[0]
  N = 0
  for i in range(1, len(nums)):
    if nums[i] > scores[N]:
      N += 1
      scores[N] = nums[i]
    else:
      index = -1
      for j in range(0, N+1):
        if scores[j] > nums[i]:
          index = j
          break
      if index != -1:
        scores[index] = nums[i]
  return N+1

print lis([10, 9, 2, 5, 3, 7, 101, 18, 5])
print lis2([10, 9, 2, 5, 3, 7, 101, 18, 5])
