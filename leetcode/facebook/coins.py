# infinite supply of coins
# the total number of distinct ways to make up a target amount.

def makeup(coins, target):
  coins = sorted(coins)
  combines = []
  for i in range(len(coins)):
    row = [0] * (target+1)
    combines.append(row)
  for value in range(1, len(combines[0])):
    remain = value - coins[0]
    if remain == 0:
      combines[0][value] = 1
    elif remain > 0:
      combines[0][value] = combines[0][remain]
    else:
      combines[0][value] = 0
  for i in range(1, len(coins)):
    for j in range(1, len(combines[i])):
      c1 = combines[i-1][j] # not use kth coin
      c2 = 0
      remain = j - coins[i]
      if remain == 0:
        c2 = 1
      elif remain > 0:
        c2 = combines[i][remain]
      combines[i][j] = c1 + c2
  for row in combines:
    print row

makeup([1,2,3], 4)
print '==========='
makeup([2,3], 4)
print '==========='
makeup([2,3,10], 20)
