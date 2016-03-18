# Given a vector of intervals, return the interval that has the most overlap.
# [0,1], [2,8], [3,5], [4,6], [9,10]
# return 3, [4,5]

# 0 +1 <= convert intervals to change events.
# 1 -1
# 2 +1
# 8 -1
# 3 +1
# 5 -1
# ..

def most_overlap1(intervals):
  start = [(e[0], +1) for e in intervals]
  end = [(e[1], -1) for e in intervals]
  total = start + end
  total = sorted(total, key=lambda e: e[0]) # sort: total order of change events.
  
  # (0, +1), (1, -1), (2, +1), (8, -1), (3, +1), (5, -1)
  start = total[0][0]
  value = total[0][1]
  candidate = None
  for i in range(1, len(total)):
    (tp, inc) = total[i]
    if inc < 0:
      if candidate is None:
        candidate = (value, start, tp)
      elif value > candidate[0]:
        candidate = (value, start, tp)
      start = tp
      value += inc
    else:
      start = tp
      value += inc
  print candidate

most_overlap1([[0,1], [2,8], [3,5], [4,6], [9,10]])

# [0,9], [1,2], [1,3], [1,4]
# instead maintain a stack.
def most_overlap2(intervals):
  intervals = sorted(intervals, key = lambda e: e[0]) # sort by start time.
  start = intervals[0][0]
  value = 1
  cache = [intervals[0][1]] # only end would run into cache
  candidate = None
  for i in range(1, len(intervals)):
    (itstart, itend) = intervals[i]
    while len(cache) > 0 and cache[0] <= itstart:
      et = cache.pop(0)
      if candidate is None:
        candidate = (value, start, et)
      elif value > candidate[0]:
        candidate = (value, start, et)
      start = et
      value -= 1
    start = itstart
    value += 1
    cache.append(itend)
    cache = sorted(cache) # to be optimized.
  while len(cache) > 0:
    et = cache.pop(0)
    if candidate is None:
      candidate = (value, start, et)
    elif value > candidate[0]:
      candidate = (value, start, et)
    start = et
    value -= 1
  print candidate

most_overlap2([[0,1], [2,8], [3,5], [4,6], [9,10]])
most_overlap2([[1, 10], [2, 10], [3, 10], [4, 10], [5, 10]])
