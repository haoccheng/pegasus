# Given an array of strings, group anagrams together
# [eat, tea, tan, ate, nat, bat]
# ate/eat/tea, nat/tan, bat.

from collections import defaultdict

def group_anagrams(strs):
  hits = defaultdict(list)
  for s in strs:
    key = ''.join(sorted(s))
    hits[key].append(s)
  ret = [sorted(e) for e in hits.values()]
  return ret

print group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
