# Given price of each dishes.
# A target amount to spend.
# Find all combination of ordering dishes to use up the money.

def dish_base(prices, target):
  if len(prices) == 0:
    return []
  out = []
  for i in range(target / prices[0] + 1):
    remain = target - prices[0] * i
    if remain == 0:
      out.append([(prices[0], i)])
    elif remain > 0:
      remain_out = dish_base(prices[1:], remain)
      if len(remain_out) > 0:
        for e in remain_out:
          if i > 0:
            out.append([(prices[0], i)] + e)
          else:
            out.append(e)
  return out

prices = [1, 5, 8, 10]
target = 20
print prices, target
for e in dish_base(prices, target):
  print e
