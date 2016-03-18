# text justification.

def line_justification(words, maxlen):
  output = ''
  if len(words) == 1:
    output = words[0]
  else:
    nspace = maxlen - sum([len(w) for w in words])
    output = words[0]
    nbreak = len(words) - 1
    for i in range(1, len(words)):
      space = nspace / nbreak
      output += ' ' * space + words[i]
      nspace -= space
      nbreak -= 1
  return output

def justification(input, maxlen):
  # tokenization.
  words = input.split()
  words = [words.strip() for words in words if len(words) > 0]
  output = []
  # 
  curr_word = []
  curr_sum = 0 
  for word in words:
    if curr_sum + len(word) + len(curr_word) <= maxlen:
      curr_word.append(word)
      curr_sum += len(word)
    else:
      output.append(line_justification(curr_word, maxlen))
      curr_word = [word]
      curr_sum = len(word)
  if len(curr_word) > 0:
    output.append(line_justification(curr_word, maxlen))
  for row in output:
    print row

justification('Ruby is a dynamic, open source programming language with a focus on simplicity and productivity. It has an elegant syntax that is natural to read and easy to write.', 15)
