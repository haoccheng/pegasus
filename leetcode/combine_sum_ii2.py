# combination sum II
# all numbers are positive.

def search(candidates, target, start, cache, cache2):
  if (target, start) in cache:
    return cache[(target, start)]
  result = []
  if target == 0:
    return result
  istart = start
  while (istart < len(candidates)):
    iend = istart
    while (iend < len(candidates)):
      if candidates[istart] == candidates[iend]:
        iend += 1
      else:
        break
    if (target, istart) in cache2:
      result = result + cache2[(target, istart)]
    else:
      if candidates[istart] == target:
        cache2[(target, istart)] = [[target]]
        result.append([target])
        break
      elif candidates[istart] > target:
        break
      iresult = []
      for i in range(0, iend-istart+1):
        remain = target - candidates[istart]*i
        if remain == 0:
          iresult.append([candidates[istart]] * i)
          break
        elif remain < 0:
          break
        else:
          if remain < candidates[istart]:
            break
          ret = search(candidates, remain, iend, cache, cache2)
          if len(ret) > 0:
            iresult = iresult + [[candidates[istart]] * i + e for e in ret]
      cache2[(target, istart)] = [list(e) for e in set([tuple((e)) for e in iresult])]
      result = result + iresult
    istart = iend
  if (target, start) not in cache:
    cache[(target, start)] = [list(e) for e in set([tuple((e)) for e in result])]
  return result

def combination_sum(candidates, target):
  if len(candidates) == 0:
    return []
  candidates = sorted(candidates)
  cache = {}
  cache2 = {}
  ret = search(candidates, target, 0, cache, cache2)
  #ret = set([tuple(sorted(e)) for e in ret])
  ret = set([tuple((e)) for e in ret])
  ret = [list(e) for e in ret]
  return ret

#print combination_sum([10,1,2,7,6,1,5], 8)
#print combination_sum([3,1,2], 3)
#print combination_sum([4,4,2,1,4,2,2,1,3], 6)
#print combination_sum([4,4,2,1,4,2,2,3], 6)
#print combination_sum([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12], 27)
#print combination_sum([29,19,14,33,11,5,9,23,23,33,12,9,25,25,12,21,14,11,20,30,17,19,5,6,6,5,5,11,12,25,31,28,31,33,27,7,33,31,17,13,21,24,17,12,6,16,20,16,22,5], 28)
x = combination_sum([19,33,28,13,25,29,11,24,11,8,18,7,6,10,31,26,28,5,5,15,24,9,14,18,13,29,21,30,21,19,22,6,17,16,6,29,32,12,18,30,7,31,24,30,28,20,22,22,20,14,24,31], 25)
print len(x)
print x
