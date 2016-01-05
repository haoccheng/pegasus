# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def max_profit(prices):
  minp = [-1] * len(prices)
  maxp = [-1] * len(prices)
  minp[0] = prices[0]
  for i in range(1, len(prices)):
    minp[i] = min(minp[i-1], prices[i])
  maxp[-1] = prices[-1]
  for i in range(len(prices)-2, -1, -1):
    maxp[i] = max(maxp[i+1], prices[i])
  gain = None
  for i in range(len(prices)):
    if gain is None:
      gain = maxp[i] - minp[i]
    else:
      v = maxp[i] - minp[i]
      if v > gain:
        gain = v
  return gain

#print max_profit([5, 2, 3, 7, 4, 1])
print max_profit([2, 1, 4])
