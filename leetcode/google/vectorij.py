# given a vector, find a pair i/j, such that a[j] = a[i] + 1 and j - i is maximized.
# Next: a[j] > a[i].

def examine_vector(input):
  hit = {}
  candidate = None
  for i in range(len(input)):
    vi = input[i]
    if (vi - 1) in hit:
      pd = i - hit[vi-1] + 1
      if candidate is None:
        candidate = (pd, hit[vi-1], i)
      elif pd > candidate[0]:
        candidate = (pd, hit[vi-1], i)
    hit[vi] = i
  print candidate

examine_vector([1, 3, 2, 5, 4, 2])

# a[j] > a[i]
# [1, 3, 2, 0, 5, 4, 2]
# nlogn
def examine_vector2(input):
  cache = []
  cache.append((input[0], 0))
  candidate = None
  for j in range(1, len(input)):
    vj = input[j]
    # compute a[j] > a[i] and maximum distance. can be changed to binary search.
    for (vi, i) in cache:
      if vi < vj:
        pd = j - i + 1
        if candidate is None:
          candidate = (pd, i, j)
        elif pd > candidate[0]:
          candidate = (pd, i, j)
      else:
        break
    # update cache.
    if vj < cache[-1][0]:
      cache.append((vj, j))
  print input
  print cache
  print candidate

examine_vector2([1, 3, 2, 0, 5, 4, 2])
