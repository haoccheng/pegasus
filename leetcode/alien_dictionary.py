# There is a new alien language which uses the latin alphabet.
# However, the order among letters are unknown to you. 
# You receive a list of words from the dictionary, where words are sorted 
# lexicographically by the rules of this new language. 
# Derive the order of letters in this language.

from collections import defaultdict

def alien_dictionary(words):
  relative_order = defaultdict(set)
  for i in range(len(words)):
    for j in range(i+1, len(words)):
      wi = words[i]
      wj = words[j]
      for k in range(min(len(wi), len(wj))):
        if wi[k] != wj[k]:
          relative_order[wj[k]].add(wi[k])
          break
  for word in words:
    for c in word:
      if c not in relative_order:
        relative_order[c]
  target_size = len(relative_order)
  final_order = []
  while (len(relative_order) > 0):
    step = []
    for k,v in relative_order.items():
      if len(v) == 0:
        step.append(k)
    if len(step) == 0:
      break
    final_order += step
    for k,v in relative_order.items():
      for c in step:
        if c in v:
          v.remove(c)
    for c in step:
      del relative_order[c]
  if len(relative_order) > 0:
    return []
  else:
    return final_order

print alien_dictionary(['wrt', 'wrf', 'er', 'ett', 'rftt'])
