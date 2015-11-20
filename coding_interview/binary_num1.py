# Implement a function to get the number of 1s in the binary representation of an integer.
# 9 : 1001 in binary. -> 2.

# integer 32-bit.
def count1(input):
  count = 0
  for i in range(32):
    bit = (1 << i)
    v = input & bit
    if v != 0:
      count += 1
  return count

print count1(0)
print count1(1)
print count1(3)
print count1(9)
