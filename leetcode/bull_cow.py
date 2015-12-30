# https://leetcode.com/problems/bulls-and-cows/

from collections import defaultdict

def hint(secret, guess):
  exact_match = 0
  hit1 = defaultdict(int)
  hit2 = defaultdict(int)
  for i in range(len(secret)):
    if secret[i] == guess[i]:
      exact_match += 1
    else:
      hit1[secret[i]] += 1
      hit2[guess[i]] += 1
  char_match = 0
  for k,c1 in hit1.items():
    if k in hit2:
      c2 = hit2[k]
      char_match += min(c1, c2)
  return '%dA%dB' % (exact_match, char_match)

print hint('1807', '7810')
print hint('1123', '0111')
