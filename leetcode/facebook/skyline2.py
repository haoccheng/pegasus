# https://leetcode.com/problems/the-skyline-problem/

import heapq

def skyline(input):
  points = [('start', start, height) for (start, end, height) in input]
  points += [('end', end, height) for (start, end, height) in input]
  points = sorted(points, key=lambda e: e[1])
  
  start = []
  end = []
  curr = None
  for (startend, timep, height) in points:
    if curr is not None:
      if curr < timep:
        while len(end) > 0:
          end_top = -end[0]
          start_top = -start[0]
          if start_top == end_top:
            heapq.heappop(start)
            heapq.heappop(end)
          else:
            break
        curr_height = -start[0] if len(start) > 0 else 0
        print curr, curr_height
    curr = timep

    if startend == 'start':
      heapq.heappush(start, -height)
    else:
      heapq.heappush(end, -height)
  print curr, 0

input = [[2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8]]
skyline(input)

