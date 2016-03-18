# get the longest consecutive substring of two distinct characters.
# print all substrings.
# yellow -> [ell, llo]

def twoletter(input):
  output = []
  outlen = 0

  c1 = None
  c2 = None
  c1pos = 0
  c2pos = 0

  curr_start = 0
  curr_len = 0
  for i in range(len(input)):
    cc = input[i]
    if (c1 is None) and (c2 is None):
      c1 = cc
      c1pos = i
      curr_len += 1
    elif (c2 is None):
      if c1 == cc:
        curr_len += 1
      else:
        c2 = cc
        c2pos = i
        curr_len += 1
    else:
      if cc == c1:
        curr_len += 1
        if c1pos < c2pos:
          c1pos = i
      elif cc == c2:
        curr_len += 1
        if c2pos < c1pos:
          c2pos = i
      else:
        if c1pos < c2pos:
          curr_start = c2pos
          c1 = cc
          c1pos = i
          curr_len = i - curr_start + 1
        else:
          curr_start = c1pos
          c2 = cc
          c2pos = i
          curr_len = i - curr_start + 1
    if curr_len == outlen:
      output.append(input[curr_start:curr_start+curr_len])
    elif curr_len > outlen:
      outlen = curr_len
      output = [input[curr_start:curr_start+curr_len]]
  return output

print twoletter('yellow')
print twoletter('abcdefg')
print twoletter('yellollwwa')
print twoletter('yellollwwlll')
