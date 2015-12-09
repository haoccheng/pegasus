# Most profit from stock.
# Stock prices are sorted in an array in order of date.
# Get the most profit from the sequence of stock prices.
# {9,11,5,7,16,1,4,2} -> would be buy at 5, sell at 16, gain 11.

# Solution would be O(n)
# Imagine cut between position i and position i+1.
# Then, buy at the minimal from 0~i, sell at maximum from i+1~end.
# Basically, maintain two counters..

def stock_profit(stock):
  min_count = []
  max_count = []
  
  min_count.append(stock[0])
  for i in range(1, len(stock)-1):
    m = min(min_count[-1], stock[i])
    min_count.append(m)
  max_count.append(stock[-1])
  for i in range(len(stock)-2, 0, -1):
    m = max(max_count[0], stock[i])
    max_count.insert(0, m)
  assert(len(min_count) == len(max_count))
  profit = 0
  for i in range(len(min_count)):
    v = max_count[i] - min_count[i]
    if v > profit:
      profit = v
  return profit

print stock_profit([9, 11, 5, 7, 16, 1, 4, 2])
