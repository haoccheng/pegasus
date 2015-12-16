# roman numeral -> integer.
# Input is within range of 1-3999

# roman numeral
# I, II, III, IV, V, VI, VII, VIII, IX, X
# V: 5
# X: 10
# L: 50
# C: 100
# D: 500
# M: 1000
# I placed before V/X indicate one less.
# X placed before L/C indicate ten less.
# C placed before D/M indicate hundred less.
# 1954: MCMLIV
# 1990: MCMXC
# 2014: MMXIV

def roman_int(input):
  roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
  stack = []
  value = 0
  for c in input:
    vc = roman[c]
    if len(stack) == 0:
      stack.append(vc)
    else:
      sc = stack[-1]
      if vc == sc:
        stack.append(vc)
      elif vc < sc:
        for sc in stack:
          value += sc
        stack = []
        stack.append(vc)
      else:
        value += vc
        for sc in stack:
          value -= sc
        stack = []
  for sc in stack:
    value += sc
  return value

for r in ['MCMLIV', 'MCMXC', 'MMXIV']:
  print roman_int(r)
