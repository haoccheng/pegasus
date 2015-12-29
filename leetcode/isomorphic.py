# Two strings are isomorphic if characters in s can be replaced to get t.

def is_isomorphic(s, t):
  hit = {}
  reverse_hit = {}
  for i in range(len(s)):
    s1 = s[i]
    t1 = t[i]
    if s1 not in hit:
      hit[s1] = t1
      if t1 in reverse_hit: # duplicate..
        return False
      reverse_hit[t1] = s1
    else:
      if hit[s1] != t1:
        return False
  return True

print is_isomorphic('egg', 'add')
print is_isomorphic('foo', 'bar')
print is_isomorphic('paper', 'title')
print is_isomorphic('ab', 'aa')
