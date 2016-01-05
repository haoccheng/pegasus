# fewest number of coins that make up the amount.

def coin_change(coins, amount):
  coins = sorted(coins)
  solution = [-1] * (amount+1)
  solution[0] = 0
  for i in range(1, amount+1):
    choice = -1
    for c in coins:
      remain = i - c
      if remain == 0:
        choice = 1
        break
      elif remain > 0:
        if solution[remain] >= 0:
          if choice < 0:
            choice = solution[remain] + 1
          else:
            if choice > solution[remain] + 1:
              choice = solution[remain] + 1
    solution[i] = choice
  print solution

coin_change([1,2,5], 11)
  
