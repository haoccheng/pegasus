# run length encoding
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# 12W1B12W3B24W1B14W

def rle(input):
  ret = ''
  prev_char = None
  prev_count = 0
  for c in input:
    if prev_char is None:
      prev_char = c
      prev_count = 1
    elif prev_char == c:
      prev_count += 1
    else:
      ret += ('%d%s' % (prev_count, prev_char))
      prev_char = c
      prev_count = 1
  if prev_char is not None:
    ret += ('%d%s' % (prev_count, prev_char))
  return ret

def rld(input):
  ret = ''
  count = ''
  for c in input:
    if c in '0123456789':
      count += c
    else:
      ret += (c * int(count))
      count = ''
  return ret

print rle('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')
print '12W1B12W3B24W1B14W'
print rld('12W1B12W3B24W1B14W')
print 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
