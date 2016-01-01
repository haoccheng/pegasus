# divide two integers (no */%)

def divide(dividend, divisor):
  if dividend == 0:
    return 0
  elif divisor == 0:
    return 2147483647
  sign = +1 if ((dividend > 0) and (divisor > 0)) or ((dividend < 0) and (divisor < 0)) else -1
  a = dividend if (dividend > 0) else -dividend
  b = divisor if (divisor > 0) else -divisor
  v = 0
  while (a >= b):
    b1 = b
    v1 = 1
    while (a >= b1 + b1):
      b1 = b1 + b1
      v1 = v1 + v1
    v = v + v1
    a = a - b1
  v = v if sign == 1 else -v
  v = int32(v)
  return v

print divide(5, 2)
print divide(18, 2)
print divide(37, 2)
print divide(63, 2)
print divide(1, 1)
print divide(31, 1)
print divide(1, -1)
