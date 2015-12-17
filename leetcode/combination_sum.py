# {2,3,6,7}, target=7
# Any unique combinations, numbers are allowed to repeat multiple times.
# [7], [2,2,3]

# possible approaches. dynamic programming; another way would be expansion.

def combination_sum_base(hits, target):
  if target <= 0:
    return None
  ret = []
  for v in hits.keys():
    r = target - v
    if r == 0:
      ret.append([v])
    elif r < 0:
      continue
    else:
      ret_sub = combination_sum_base(hits, r)
      if ret_sub is not None:
        for e in ret_sub:
          e.append(v)
          ret.append(e)
  return ret

def combination_sum(candidates, target):
  hits = {}
  for c in candidates:
    hits[c] = 1
  ret = combination_sum_base(hits, target)
  ret = [sorted(e) for e in ret]
  ret = [tuple(e) for e in ret]
  ret = list(set(ret))
  return ret

print combination_sum([2, 3, 6, 7], 7)
