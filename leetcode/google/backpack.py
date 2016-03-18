# A backpack has volume.
# a set of items, each item (volume, value).
# Find the maximum value that the backpack can hold.

# items: (volume, value)
def max_value(items, max_volume):
  scores = []
  for i in range(len(items)):
    row = [0] * (max_volume + 1)
    scores.append(row)
  for j in range(1, max_volume+1):
    if j >= items[0][0]:
      scores[0][j] = items[0][1]
  for i in range(1, len(items)):
    for j in range(1, max_volume+1):
      c1 = scores[i-1][j]
      remain = j - items[i][0]
      c2 = 0
      if remain == 0:
        c2 = items[i][1]
      elif remain > 0:
        c2 = scores[i-1][remain] + items[i][1]
      scores[i][j] = max(c1, c2)
  return scores[-1][-1]

for v in range(1, 25):
  print v, max_value([(5, 1), (7, 5), (8, 4)], v)
