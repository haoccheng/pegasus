# Given two integers n/k, return all possible combinations of k numbers out of 1..n

def combine(n, k):
  if (n == 0) or (k == 0):
    return []
  elif (n == k):
    return [range(1,n+1)]
  elif (k == 1):
    return [[e] for e in range(1,n+1)]
  bit = [0] * (n-k) + [1] * k
  
  ret = []
  while (True):
    row = []
    for i in range(len(bit)):
      if bit[len(bit)-1-i] == 1:
        row.append(i+1)
    ret.append(row)

    pivot = len(bit) - 1
    bit1 = 0
    for i in range(len(bit)-1, -1, -1):
      if bit[i] == 1:
        bit1 += 1
      if i == 0:
        pivot = 0
        break
      else:
        if (bit[i] == 1) and (bit[i-1] == 0):
          pivot = i
          break
    if pivot == 0:
      break
    bit[pivot-1] = 1
    for i in range(pivot, len(bit)):
      bit[i] = 0
    for i in range(bit1-1):
      bit[len(bit)-1-i] = 1
  return ret

print combine(4, 2)
