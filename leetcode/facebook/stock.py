# stock buy/sell at most two transactions.

def stock(input):
  print input
  scores = []
  for i in range(3):
    row = [0] * len(input)
    scores.append(row)

  for i in range(1, 3):
    for j in range(1, len(input)):
      c1 = scores[i][j-1] # not trade at position j.
      c2 = input[j] - input[0]
      for k in range(1, j):
        c2 = max(c2, (input[j] - input[k]) + scores[i-1][k-1])
      scores[i][j] = max(c1, c2)
  for row in scores:
    print row

stock([5, 1, 10, 6, 7])
