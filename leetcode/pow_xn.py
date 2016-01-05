def my_pow(x, n):
  if x == 0:
    return 0
  elif (n == 0):
    return 1.0
  
  pos = True if n > 0 else False
  n = n if pos == True else -n
  
  ret = 1
  v = n
  while (v > 0):
    x1 = x
    base = 1
    while (base + base <= v):
      x1 = x1 * x1
      base = base + base
    ret = ret * x1
    v = v - base
  
  return ret if pos == True else 1.0/ret

print my_pow(2, 1)
print my_pow(2, 4)
print my_pow(2, 7)
