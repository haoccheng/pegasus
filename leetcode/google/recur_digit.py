# recuring digit.
# 1/2 = 0.5
# 2/3 = 0.(6)
# 2/1 = 2

def recur(numer, denom):
  ret = str(numer / denom)
  remain = numer % denom
  if remain > 0:
    ret += '.'
  else:
    return ret
  hit = {}
  while True:
    if remain in hit:
      ret2 = ret[:hit[remain]] + '(' + ret[hit[remain]:] + ')'
      return ret2
    else:
      hit[remain] = len(ret)
      value = remain * 10
      ret += str(value / denom)
      remain = value % denom
      if remain == 0:
        return ret

print recur(1, 3)
print recur(2, 3)
print recur(200, 3)
print recur(4, 2)
print recur(3, 6)
print recur(1, 40)
print recur(0, -1)
