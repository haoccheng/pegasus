# gray code is a binary numeral system where two successive values differ in only one bit.
# Given a non-negative integer n representing the total number of bits in the code.
# print the sequence of gray code, start with 0.
# n=2 -> 00 -> 01 -> 11 -> 10. Return [0, 1, 3, 2]

def next_permute(curr, hits):
  for i in range(len(curr)-1, -1, -1):
    next = curr[:i]
    if curr[i] == '0':
      next = next + '1'
    else:
      next = next + '0'
    next = next + curr[i+1:]
    if next not in hits:
      hits[next] = 1
      return next
  return None

def bin2int(input):
  v = 0
  base = 1
  for i in range(len(input)-1, -1, -1):
    if input[i] == '1':
      v = v + base
    base = base * 2
  return v

def gray_code(n):
  curr = '0' * n
  hits = {}
  ret = []
  hits[curr] = 1
  while (True):
    ret.append(curr)
    curr = next_permute(curr, hits)
    if curr is None:
      break
  ret = [bin2int(e) for e in ret]
  return ret

print gray_code(1)
print gray_code(2)
print gray_code(3)

