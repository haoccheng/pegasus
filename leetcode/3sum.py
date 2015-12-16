# Give an array S of n integers, are there elements a/b/c such that a+b+c=0?
# Find all unique triplets.
# Elements in a triplet should be in non-descending order (a <= b <= c).
# The solution set should not contain duplicate triplets.
# {-1, 0, 1, 2, -1, -4} -> (-1, 0, 1), (-1, -1, 2)

from collections import defaultdict

def three_sum(nums):
  # build the lookup table first.
  hits = defaultdict(int)
  for v in nums:
    hits[v] += 1
  candidates = []
  for v1 in hits.keys():
    for v2 in hits.keys():
      v3 = 0 - v1 - v2
      if v3 in hits:
        if (v1 == v2) and (v2 == v3):
          if hits[v1] >= 3:
            candidates.append((v1, v2, v3))
        elif (v1 == v2) or (v1 == v3):
          if hits[v1] >= 2:
            candidates.append((v1, v2, v3))
        elif (v2 == v3):
          if hits[v2] >= 2:
            candidates.append((v1, v2, v3))
        else:
          candidates.append((v1, v2, v3))
  # sort, dedup.
  candidates = [tuple(sorted(e)) for e in candidates]
  candidates = list(set(candidates))
  return candidates

print three_sum([-1, 0, 1, 2, -1, -4])
print three_sum([-1, 0, 1, 2, -1, -4, 0, 0])

