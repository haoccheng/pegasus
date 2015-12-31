# a message containing letters from A-Z is encoded as below
# A:1, B:2 .. Z:26
# Given an encoded message, determine the total number of ways to decode it.
# Example: '12' two ways to decode 'AB' or 'L'

def decode_ways_recursive(s):
  if len(s) == 0:
    return 0
  elif s[0] == '0':
    return 0
  elif len(s) == 1:
    return 1
  else:
    # route 1.
    r1 = decode_ways_recursive(s[1:])
    # route 2.
    r2 = 0
    s12 = int(s[0:2])
    if (s12 >= 1) and (s12 <= 26):
      if len(s) > 2:
        r2 = decode_ways_recursive(s[2:])
      else:
        r2 = 1
    return r1 + r2

def decode_ways_iterative(s):
  if len(s) == 0:
    return 0
  elif s[0] == '0':
    return 0
  elif len(s) == 1:
    return 1
  else:
    d2 = 1
    d1 = 1
    for i in range(1, len(s)):
      d0 = None
      if s[i] == '0':
        if (s[i-1] == '1') or (s[i-1] == '2'):
          d0 = d2
        else:
          return 0
      else:
        if (s[i-1] == '0'):
          d0 = d1
        elif (s[i-1] == '1'):
          d0 = d1 + d2
        elif (s[i-1] == '2') and (s[i] in '1234560'):
          d0 = d1 + d2
        else:
          d0 = d1
      d2 = d1
      d1 = d0
    return d1

for s in ['1', '12', '102', '122']:
  print s, decode_ways_recursive(s), decode_ways_iterative(s)
