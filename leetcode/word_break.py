# given a string s and dictionary of words dict.
# determine if s can be segmented into space-separated sequence of one or more dictionary words.
# s = 'leetcode'
# dict = ['leet', 'code']
# -> return True.

def word_break1(s, word_dict):
  if len(s) == 0:
    return True
  if s in word_dict:
    return True
  for i in range(1, len(s)):
    s1 = s[:i]
    s2 = s[i:]
    if s1 in word_dict:
      c = word_break1(s2, word_dict)
      if c == True:
        return True
  return False

def word_break2(s, word_dict):
  if len(s) == 0:
    return True
  scores = []
  for i in range(len(s)):
    row = [0] * len(s)
    scores.append(row)
  for i in range(len(s)):
    if s[i] in word_dict:
      scores[i][i] = 1
  for j in range(1, len(s)):
    for i in range(j-1, -1, -1):
      if s[i:j+1] in word_dict:
        scores[i][j] = 1
      else:
        for k in range(i, j):
          if scores[i][k] == 1 and scores[k+1][j] == 1:
            scores[i][j] = 1
            break
  return (scores[0][-1] == True)

def word_break3(s, word_dict):
  if len(s) == 0:
    return True
  hit = [0] * len(s)
  start = 0
  while (start < len(s) and start >= 0):
    for i in range(start, len(s)):
      if hit[i] == 1:
        continue
      if s[start:i+1] in word_dict:
        hit[i] = 1
    if hit[-1] == 1:
      return True
    next_start = -1
    for i in range(start, len(s)):
      if hit[i] == 1:
        next_start = i+1
        break
    start = next_start
  return False

print word_break1('leetcode', set(list(['leet', 'code'])))
print word_break2('leetcode', set(list(['leet', 'code'])))
print word_break3('leetcode', set(list(['leet', 'code'])))


