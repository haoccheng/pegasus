# happy number

def is_happy(n):
  s = str(n)
  hits = {}
  hits[s] = 1
  while (True):
    v = 0
    for c in s:
      v = v + int(c)*int(c)
    if v == 1:
      return True
    s = str(v)
    if s in hits:
      return False
    hits[s] = 1

print is_happy(2)
