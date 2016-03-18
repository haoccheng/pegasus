# Given two independent queues which has sorted timestamp.
# getNext() can fetch timestamp in queue. Each timestamp can only be consumed once.
# Compare timestamp in the two queues, if difference is < 1, print the pair of timestamp.
# Q1 0.2, 1.4, 3.0
# Q2 1.0 1.1, 3.5
# Output: (0.2, 1.0), (1.4, 1.0), (0.2, 1.1), (1.4, 1.1), (3.0, 3.5)

def twoqueues(queue1, queue2):
  p1 = 0
  p2 = 0
  stack1 = []
  stack2 = []
  while p1 < len(queue1) and p2 < len(queue2):
    if queue1[p1] < queue2[p2]:
      while (len(stack2) > 0):
        if stack2[0] + 1 < queue1[p1]:
          stack2.pop(0)
        else:
          break
      for v in stack2:
        if v >= queue1[p1] - 1 and v <= queue1[p1] + 1:
          print queue1[p1], v
        else:
          break
      stack1.append(queue1[p1])
      p1 += 1
    else:
      while (len(stack1) > 0):
        if stack1[0] + 1 < queue2[p2]:
          stack2.pop(0)
        else:
          break
      for v in stack1:
        if v >= queue2[p2] - 1 and v <= queue2[p2] + 1:
          print v, queue2[p2]
        else:
          break
      stack2.append(queue2[p2])
      p2 += 1
  while p1 < len(queue1):
    while len(stack2) > 0:
      if stack2[0] + 1 < queue1[p1]:
        stack2.pop(0)
      else:
        break
    for v in stack2:
      if v >= queue1[p1] - 1 and v <= queue1[p1] + 1:
        print queue1[p1], v
      else:
        break
    stack1.append(queue1[p1])
    p1 += 1
  while p2 < len(queue2):
    while len(stack1) > 0:
      if stack1[0] + 1 < queue2[p2]:
        stack1.pop(0)
      else:
        break
    for v in stack1:
      if v >= queue2[p2] - 1 and v <= queue2[p2] + 1:
        print v, queue2[p2]
      else:
        break
    stack2.append(queue2[p2])
    p2 += 1

twoqueues([0.2, 1.4, 3.0], [1.0, 1.1, 3.5])

