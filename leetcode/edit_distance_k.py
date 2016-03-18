# Given a list of words and target word, return all words within K edit distance.

def bruteforce(words, target, K):
  hit = []
  for word in words:
    scores = []
    for i in range(len(word)+1):
      row = [0] * (len(target) + 1)
      scores.append(row)
    for i in range(len(scores)):
      scores[i][0] = i
    for j in range(len(scores[0])):
      scores[0][j] = j
    for i in range(1, len(scores)):
      for j in range(1, len(scores[i])):
        d1 = scores[i-1][j-1] if word[i-1] == target[j-1] else scores[i-1][j-1]+1 # replace
        d2 = scores[i-1][j] + 1
        d3 = scores[i][j-1] + 1
        scores[i][j] = min(d1, d2, d3)
    match = scores[-1][-1]
    if match <= K:
      hit.append(word)
  hit = sorted(hit)
  return hit

class TrieNode:
  def __init__(self, end=False):
    self.end = end
    self.child = {}

  def add(self, word):
    start = word[0]
    if start not in self.child:
      self.child[start] = TrieNode()
    curr = self.child[start]
    if len(word) == 1:
      curr.end = True
    else:
      curr.add(word[1:])

def trie_match(words, target, K):
  trie = TrieNode()
  for word in words:
    trie.add(word)
  scores = []
  scores.append([0] * (len(target) + 1))
  for j in range(len(scores[0])):
    scores[0][j] = j
  out = []
  for nc,ntrie in trie.child.items():
    out += trie_match_base(scores, nc, ntrie, target, K, '')
  return out

def trie_match_base(scores, c, trie, target, K, prefix):
  scores.append([0] * (len(target) + 1))
  scores[-1][0] = len(scores)
  out = []
  for j in range(1, len(scores[-1])):
    d1 = scores[-2][j-1] if c == target[j-1] else scores[-2][j-1]+1
    d2 = scores[-2][j] + 1
    d3 = scores[-1][j-1] + 1
    scores[-1][j] = min(d1, d2, d3)
  if trie.end == True:
    if scores[-1][-1] <= K:
      out.append(prefix + c)
  if min(scores[-1]) <= K:
    for nc,ntrie in trie.child.items():
      out += trie_match_base(scores, nc, ntrie, target, K, prefix+c)
  scores.pop()
  return out

words = ['abc', 'abd', 'abcd', 'adc', 'ad', 'bc', 'abcdef', 'bcdefg']
target = 'ac'
K = 1
print bruteforce(words, target, K)
print trie_match(words, target, K)

