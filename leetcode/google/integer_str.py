# convert integer to string. 1000 -> one thousand.

def int2str10(value):
  if (value > 0) and (value < 10):
    m = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    return [m[value]]

def int2str100(value):
  if (value > 0) and (value < 10):
    return int2str10(value)
  elif (value >= 10) and (value < 20):
    m = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
    return [m[value]]
  elif (value >= 20) and (value < 100):
    v1 = value / 10
    v2 = value % 10
    m = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
    if v2 == 0:
      return [m[v1]]
    else:
      return [m[v1]] + int2str10(v2)

def int2str1000(value):
  if (value > 0) and (value < 100):
    return int2str100(value)
  elif (value >= 100) and (value < 1000):
    v1 = value / 100
    v2 = value % 100
    if v2 == 0:
      return int2str10(v1) + ['hundred']
    else:
      return int2str10(v1) + ['hundred'] + int2str100(v2)
  return []

def int2str(value):
  bases = ['', 'thousand', 'million', 'billion']
  out = []
  for base in bases:
    if value == 0:
      break
    v1 = value / 1000
    v2 = value % 1000
    s2 = int2str1000(v2)
    if len(s2) > 0:
      if len(base) > 0:
        out = s2 + [base] + out
      else:
        out = s2 + out
    value = v1
  return out

for value in [1, 11, 111, 1111, 11111, 999999, 9999999, 99999999, 9999000000]:
  print value, int2str(value)
