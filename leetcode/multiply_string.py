# Given two numbers represented as strings, return mulplications of the numbers as string.
# numbers are arbitrary long and non-negative.

def multiply(num1, num2):
  if len(num1) == 0 or len(num2) == 0:
    return ''
  num1 = [int(e) for e in num1]
  num2 = [int(e) for e in num2]
  ret = [0]
  for i in range(len(num1)):
    for j in range(len(num2)):
      zlen = len(num1)-1-i + len(num2)-1-j
      v1 = num1[i]
      v2 = num2[j]
      vs = [int(e) for e in str(v1 * v2)] + [0] * zlen    
      carry = 0
      r = []
      m = len(ret)-1
      n = len(vs) - 1
      while (m >= 0) and (n >= 0):
        s = carry + ret[m] + vs[n]
        carry = 1 if s >= 10 else 0
        s0 = s - 10 if s >= 10 else s
        r.insert(0, s0)
        m -= 1
        n -= 1
      while (m >= 0):
        s = carry + ret[m]
        carry = 1 if s >= 10 else 0
        s0 = s - 10 if s >= 10 else s
        r.insert(0, s0)
        m -= 1
      while (n >= 0):
        s = carry + vs[n]
        carry = 1 if s >= 10 else 0
        s0 = s - 10 if s >= 10 else s
        r.insert(0, s0)
        n -= 1
      if carry > 0:
        r.insert(0, carry)
      ret = r
  start = 0
  while (ret[start] == 0) and (start < len(ret)-1):
    start += 1
  ret = ret[start:]
  ret = [str(e) for e in ret]
  return ret

print multiply('123', '1')
print multiply('123', '10')
print multiply('123', '5')
print multiply('0', '0')
