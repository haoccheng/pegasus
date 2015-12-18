# Given two binary strings, return sum (also a binary string).
# a = '11'
# b = '1'
# return '100'

def value_binary(v, ret):
  if v == 0:
    ret = '0' + ret
    carry = 0
  elif v == 1:
    ret = '1' + ret
    carry = 0
  elif v == 2:
    ret = '0' + ret
    carry = 1
  elif v == 3:
    ret = '1' + ret
    carry = 1
  return (ret, carry)

def add_binary(a, b):
  carry = 0
  ret = ''
  ai = len(a) - 1
  bi = len(b) - 1
  while (ai >= 0) and (bi >= 0):
    av = int(a[ai])
    bv = int(b[bi])
    v = av + bv + carry
    (ret, carry) = value_binary(v, ret)
    ai -= 1
    bi -= 1
  while (ai >= 0):
    av = int(a[ai])
    v = av + carry
    (ret, carry) = value_binary(v, ret)
    ai -= 1
  while (bi >= 0):
    bv = int(b[bi])
    v = bv + carry
    (ret, carry) = value_binary(v, ret)
    bi -= 1
  if carry == 1:
    ret = '1' + ret
  return ret

print add_binary('11', '1')
