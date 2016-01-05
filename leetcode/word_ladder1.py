# word ladder

def ladder1(begin_word, end_word, word_list, used):
  diff = 0
  for i in range(len(begin_word)):
    if begin_word[i] != end_word[i]:
      diff += 1
    if diff > 1:
      break
  if diff == 1:
    return 1
  if (begin_word == end_word):
    return 0
  min_change = None
  for c in word_list:
    if c in used:
      continue
    diff = 0
    for i in range(len(begin_word)):
      if begin_word[i] != c[i]:
        diff += 1
        if diff > 1:
          break
    if diff == 1:
      used.append(c)
      r = ladder1(c, end_word, word_list, used)
      if r >= 0:
        if min_change is None:
          min_change = r+1
        else:
          if r+1 < min_change:
            min_change = r+1
      used.pop()
  return min_change if min_change is not None else -1

print ladder1('hit', 'cog', ["hot","dot","dog","lot","log"], [])

