# meeting schedule
# start, end
# input: [[(100, 300), (800, 900)], [..]]
# list of list of intervals.
# return the list of intervals that are not covered by the above.

def merge_intervals(intervals):
  its = []
  for e in intervals:
    its += e
  its = sorted(its, key=lambda e: e[0])
  curr = None
  output = []
  for it in its:
    if curr is None:
      curr = it
    else:
      if curr[1] < it[0]:
        output.append(curr)
        curr = it
      else:
        curr = (min(curr[0], it[0]), max(curr[1], it[1]))
  if curr is not None:
    output.append(curr)
  return output

def inverse_intervals(start, end, intervals):
  output = []
  x = start
  for it in intervals:
    if x < it[0]:
      output.append((x, it[0]))
    x = it[1]
  if x < end:
    output.append((x, end))
  return output

def schedule(start, end, intervals):
  its1 = merge_intervals(intervals)
  its2 = inverse_intervals(start, end, its1)
  return its2

intervals = [[(100, 300), (800, 900)], [(200,400), (850,950)]]
print schedule(0, 1000, intervals)

intervals = [[(100, 300), (800, 900)], [(200,1000)]]
print schedule(0, 1000, intervals)

intervals = [[(100, 300), (800, 900)], [(0,1000)]]
print schedule(0, 1000, intervals)
