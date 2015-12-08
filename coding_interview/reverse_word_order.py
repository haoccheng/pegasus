# Reverse the order of words in a sentence but keep words themselves unchanged.
# "I am a student." -> "student. a am I"

def reverse_word_order(sentence):
  curr = ''
  ret = ''
  for c in sentence:
    if c != ' ':
      curr += c
    else: # reach word boundary.
      if len(ret) > 0:
        ret = curr + ' ' + ret
      else:
        ret = curr
      curr = ''
  if len(curr) > 0:
    ret = curr + ' ' + ret
  return ret

print reverse_word_order('I am a student.')
