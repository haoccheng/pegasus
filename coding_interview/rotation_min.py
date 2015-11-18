# When some elements at the beginning of an array are moved to end,
# it becomes a rotation of the original array.
# Implement a function to get the minimum number in a rotation of an increasingly
# sorted array.
# {3,4,5,1,2} -> minimum of the rotation {1,2} = 1.

def rotation_min(input, start, end):
  mid = (start + end) / 2
  if (input[start] < input[mid]) and (input[mid] > input[end]):
    if (mid + 1 < end):
      return rotation_min(input, mid, end)
    else:
      return input[mid]
  elif (input[start] > input[mid]) and (input[mid] < input[end]):
    if (start + 1 < mid):
      return rotation_min(input, start, mid)
    else:
      return input[mid]
  else:
    raise RuntimeError('dead path')

t = [3,4,5,1,2]
print rotation_min(t, 0, len(t)-1)
t = [4,5,6,7,1,2,3]
print rotation_min(t, 0, len(t)-1)
