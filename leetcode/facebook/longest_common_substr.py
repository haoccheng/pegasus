# longest common substring.

def loncom_substr(S, T):
  scores = []
  for i in range(len(S)+1):
    row = [0] * (len(T)+1)
    scores.append(row)
  for i in range(1, len(scores)):
    for j in range(1, len(scores[i])):
      if S[i-1] == T[j-1]:
        scores[i][j] = scores[i-1][j-1] + 1
  for row in scores:
    print row

loncom_substr('abac', 'cabdc')
