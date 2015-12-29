# A valid additive sequence should contain at least 3 numbers.
# Except for the first two, each subsequent number in the sequence must be
# the sum of the preceding two.
# 112358 -> 1+1=2, 1+2=3, 2+3=5, 3+5=8
# 199100199 -> 1+99=100, 99+100=199.

def check(num, v1, v2):
  x1 = v1
  x2 = v2
  sc = str(x1) + str(x2)
  while (True):
    x3 = x1 + x2
    sc = sc + str(x3)
    if len(sc) > len(num):
      return False
    elif len(sc) == len(num):
      if sc == num:
        return True
      else:
        return False
    else:
      if (sc != num[:len(sc)]):
        return False
      x1 = x2
      x2 = x3

def is_additive_number(num):
  for x in range(0, len(num)):
    s1 = num[:(x+1)]
    v1 = int(s1)
    if str(v1) != s1:
      continue
    for y in range(x+1, len(num)):
      s2 = num[(x+1):(y+1)]
      v2 = int(s2)
      if str(v2) != s2:
        continue
      if check(num, v1, v2):
        return True
  return False

print is_additive_number('112358')
print is_additive_number('199100199')
print is_additive_number('111')
