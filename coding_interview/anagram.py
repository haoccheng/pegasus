# anagram.
# If two English words have the same characters and occurrence number of each character
# is also identical.
# The only difference of a pair of anagram is character order.

from collections import defaultdict

def signature(text):
  counts = defaultdict(int)
  for c in text:
    counts[c] += 1
  return counts

def anagram(text1, text2):
  s1 = signature(text1)
  s2 = signature(text2)
  if len(s1) != len(s2):
    return False
  for k,c1 in s1.items():
    if k not in s2:
      return False
    if c1 != s2[k]:
      return False
  return True

def test():
  print anagram('evil', 'live')
  print anagram('silent', 'listen')
  print anagram('google', 'oogle')

test()
