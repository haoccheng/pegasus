# https://leetcode.com/problems/the-skyline-problem/

def compare(p1, p2):
  # (start/end, time, height)
  if p1[2] == p2[2]: # same time point.
    if p1[1] == 'start' and p2[1] == 'end':
      return -1
    elif p1[1] == 'end' and p2[1] == 'start':
      return +1
    else: # same start/end type.
      if p1[0] < p2[0]:
        return -1
      elif p2[0] > p1[0]:
        return +1
      else:
        return 0
  else:
    if p1[2] < p2[2]:
      return -1
    elif p1[2] > p2[2]:
      return +1

import heapq

def skyline(input):
  points = [(height, 'start', start) for (start, end, height) in input]
  points += [(height, 'end', end) for (start, end, height) in input]
  points = sorted(points, cmp=lambda x,y: compare(x,y))
  # python heap: heap elements could be tuples in which the 1st element is the priority and defines sort order.
  start = []
  end = []
  for (height, startend, timep) in points:
    if startend == 'start':
      heapq.heappush(start, -height)
    else:
      top = -start[0]
      if top == height:
        heapq.heappop(start)
        while len(end) > 0:
          end_top = -end[0]
          start_top = -start[0]
          if start_top == end_top:
            heapq.heappop(start)
            heapq.heappop(end)
          else:
            break
      else:
        heapq.heappush(end, -height)
    curr_height = -start[0] if len(start) > 0 else 0
    print timep, curr_height
  print points

input = [[2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8]]
skyline(input)

