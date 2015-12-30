# pattern = "abba", str = "dog cat cat dog" should return true
# pattern = "abba", str = "dog cat cat fish" should return false.

def word_pattern(pattern, input):
  hit1 = {}
  hit2 = {}
  items = input.split(' ')
  if len(pattern) != len(items):
    return False
  for i in range(len(pattern)):
    p = pattern[i]
    s = items[i]
    if p in hit1:
      if s != hit1[p]:
        return False
    if s in hit2:
      if p != hit2[s]:
        return False
    hit1[p] = s
    hit2[s] = p
  return True

print word_pattern('abba', 'dog cat cat dog')
print word_pattern('abba', 'dog cat cat fish')
