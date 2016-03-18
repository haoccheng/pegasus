# Given two strings S/T, determine if they are both one edit distance apart.

def edit_replace(s, t):
  check = [s[i]!=t[i] for i in range(len(s))]
  if sum(check) == 1:
    return True
  else:
    return False

def edit_addition(s, t): # s is 1-letter shorter.
  p = 0
  while p < len(s):
    if s[p] == t[p]:
      p += 1
    else:
      break
  if p == len(s):
    return True
  return s[p:] == t[p+1:]

def edit1(s, t):
  if len(s) == len(t):
    return edit_replace(s, t)
  elif len(s)+1 == len(t):
    return edit_addition(s, t)
  elif len(t)+1 == len(s):
    return edit_addition(t, s)
  else:
    return False

print edit1('abc', 'abcd')
print edit1('ac', 'acd')
print edit1('ac', 'acdb')
print edit1('acd', 'ace')
