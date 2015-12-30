# text justification.
# https://leetcode.com/problems/text-justification/

def justify(words, max_width):
  start = 0
  row = []
  r1 = []
  while (start < len(words)):
    if len(row) == 0:
      row.append(words[start]) # assume no word is longer than max_width
      start += 1
    else:
      v = sum([len(e) for e in row]) + len(words[start]) + len(row)
      if v <= max_width:
        row.append(words[start])
        start += 1
      else:
        r1.append(row)
        row = []
  if len(row) > 0:
    r1.append(row)
  # justify.
  ret = []
  for irow in range(len(r1)):
    row = r1[irow]
    if irow == len(r1)-1:
      s = ' '.join(row)
      s = s + ' '*(max_width - len(s))
      ret.append(s)
    else:
      if len(row) == 1:
        ret.append(row[0] + (' ' * (max_width - len(row[0]))))
      else:
        ns = max_width - sum([len(e) for e in row])
        ns1 = (int)(ns / (len(row)-1))
        ns0 = ns - (len(row)-1) * ns1
        s = row[0]
        for i in range(1, len(row)):
          if i <= ns0:
            s = s + ' '*ns1 + ' ' + row[i]
          else:
            s = s + ' '*ns1 + row[i]
        ret.append(s)
  return ret

#rs = justify(["This", "is", "an", "example", "of", "text", "justification."], 16)
#rs = justify(["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."], 30)
#rs = justify([''], 2)
rs = justify(['a', 'b', 'c', 'd', 'e'], 3)
for r in rs:
  print '[%s]' % r
