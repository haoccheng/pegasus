# https://leetcode.com/problems/summary-ranges/
# [0,1,2,4,5,7], return ["0->2","4->5","7"]

def summary_ranges(nums):
  curr_s = None
  curr_e = None
  ret = []
  for v in nums:
    if curr_s is None:
      curr_s = v
      curr_e = v
    else:
      if curr_e + 1 == v:
        curr_e = v
      else:
        if curr_s != curr_e:
          ret.append('%d->%d' % (curr_s, curr_e))
        else:
          ret.append(str(curr_s))
        curr_s = v
        curr_e = v
  if curr_s is not None:
    if curr_s != curr_e:
      ret.append('%d->%d' % (curr_s, curr_e))
    else:
      ret.append(str(curr_s))
  return ret

print summary_ranges([0,1,2,4,5,7])

