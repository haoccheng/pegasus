def ugly(num):
  if num == 0:
    return False
  while (num % 2 == 0):
    num = num / 2
  while (num % 3 == 0):
    num = num / 3
  while (num % 5 == 0):
    num = num / 5
  if num == 1:
    return True
  return False

for v in [2, 3, 5, 6, 8, 14]:
  print v, ugly(v)
