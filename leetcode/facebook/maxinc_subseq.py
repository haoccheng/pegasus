# max increasing subsequence in an array
# {9, 15, 11, 3, 12, 10}
# {9, 11, 12}

def maxinc_subseq(input):
  cache = []
  for v in input:
    if len(cache) == 0:
      cache.append((1, v, [v])) # (length, end, seq)
    else:
      start = None
      for i in range(len(cache)-1, -1, -1):
        if cache[i][1] < v:
          start = i
          break
      if start == len(cache)-1:
        (l, e, seq) = cache[-1]
        cache.append((l+1, v, seq + [v]))
      elif start is None:
        cache[0] = (1, v, [v])
      else:
        (l, e, seq) = cache[start]
        if cache[start+1][1] > v:
          cache[start+1] = (l+1, v, seq + [v])
  print cache

maxinc_subseq([9, 15, 11, 3, 12, 10])
    
