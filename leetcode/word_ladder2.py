# word ladder

def ladder(start_word, end_word, word_list, used):
  if start_word == end_word:
    return 0
  choice = None
  for i in range(len(start_word)):
    for c in 'abcdefghijklmnopqrstuvwxyz':
      w = start_word[:i] + c + start_word[i+1:]
      if w == end_word:
        return 1
      if (w in word_list) and (w not in used):
          used.add(w)
          check = ladder(w, end_word, word_list, used)
          used.remove(w)
          if check is not None:
            if choice is None:
              choice = check + 1
            elif choice < check + 1:
              choice = check + 1
  return choice if choice is not None else 0

used = set()
print ladder('hit', 'cog', ["hot","dot","dog","lot","log"], used)
#ladder('hit', None, None, None)
