# largest rectangle in histogram.

def rectangle1(height):
  if len(height) == 0:
    return 0
  max_height = max(height)
  scores = []
  for i in range(len(height)):
    row = [-1] * (max_height+1)
    scores.append(row)

  for j in range(1, height[0]+1):
    scores[0][j] = j
  for i in range(len(height)):
    for j in range(1, height[i]+1):
      if scores[i-1][j] > 0:
        scores[i][j] = scores[i-1][j] + j
      else:
        scores[i][j] = j
  return max([max(e) for e in scores])

def rectangle2(height):
  if len(height) == 0:
    return 0
  order_height = sorted(list(set([e for e in height if e > 0])))
  if len(order_height) == 0:
    return 0
  scores = []
  for i in range(len(height)):
    row = [-1] * (len(order_height))
    scores.append(row)
  for i in range(len(height)):
    for j in range(len(order_height)):
      if i == 0:
        if height[i] >= order_height[j]:
          scores[i][j] = order_height[j]
        else:
          break
      else:
        if height[i] >= order_height[j]:
          if scores[i-1][j] > 0:
            scores[i][j] = scores[i-1][j] + order_height[j]
          else:
            scores[i][j] = order_height[j]
        else:
          break
  return max([max(e) for e in scores])

def rectangle3(height):
  if len(height) == 0:
    return 0
  stack = []
  max_area = 0
  for i in range(len(height)):
    if len(stack) == 0:
      stack.append((height[i], i))
    else:
      start = i
      while (len(stack) > 0):
        (th, ti) = stack[-1]
        if th == height[i]:
          start = -1
          break
        elif th < height[i]:
          break
        else:
          stack.pop()
          area = (i-ti)*th
          max_area = max(max_area, area)
          start = ti
      if start >= 0:
        stack.append((height[i], start))
  for (h,i) in stack:
    area = (len(height)-1-i+1)*h
    max_area = max(max_area, area)
  return max_area

print rectangle3([2,1,5,6,2,3])
print rectangle3([0,0,0,0,0,0,0,0,2147483647])

