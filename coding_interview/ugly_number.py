# If a number only has factor 2/3/5, it is an ugly number.
# 6 and 10 are ugly. 14 is not.
# 1 is considered to be 1st ugly.
# What is the arbitrary kth ugly number.

import heapq

def uglyK(K):
  heap = []
  heap.append(1)
  gv = None
  for i in range(K):
    v = heap[0] # minimum.
    while (len(heap) >0) and (heap[0] == v):
      heapq.heappop(heap)
    for e in [2, 3, 5]:
      heapq.heappush(heap, v*e)
    gv = v
  return (gv, len(heap))

for i in range(2000):
  print uglyK(i)
