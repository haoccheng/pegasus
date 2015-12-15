# if an element at the left side is greater than another element at the right side,
# form a reverse pairs in an array. Count the total number of reversed pairs.
# {7, 6, 5, 4} -> (7,6), (7,5), (7,4), (6,5), (6,4), (5,4)

def swap(input, p1, p2):
  t = input[p1]
  input[p1] = input[p2]
  input[p2] = t

def reverse_pair_count(input, start, end):
  if start >= end:
    return 0
  elif start + 1 == end:
    if input[start] > input[end]:
      swap(input, start, end)
      return 1
    else:
      return 0
  else:
    mid = (start + end) / 2
    c1 = reverse_pair_count(input, start, mid)
    c2 = reverse_pair_count(input, mid+1, end)
    c3 = 0
    i = start
    j = mid+1
    buffer = []
    while (i <= mid) and (j <= end):
      if input[i] < input[j]:
        buffer.append(input[i])
        i += 1
        c3 = c3 + (j - (mid+1) + 1 - 1)
      else:
        buffer.append(input[j])
        j += 1
    while (i <= mid):
      buffer.append(input[i])
      i += 1
      c3 = c3 + (end - (mid+1) + 1)
    while (j <= end):
      buffer.append(input[j])
      j += 1
    for i in range(len(buffer)):
      input[start + i] = buffer[i]
    return c1 + c2 + c3

def test():
  input = [7, 6, 5, 4]
  print input, reverse_pair_count(input, 0, len(input)-1)

  input = [1]
  print input, reverse_pair_count(input, 0, len(input)-1)

  input = [3, 5, 2, 6]
  print input, reverse_pair_count(input, 0, len(input)-1)
test()
