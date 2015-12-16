# given an integer, convert to roman numeral.
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

import math

def base_roman(curr, exp):
  if curr == 0:
    return ''
  d1 = None
  d5 = None
  d10 = None
  if exp == 1:
    d1 = 'I'
    d5 = 'V'
    d10 = 'X'
  elif exp == 10:
    d1 = 'X'
    d5 = 'L'
    d10 = 'C'
  elif exp == 100:
    d1 = 'C'
    d5 = 'D'
    d10 = 'M'
  elif exp == 1000:
    d1 = 'M'
  if curr <= 3:
    s = d1 * curr
  elif (curr <= 5):
    s = d1 * (5-curr) + d5
  elif (curr <= 8):
    s = d5 + d1 * (curr - 5)
  else:
    s = d1 * (10 - curr) + d10
  return s

def int_to_roman(num):
  exp = (int)(math.log(num) / math.log(10))
  exp10 = (int)(math.pow(10, exp))
  r = num
  roman = ''
  for i in range(exp, -1, -1):
    c = (int)(r / exp10)
    roman = roman + base_roman(c, exp10)
    r = r - c * exp10
    exp10 = exp10 / 10
  return roman

print 'MCMLIV', int_to_roman(1954)
print 'MCMXC', int_to_roman(1990)
print 'MMXIV', int_to_roman(2014)

