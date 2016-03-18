# word search ii
# https://leetcode.com/problems/word-search-ii/

class TrieNode:
  def __init__(self, end=False):
    self.end = end
    self.child = {}

  def add(self, word):
    start = word[0]
    if start not in self.child:
      self.child[start] = TrieNode()
    if len(word) == 1:
      self.child[start].end = True
    else:
      self.child[start].add(word[1:])

def board_search(board, x, y, trie, prefix):
  c = board[x][y]
  out = []
  if c in trie.child:
    curr = trie.child[c]
    if curr.end:
      out.append(prefix + c)
    board[x][y] = '1'
    if (x > 0):
      if board[x-1][y] != '1':
        out += board_search(board, x-1, y, curr, prefix+c)
    if (x < len(board)-1):
      if board[x+1][y] != '1':
        out += board_search(board, x+1, y, curr, prefix+c)
    if (y > 0):
      if board[x][y-1] != '1':
        out += board_search(board, x, y-1, curr, prefix+c)
    if (y < len(board[0])-1):
      if board[x][y+1] != '1':
        out += board_search(board, x, y+1, curr, prefix+c)
  board[x][y] = c
  return out

def find_words(board, words):
  trie = TrieNode()
  for word in words:
    trie.add(word)
  out = []
  for i in range(len(board)):
    for j in range(len(board[i])):
      out += board_search(board, i, j, trie, '')
  out = set(out)
  return out

print find_words([list('oaan'), list('etae'), list('ihkr'), list('iflv')], ['oath', 'pea', 'eat', 'rain', 'eate'])
