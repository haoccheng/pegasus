# citations are sorted.

def hindex(citations):
  if len(citations) == 0:
    return 0
  if citations[-1] == 0:
    return 0
  
  N = len(citations)
  h1 = 1
  h2 = N
  while (True):
    hm = (int)((h1 + h2) / 2)
    im = N - hm
    if citations[im] >= hm:
      h1 = hm
    else:
      h2 = hm
    if (h1 == h2):
      return h1
    elif (h1 + 1 == h2):
      p2 = N - h2
      if citations[p2] >= h2:
        return h2
      else:
        return h1

print hindex(sorted([3, 0, 6, 1, 5]))
