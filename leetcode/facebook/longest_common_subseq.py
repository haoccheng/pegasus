# longest common subsequence in 2 strings.

def loncom_subseq(S, T):
  scores = []
  for i in range(len(S)+1):
    row = [None] * (len(T)+1)
    scores.append(row)
  for j in range(len(scores[0])):
    scores[0][j] = (0, [])
  for i in range(len(scores)):
    scores[i][0] = (0, [])
  for i in range(1, len(scores)):
    for j in range(1, len(scores[i])):
      c1 = scores[i-1][j]
      c2 = scores[i][j-1]
      c3 = scores[i-1][j-1]
      if S[i-1] == T[j-1]:
        c3 = (scores[i-1][j-1][0]+1, scores[i-1][j-1][1]+[S[i-1]])
      if c1[0] > c2[0] and c1[0] > c3[0]:
        scores[i][j] = c1
      elif c2[0] > c1[0] and c2[0] > c3[0]:
        scores[i][j] = c2
      else:
        scores[i][j] = c3
  for row in scores:
    print row

#loncom_subseq('abc', 'abdc')
loncom_subseq('cbba', 'aabcb')
