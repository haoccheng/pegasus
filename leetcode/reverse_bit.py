# reverse bits of 32-bits unsigned integer.

def reverse_bits(n):
  ret = 0
  for i in range(32):
    bit = (1 << i)
    if (n & bit) != 0:
      ret = ret | (1 << (31-i))
  return ret

print reverse_bits(43261596)
