# sort colors

def sortcolor(input, middle):
  i = 0
  j = 0
  k = len(input)-1
  while j <= k:
    if input[j] < middle:
      t = input[i]
      input[i] = input[j]
      input[j] = t
      i += 1
      j += 1
    elif input[j] > middle:
      t = input[k]
      input[k] = input[j]
      input[j] = t
      k -= 1
    else:
      j += 1

input = [2, 2, 1, 2, 1, 3, 2, 1, 3, 3, 1]
print input
sortcolor(input, 2)
print input
