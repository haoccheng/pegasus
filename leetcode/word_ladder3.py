# word ladder

def ladder(start_word, end_word, word_list):
  if start_word == end_word:
    return 1
  start = set([start_word])
  words = word_list
  step = 1
  while (True):
    candidates = [word[:i]+c+word[i+1:] for word in start for i in range(len(word)) for c in 'abcdefghijklmnopqrstuvwxyz']
    candidates = set(candidates)
    step += 1
    if end_word in candidates:
      return step
    candidates = candidates & words
    if len(candidates) == 0:
      return 0
    words = words - candidates
    start = candidates

print ladder('hit', 'cog', set(["hot","dot","dog","lot","log"]))
