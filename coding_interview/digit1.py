# How many times does the digit 1 occur in the integers from 1 to n?
# If n = 12, appears at 1, 10, 11, 12. Total, 5 times.

import math

def digit1_bruteforce(value):
  count = 0
  for i in range(1, value+1):
    s = str(i)
    s1 = [e for e in s if e == '1']
    count += len(s1)
  return count


class Digit1:
  def __init__(self):
    self.c10n = [0] * 10
    self.c10n[1] = 1
    for i in range(2, len(self.c10n)):
      self.c10n[i] = int(10 * self.c10n[i-1] + math.pow(10, i-1))

  def decompose(self, value):
    if (value == 0):
      return 0
    exp = (int)(math.log(value) / math.log(10))
    if (exp == 0):
      if value == 0:
        return 0
      else:
        return 1
    else:
      inc = (int)(math.pow(10, exp))
      count = 0
      cc = 0
      r = value
      while (r >= inc):
        r = r - inc
        cc += 1
        count = count + self.c10n[exp]
      if (cc >= 2):
        count = count + int(math.pow(10, exp))
      elif (cc == 1):
        count = count + (value - int(math.pow(10, exp)) + 1)
      rc = self.decompose(r)
      count += rc
      return count

d = Digit1()
for i in [9, 99, 150, 999, 1634, 1999, 3145]:
  print digit1_bruteforce(i), d.decompose(i)
