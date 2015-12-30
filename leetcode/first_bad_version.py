# https://leetcode.com/problems/first-bad-version/

def first_bad_version(n):
  start = 1
  end = n
  bad = None
  while (start <= end):
    mid = int((start + end) / 2)
    if isBadVersion(mid) == True:
      bad = mid
      if (start == mid):
        break
      else:
        end = mid - 1
    else:
      start = mid + 1
  return bad
