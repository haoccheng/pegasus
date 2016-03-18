# Given a list of words, can two words be joined together to form a palindrome?
# There can be multiple pairs, just return true if found one.

class TrieNode:
  def __init__(self, end=0):
    self.end = end
    self.child = {}

  def add(self, word):
    start = word[0]
    if start not in self.child:
      self.child[start] = TrieNode()
    if len(word) == 1:
      self.child[start].end += 1
    else:
      self.child[start].add(word[1:])
#=====================================
def bruteforce(words):
  pairs = []
  for i in range(len(words)):
    for j in range(len(words)):
      if i == j:
        continue
      check = False
      wi = words[i]
      wj = words[j]
      w = wi + wj
      if w == w[::-1]:
        check = True
      if check == True:
        pairs.append((wi, wj))
  return pairs
#=====================================
def trie_pair(words):
  trie = TrieNode()
  for word in words:
    trie.add(word)
  for word in words:
    match = -1
    reverse_word = word[::-1]
    curr = trie
    for i in range(len(reverse_word)):
      if reverse_word[i] not in curr.child:
        break
      else:
        if curr.child[reverse_word[i]].end > 0:
          match = i
          remain = reverse_word[match+1:]
          start = 0
          end = len(remain) - 1
          check = True
          while (start < end):
            if remain[start] != remain[end]:
              check = False
              break
            start += 1
            end -= 1
          if check == True:
            if match == len(reverse_word)-1:
              if word == reverse_word:
                if curr.child[reverse_word[i]].end > 1:
                  print reverse_word[:match+1], word
              else:
                print reverse_word[:match+1], word
            else:
              print reverse_word[:match+1], word
        curr = curr.child[reverse_word[i]]
        if i == len(reverse_word)-1: # match till the end.
          leaves = extract_leaves(curr, '')
          for leave in leaves:
            start = 0
            end = len(leave)-1
            check = True
            while (start < end):
              if leave[start] != leave[end]:
                check = False
                break
              start += 1
              end -= 1
            if check == True:
              print reverse_word+leave, word

def extract_leaves(root, prefix):
  leaves = []
  for c,node in root.child.items():
    if node.end > 0:
      leaves.append(prefix + c)
    leaves += extract_leaves(node, prefix+c)
  return leaves

words = ['bataa', 'tab', 'bat', 'aatab', 'aaa', 'aaa', 'bb', 'bbb', 'cc']
print bruteforce(words)
trie_pair(words)

