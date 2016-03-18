# substring with k unique characters.
# google, k=2 -> goog

def substrk(input, k):
  hit = {}
  start = 0
  clen = 0
  candidate = None
  for i in range(len(input)):
    c = input[i]
    if c not in hit:
      if len(hit) < k:
        hit[c] = i
        clen += 1
        if candidate is None:
          candidate = (clen, start)
        elif clen > candidate[0]:
          candidate = (clen, start)
      else:
        check = sorted(hit.items(), key=lambda e:e[1]) # char/position.
        del hit[check[0][0]]
        start = check[1][1]
        clen = i - start + 1
        hit[c] = i
    else:
      prev = input[i-1]
      if prev != c:
        hit[c] = i
      clen += 1
      if candidate is None:
        candidate = (clen, start)
      elif clen > candidate[0]:
        candidate = (clen, start)
  print input, input[candidate[1]:candidate[1]+candidate[0]]

substrk('google', 2)
substrk('walmart', 2)
substrk('todotodo', 3)

