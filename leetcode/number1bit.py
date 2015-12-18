# Write a function that take an unsigned integer and return number of 1bit.
# 

def hamming_weight(n):
  check = 1
  count = 0
  for i in range(32):
    c = check << i
    if (n & c) > 0:
      count += 1
  return count

print hamming_weight(11)
