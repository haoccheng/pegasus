# generate all combination of a given string.
# Combination of 'abc' -> 'a', 'b', 'c', 'ab', 'bc', 'ac', 'abc'

# bit representation. 000 -> 001 ..
# only thing to watch out is for arbitrary length of string.
# This calls for a BigInt implementation.

class BigInt:
  def __init__(self):
    self.bits = ['1']

  def next(self): # increment by 1.
    carry = 1
    for i in range(len(self.bits)):
      if (self.bits[i] == '0'):
        if (carry == 0):
          1 # noop.
        else:
          self.bits[i] = '1'
          carry = 0
      else: # bit == 1
        if (carry == 0):
          1 # noop.
        else:
          self.bits[i] = '0'
          carry = 1
    if carry == 1:
      self.bits.append('1')

  def pt(self):
    print self.bits

class Combination:
  def __init__(self, chars):
    self.chars = chars
    self.i = BigInt()

  def pt(self):
    seq = []
    for i in range(len(self.i.bits)):
      if (self.i.bits[i] == '1'):
        seq.append(self.chars[i])
    print seq

  def next(self):
    if (len(self.i.bits) <= len(self.chars)):
      self.i.next()
      if len(self.i.bits) > len(self.chars):
        return False
      else:
        return True
    else:
      return False

def test():
  c = Combination('abcd')
  while (True):
    c.pt()
    n = c.next()
    if n == False:
      break

test()
