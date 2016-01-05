# Given n pairs of parentheses, generate all combinations of parentheses.
# n=3
# "((()))", "(()())", "(())()", "()(())", "()()()"

from collections import defaultdict

def generate(n):
  if n <= 0:
    return []
  cache = defaultdict(list)
  cache[1].append('()')
  for i in range(2, n+1):
    dup = {}
    for e in cache[i-1]:
      dup['(%s)' % e] = 1
    for x in range(1, i):
      y = i - x
      cx = cache[x]
      cy = cache[y]
      for ex in cx:
        for ey in cy:
          dup['%s%s' % (ex, ey)] = 1
    cache[i] = dup.keys()
  return cache[n]

print generate(2)
