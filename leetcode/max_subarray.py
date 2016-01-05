# maximum subarray.

def max_subarray(nums):
  scores = [0] * len(nums)
  start = [-1] * len(nums)
  scores[0] = nums[0]
  start[0] = 0
  for i in range(1, len(nums)):
    o1 = scores[i-1] + nums[i]
    o2 = nums[i]
    if o1 > o2:
      start[i] = start[i-1]
      scores[i] = o1
    else:
      start[i] = i
      scores[i] = o2
  max_index = None
  for i in range(len(scores)):
    if max_index is None:
      max_index = i
    else:
      if scores[i] > scores[max_index]:
        max_index = i
  return scores[max_index]

print max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
