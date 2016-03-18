# search a target in rotated sorted array.

def locate_pivot(input, start, end):
  if start == end:
    return start
  elif start + 1 == end:
    return start if input[start] <= input[end] else end
  else:
    middle = (start + end) / 2
    if input[middle] > input[end]:
      return locate_pivot(input, middle, end)
    elif input[middle] < input[end]:
      return locate_pivot(input, start, middle)
    elif input[start] > input[middle]:
      return locate_pivot(input, start, middle)
    elif input[start] < input[middle]:
      return locate_pivot(input, start, middle)
    else:
      c1 = locate_pivot(input, start, middle)
      c2 = locate_pivot(input, middle, end)
      if input[c1] == input[c2]:
        return c2
      else:
        return c1 if input[c1] <= input[c2] else c2

input = [1, 1, 1, 1, 1, 1]
print input, locate_pivot(input, 0, len(input)-1)

input = [1, 1, 1, 4, 1, 1, 1]
print input, locate_pivot(input, 0, len(input)-1)

input = [1, 1, 1, 1, 1, 1, 1, 2]
print input, locate_pivot(input, 0, len(input)-1)

input = [1, 1, 1, 1, 1, 1, 9, 1, 1]
print input, locate_pivot(input, 0, len(input)-1)

input = [1, 1, 1, 1, 1, 1, 0, 1, 1]
print input, locate_pivot(input, 0, len(input)-1)
