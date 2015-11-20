# implement a function that gets the minimal number of coins with values v1, v2, .. vn,
# To make change for an amount of money with value t.
# There are infinite number of coins for each value vi.
# Consider set of coins with values 1,3,9,10.
# 15 cent -> 3 (two coins 3 and 1 coin 9).

# coin[x]: minimal number of coins to make up x.

def build_changes(value):
  return [None] * (value + 1)

def minimal_coin(value):
  coins = [1, 3, 9, 10]
  changes = build_changes(value)
  changes[0] = 0
  for i in range(1, value+1):
    v = i
    # test all the coins.
    candidates = []
    for c in coins:
      r = v - c
      if (r >= 0):
        candidates.append(changes[r] + 1)
    changes[i] = min(candidates)
    print changes
  return changes

print minimal_coin(15)

