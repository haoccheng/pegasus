# print all permutations of a given string.
#
# At each variation, permute to the next immediate large value.
# 01234 -> next number -> 01243 -..

def next_number(input):
  curr = len(input) - 1
  for i in range(len(input)-2, -1, -1):
    if input[i] > input[curr]:
      curr = i
    else:
      break
  if curr == 0:
    return None # end of permutation.
  prev = curr - 1
  swap = None
  for i in range(len(input)-1, curr-1, -1):
    if input[i] > input[prev]:
      swap = i
      break
  t = input[prev]
  input[prev] = input[swap]
  input[swap] = t
  start = curr
  end = len(input) - 1
  while (start < end):
    t = input[start]
    input[start] = input[end]
    input[end] = t
    start += 1
    end -= 1
  return input

def permute(input):
  n = input
  while (n is not None):
    print n
    n = next_number(n)

permute(list('012'))
