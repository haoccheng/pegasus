# pow(x, y)

def pow1(x, y):
  if y == 0:
    return 1
  elif x < 0.0000001:
    return 0 if y > 0 else None
  elif y < 0:
    v = pow1(x, -y)
    return 1.0 / v
  
  final = 1
  power = y
  while (power > 0):
    base = 1
    value = x
    while (base + base <= power):
      base = base + base
      value = value * value
    power -= base
    final = final * value
  return final

print pow1(2, 5)
print pow1(2, 19)
print pow1(2, 6)

