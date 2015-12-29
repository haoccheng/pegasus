# Given two strings s/t, determine if t is anagram of s.
# assume string only contain lowercase alphabets.

def is_anagram(s, t):
  hs = [0] * 26
  ht = [0] * 26
  for c in s:
    hs[ord(c) - ord('a')] += 1
  for c in t:
    ht[ord(c) - ord('a')] += 1
  for i in range(len(hs)):
    if hs[i] != ht[i]:
      return False
  return True

print is_anagram('anagram', 'nagaram')
print is_anagram('rat', 'car')
