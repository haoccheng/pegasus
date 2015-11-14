# Implement a function to match regular expression '.' and '*' in patterns.
# . match a single character.
# * match zero or any number characters preceding it.
# Match means string fully matches the pattent where all character in string match the full pattern.
# 'aaa' match 'a.a' and 'ab*ac*a' but it does not match 'aa.a' nor 'ab*a'


def represent_pattern(blob):
  p = []
  for c in blob:
    if c == '.':
      p.append(('*', '.'))
    elif c == '*':
      p[-1] = (p[-1][0], '*')
    else:
      p.append((c, '1'))
  return p

def match(input, pattern):
  if (len(input) == 0) and (len(pattern) == 0):
    return True
  elif (len(input) == 0) and (len(pattern) > 0):
    p = pattern[0]
    if p[1] != '*':
      return False
    else:
      return match(input, pattern[1:])
  elif (len(input) > 0) and (len(pattern) == 0):
    return False
  else:
    (pw, pc) = pattern[0]
    if (pc == '.'):
      return match(input[1:], pattern[1:])
    elif (pc == '1'):
      if (input[0] == pw):
        return match(input[1:], pattern[1:])
      else:
        return False
    elif (pc == '*'):
      if (input[0] == pw):
        choice1 = match(input[1:], pattern[1:]) # full match, move to next.
        choice2 = match(input[1:], pattern) # partial match, continue current pattern.
        choice3 = match(input, pattern[1:]) # skip current pattern.
        if (choice1 == True) or (choice2 == True) or (choice3 == True):
          return True
        else:
          return False
      else:
        return match(input, pattern[1:])

#print represent_pattern('a.a')
#print represent_pattern('ab*ac*a')
#print represent_pattern('aa.a')
#print represent_pattern('ab*a')
# 'aaa' match 'a.a' and 'ab*ac*a' but it does not match 'aa.a' nor 'ab*a'
print match('aaa', represent_pattern('a.a'))
print match('aaa', represent_pattern('ab*ac*a'))
print match('aaa', represent_pattern('aa.a'))
print match('aaa', represent_pattern('ab*a'))
print match('abc', represent_pattern('abc'))
print match('abc', represent_pattern('c*abcc*'))
print match('abc', represent_pattern('c.abcc*'))
print match('abc', represent_pattern('.bcc*'))
