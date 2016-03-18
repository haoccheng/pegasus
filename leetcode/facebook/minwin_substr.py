# https://leetcode.com/problems/minimum-window-substring/
# ADOBECODEBANC
# ABC
#

from collections import defaultdict

def minwin(S, T):
  Tcache = defaultdict(int)
  for c in T:
    Tcache[c] += 1
  miss = len(Tcache)
  candidate = None

  start = 0
  end = 0
  while end < len(S):
    c = S[end]
    if c in Tcache:
      Tcache[c] -= 1
      if Tcache[c] == 0:
        miss -= 1
      if miss == 0:
        while (start <= end):
          c = S[start]
          if c in Tcache:
            print start, end, S[start:end+1]
            Tcache[c] += 1
            if Tcache[c] == 1:
              miss += 1
              start += 1
              while (start <= end):
                if S[start] in Tcache:
                  break
                start += 1
              break
          start += 1
    end += 1
     
minwin('ADOBECODEBANC', 'ABC')
minwin('ABCDOOABCDOABCDA', 'AABCD')
