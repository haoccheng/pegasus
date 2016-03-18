# KMP.

def kmp_table(W):
  T = [0] * len(W)
  T[0] = -1
  T[1] = 0
  pos = 2
  cnd = 0
  while (pos < len(W)):
    if W[pos-1] == W[cnd]:
      T[pos] = cnd + 1
      cnd += 1
      pos += 1
    elif cnd > 0:
      cnd = T[cnd]
    else:
      T[pos] = 0
      pos += 1
  return T

def kmp_search(S, W):
  T = kmp_table(W)
  m = 0
  i = 0
  while m + i < len(S):
    if W[i] == S[m+i]:
      if i == len(W) - 1:
        return m
      i += 1
    else:
      if T[i] > -1:
        m = m + i - T[i]
        i = T[i]
      else:
        i = 0
        m = m + 1

for s in ['abcdabd', 'xxxxxx']:
  print s, kmp_table(s), kmp_search('xxxabcdabd', s)
