# search a target in rotated sorted array.

def locate_pivot(input):
  start = 0
  end = len(input) - 1
  print input
  while (start <= end):
    if start == end:
      return start
    elif start + 1 == end:
      return start if input[start] < input[end] else end
    else:
      middle = (start + end) / 2
      if input[middle] > input[end]:
        start = middle
      elif input[middle] < input[end]:
        end = middle

def rotate_search(input, target):
  pivot = locate_pivot(input)
  start = None
  end = None
  if pivot == 0:
    if input[0] <= target and target <= input[-1]:
      start = 0
      end = len(input)-1
  else:
    if input[0] <= target and target <= input[pivot-1]:
      start = 0
      end = pivot-1
    elif input[pivot] <= target and target <= input[-1]:
      start = pivot
      end = len(input)-1
  if start is None:
    return None
  while (start <= end):
    if start == end:
      if input[start] == target:
        return start
    elif start + 1 == end:
      if input[start] == target:
        return start
      elif input[end] == target:
        return end
    else:
      middle = (start + end) / 2
      if input[middle] == target:
        return middle
      elif input[middle] < target:
        start = middle + 1
      else:
        end = middle - 1
  return None

print rotate_search([5,6,1,2,3,4], 2)
print rotate_search([5,6,1,2,3,4], 0)

