# https://leetcode.com/problems/combination-sum-iii/

def combine_sum_base(k, n, minv):
  if (k == 1):
    if (n >= minv) and (n <= 9):
      return [[n]]
    else:
      return []
  else:
    ret = []
    for v in range(minv, 9):
      r = n - v
      if r <= 0:
        break
      else:
        r2 = combine_sum_base(k-1, r, v+1)
        if len(r2) > 0:
          ret += [[v] + e for e in r2]
    return ret

def combine_sum(k, n):
  return combine_sum_base(k, n, 1)

print combine_sum(3, 7)
print combine_sum(3, 9)
