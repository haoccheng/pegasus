# merge sort.

def merge_sort(input, start, end, buffer):
  count = end - start + 1
  if count == 1:
    return
  elif count == 2:
    if input[start] > input[end]:
      t = input[start]
      input[start] = input[end]
      input[end] = t
  else:
    middle = (start + end) / 2
    merge_sort(input, start, middle, buffer)
    merge_sort(input, middle+1, end, buffer)
    i = start
    j = middle + 1
    index = start
    while (i <= middle) and (j <= end):
      if input[i] < input[j]:
        buffer[index] = input[i]
        i += 1
      else:
        buffer[index] = input[j]
        j += 1
      index += 1
    while (i <= middle):
      buffer[index] = input[i]
      i += 1
      index += 1
    while (j <= end):
      buffer[index] = input[j]
      j += 1
      index += 1
    for i in range(start, end+1):
      input[i] = buffer[i]

input = [1, 2, 3, 9, 8, 7, 6, 5, 4]
buffer = [0] * len(input)
merge_sort(input, 0, len(input)-1, buffer)
print input
  
