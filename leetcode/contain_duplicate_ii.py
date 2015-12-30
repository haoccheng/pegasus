# Given an array of integer and integer k, find whether there are two distinct indices
# i/j such that nums[i] == nums[j] and the difference between i and j is at most k.

from collections import defaultdict

def nearby_duplicate(nums, k):
  hits = defaultdict(list)
  for i in range(len(nums)):
    hits[nums[i]].append(i)
  for v,occurrence in hits.items():
    if len(occurrence) >= 2:
      for i in range(len(occurrence)-1):
        p1 = occurrence[i]
        p2 = occurrence[i+1]
        if p2 - p1 <= k:
          return True
  return False

print nearby_duplicate([1,2,3,4], 11)
print nearby_duplicate([1,2,3,1], 4)
print nearby_duplicate([1,2,3,1], 2)

# i think a more efficient solution would be just to keep the last position
# would be sufficient.
