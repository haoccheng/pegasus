# Given a string S, find the longest palindromic substring in S.
# Assume the maximum length of S is 1000, there exists one unique longest palindromic substring.

class Palindrome:
  def __init__(self):
    'hello world'

  def palindrome(self, s, index):
    # option 1. aSa
    li = index - 1
    ri = index + 1
    opt1 = s[index]
    while (li >= 0) and (ri <= len(s)-1):
      if s[li] == s[ri]:
        opt1 = s[li] + opt1 + s[ri]
        li -= 1
        ri += 1
      else:
        break
    # option 2. aSSa
    opt2 = s[index]
    if index + 1 <= len(s) - 1:
      if s[index] == s[index+1]:
        opt2 = s[index] + s[index+1]
        li = index - 1
        ri = index + 2
        while (li >= 0) and (ri <= len(s) - 1):
          if s[li] == s[ri]:
            opt2 = s[li] + opt2 + s[ri]
            li -= 1
            ri += 1
          else:
            break
    return opt1 if len(opt1) >= len(opt2) else opt2

  def longest_palindrome(self, s):
    candidates = [self.palindrome(s, i) for i in range(len(s))]
    candidates = [(e, len(e)) for e in candidates]
    candidates = sorted(candidates, key=lambda e:e[1], reverse=True)
    return candidates[0][0]

p = Palindrome()
print p.longest_palindrome('bananas')
print p.longest_palindrome('bananbs')
print p.longest_palindrome('a')
print p.longest_palindrome('aba')
print p.longest_palindrome('babac')
