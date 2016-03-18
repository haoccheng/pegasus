# 5 LED -> hours 0-23.
# 6 LED -> minutes 0-59.

def init_hour(nbit): # generate all possible hours with nbits of 1.
  # either permutation.
  # or as choose n from N.
  # be sure cap at 0-23. 
 return []

# same strategy for minutes. pre-populate the table.
# Then, combine.

def choose(input, k):
  if k == 0:
    return []
  elif len(input) == k:
    return [input]
  elif k == 1:
    return [[e] for e in input]
  else:
    c1 = choose(input[1:], k)
    c2 = choose(input[1:], k-1)
    c2 = [[input[0]] + e for e in c2]
    return c1 + c2

print choose(range(5), 3)

