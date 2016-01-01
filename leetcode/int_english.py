# 123 -> "One Hundred Twenty Three"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

def int1k(num):
  d1map = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
  d1xmap = {10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
  d2map = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
  s = []
  if num >= 100:
    v = num / 100
    s.append(d1map[v] + ' Hundred')
  num = num % 100
  if (num == 0):
    1
  elif (num > 0) and (num < 10):
    s.append(d1map[num])
  elif num >= 10 and num <= 19:
    s.append(d1xmap[num])
  else:
    v = num / 10
    s.append(d2map[v])
    v = num % 10
    if v > 0:
      s.append(d1map[v])
  return ' '.join(s)

def int_english(num):
  v = num
  s = []
  base = ''
  if num == 0:
    return 'Zero'
  while v > 0:
    r = v % 1000
    v = v / 1000
    e = int1k(r)
    if (e != '') and (base != ''):
      e = e + ' ' + base
    if e != '':
      s.insert(0, e)
    if base == '':
      base = 'Thousand'
    elif base == 'Thousand':
      base = 'Million'
    elif base == 'Million':
      base = 'Billion'
  return ' '.join(s)

for v in [9, 99, 999, 9999, 99999, 999999, 999999, 9999999, 99999999, 999999999, 9999999999]:
  print int_english(v)
