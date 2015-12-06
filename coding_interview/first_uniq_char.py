# Find the first character in a string that only appeared once.
# 'google' -> 'l'

def first_unique_char(input):
  index = {}
  for i in range(len(input)):
    c = input[i]
    if c in index:
      index[c] = -1 # reset
    else:
      index[c] = i
  mi = len(input)
  for k,v in index.items():
    if (v > 0) and (v < mi):
      mi = v
  if mi == len(input):
    return None
  return input[mi]

def test():
  print first_unique_char('google')
  print first_unique_char('sales')

test()
