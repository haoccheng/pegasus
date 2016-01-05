# trailing zeros of factorial N!

def zeros(n):
  base = 5
  count = 0
  while (n >= base):
    count += (n / base)
    base = base * 5
  return count

for v in [5, 25, 100]:
  print zeros(v)
