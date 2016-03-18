# quick sort.

def quicksort(input, start, end):
  count = end - start + 1
  if count <= 1:
    return
  elif count == 2:
    if input[start] > input[end]:
      t = input[start]
      input[start] = input[end]
      input[end] = t
  else:
    pivot = input[start]
    i = start + 1
    j = end
    while (i < j):
      if input[i] < pivot:
        i += 1
      elif input[j] > pivot:
        j -= 1
      else:
        t = input[i]
        input[i] = input[j]
        input[j] = t
        i += 1
        j -= 1
    middle = i if input[i] < pivot else i-1
    input[start] = input[middle]
    input[middle] = pivot
    quicksort(input, start, middle-1)
    quicksort(input, middle+1, end)

input = [1, 2, 3, 6, 5, 4]
quicksort(input, 0, len(input)-1)
print input
input = [1, 2, 3, 6, 5, 4, 9, 0, 7, 8, 0]
quicksort(input, 0, len(input)-1)
print input
