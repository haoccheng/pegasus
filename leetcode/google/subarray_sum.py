# determine if there is a subarray sum to target. (positive integers).

def subarray_sum(input, target):
  start = 0
  end = start
  cumsum = input[start]
  com = []
  while (True):
    while (end < len(input)-1 and cumsum < target):
      end += 1
      cumsum += input[end]
    if cumsum == target:
      com.append(input[start:end+1])
      if start == end:
        start += 1
        end = start
        if start > len(input) - 1:
          break
        cumsum = input[start]
      else:
        cumsum -= input[start]
        start += 1
    while (start < len(input)-1 and cumsum > target):
      cumsum -= input[start]
      start += 1
    if end == len(input)-1 and cumsum < target:
      break
    if start == len(input)-1 and cumsum > target:
      break
  return com

print subarray_sum([1, 2, 3, 4, 3], 3)
print subarray_sum([1, 2, 3, 4, 1, 5, 10, 5, 5], 10)

