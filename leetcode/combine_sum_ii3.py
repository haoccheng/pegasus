# combination sum II
# all numbers are positive.

def combination_sum(candidates, target):
  candidates.sort()
  return search(candidates, 0 ,target)

def search(candidates, start, target):
  if target == 0:
    return [[]]
  res = []
  for i in xrange(start, len(candidates)):
    if i != start and candidates[i] == candidates[i-1]:
      continue
    if candidates[i] > target:
      break
    for r in search(candidates, i+1, target-candidates[i]):
      res.append([candidates[i]]+r)
  return res

#print combination_sum([10,1,2,7,6,1,5], 8)
#print combination_sum([3,1,2], 3)
#print combination_sum([4,4,2,1,4,2,2,1,3], 6)
#print combination_sum([4,4,2,1,4,2,2,3], 6)
#print combination_sum([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12], 27)
#print combination_sum([29,19,14,33,11,5,9,23,23,33,12,9,25,25,12,21,14,11,20,30,17,19,5,6,6,5,5,11,12,25,31,28,31,33,27,7,33,31,17,13,21,24,17,12,6,16,20,16,22,5], 28)
x = combination_sum([19,33,28,13,25,29,11,24,11,8,18,7,6,10,31,26,28,5,5,15,24,9,14,18,13,29,21,30,21,19,22,6,17,16,6,29,32,12,18,30,7,31,24,30,28,20,22,22,20,14,24,31], 25)
print len(x)
print x
