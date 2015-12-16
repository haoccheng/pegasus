# reverse digits of an integer.
# x=123 -> 321
# x=-123 -> -321
# corner case
# If x=10
# Input is 32-bit integer, the reverse of 1000000003 would cause overflow, return 0 in that case.

def reverse(x):
  sign = +1 if (x >= 0) else -1
  x = x if (x >= 0) else -x
  xs = str(x)
  y = 0
  for i in range(len(xs)-1, -1, -1):
    y = int(y * 10 + int(xs[i]))
    # Note: python int type range is much larger..
    if y > 2147483647: # largest positive 32 bit value.
      return 0
  return y if sign == +1 else -y
  

print reverse(123)
print reverse(-123)
print reverse(10)
print reverse(1000000000000003)
