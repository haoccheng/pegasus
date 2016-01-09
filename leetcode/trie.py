# Implement trie
# insert/search/startsWith
# assume all inputs are lowercase a-z.

class TrieNode:
  def __init__(self):
    self.end = False
    self.outbound = [None] * 26

class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    if len(word) == 0:
      return
    curr = self.root
    for c in word:
      index = ord(c) - ord('a')
      if curr.outbound[index] is None:
        curr.outbound[index] = TrieNode()
      curr = curr.outbound[index]
    curr.end = True

  def search(self, word):
    if len(word) == 0:
      return False
    curr = self.root
    for c in word:
      index = ord(c) - ord('a')
      if curr.outbound[index] is None:
        return False
      curr = curr.outbound[index]
    return True if curr.end == True else False

  def startsWith(self, prefix):
    curr = self.root
    for c in prefix:
      index = ord(c) - ord('a')
      if curr.outbound[index] is None:
        return False
      curr = curr.outbound[index]
    return True

t = Trie()
t.insert('hello')
print t.search('hello')
t.insert('helloa')
print t.search('helloa')
print t.search('hell')
print t.startsWith('hell')
