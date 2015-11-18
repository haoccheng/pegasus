# Find the majority element in an array when exists.
# Majority is the element that occurs for more than half the size of the array.

# {1,2,3,2,2,2,5,4,2} -> 2
# majority -> median.
# Quickselect.

def swap(input, x, y):
  t = input[x]
  input[x] = input[y]
  input[y] = t

# find the right position of the pivot at position end.
def partition(input, start, end):
  pivot = input[end]
  i = start
  j = end - 1
  while (i < j):
    if input[i] <= pivot:
      i += 1
    elif input[j] >= pivot:
      j -= 1
    else:
      swap(input, i, j)
      i += 1
      j -= 1
  # either meet i==j, or j+1==i.
  if input[i] < pivot:
    swap(input, i+1, end)
    return i+1
  else:
    swap(input, i, end)
    return i

def majority(input):
  start = 0
  end = len(input) - 1
  median = (start + end) / 2
  while (True):
    pi = partition(input, start, end)
    if (pi == median):
      return input[pi]
    elif (pi < median):
      start = pi + 1
    else:
      end = pi - 1
    if (start == end): # start ~ median ~ end.
      return input[start]

t = [4, 5, 2, 3, 3]
print majority(t)
t = [20, 10, 5, 30, 15]
print majority(t)

