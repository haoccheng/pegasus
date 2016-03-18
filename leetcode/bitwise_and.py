# Given a range [m, n] where 0 <= m <= n <= 2147483647,
# return the bitwise AND of all numbers in this range, inclusive.

def bitwise(m):
  mask = [0] * 32
  value = m
  for offset in range(32):
    if value == 0:
      break
    base = (2 << offset)
    b1 = value / base * (base / 2)
    b2 = max(value % base - (base / 2 - 1), 0)
    bc = b1 + b2
    if bc == 0:
      break
    mask[offset] = bc
  return mask

def range_bitwise(m, n):
  mask_m = bitwise(m-1) if m > 0 else [0] * 32
  mask_n = bitwise(n)
  mask = [0] * 32
  for i in range(len(mask)):
    mask[i] = mask_n[i] - mask_m[i]
  final = 0
  count = n - m + 1
  for i in range(len(mask)):
    if mask[i] == count:
      final = final | (1 << i)
  return final

def range_bitwise2(m, n):
  final = m
  for v in range(m+1, n+1):
    final = final & v
  return final

for i in range(20):
  for j in range(i, 20):
    v1 = range_bitwise(i, j)
    v2 = range_bitwise2(i, j)
    if v1 != v2:
      print i, j, v1, v2
