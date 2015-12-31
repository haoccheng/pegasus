# edit distance.
import sys

def edit_distance(word1, word2):
  if len(word1) == 0 or len(word2) == 0:
    return max(len(word1), len(word2))
  scores = []
  for i in range(len(word1)+1):
    row = [0] * (len(word2)+1)
    scores.append(row)
  for i in range(len(word1)+1):
    scores[i][0] = i
  for j in range(len(word2)+1):
    scores[0][j] = j
  for i in range(1, len(word1)+1):
    for j in range(1, len(word2)+1):
      s0 = sys.maxint
      if word1[i-1] == word2[j-1]:
        s0 = scores[i-1][j-1]
      else:
        s0 = scores[i-1][j-1] + 1
      s1 = scores[i-1][j] + 1
      s2 = scores[i][j-1] + 1
      scores[i][j] = min(min(s0, s1), s2)
  return scores[-1][len(scores[-1])-1]


print edit_distance('abc', 'abe')
