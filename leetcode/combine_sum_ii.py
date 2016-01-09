# combination sum II

def combination_sum_base(candidates, target, start, end):
  if start > end:
    return []
  elif start == end:
    if candidates[start] == target:
      return [[target]]
  result = []
  if candidates[start] == target:
    result.append([target])
  remain = target - candidates[start]
  ret1 = combination_sum_base(candidates, remain, start+1, end)
  ret2 = combination_sum_base(candidates, target, start+1, end)
  if len(ret1) > 0:
    result = result + [[candidates[start]] + e for e in ret1]
  result = result + ret2
  return result

def combination_sum(candidates, target):
  if len(candidates) == 0:
    return []
  candidates = sorted(candidates)
  ret = combination_sum_base(candidates, target, 0, len(candidates)-1)
  ret = set([tuple(e) for e in ret])
  ret = [list(e) for e in ret]
  return ret

print combination_sum([10,1,2,7,6,1,5], 8)
print combination_sum([3,1,2], 3)

