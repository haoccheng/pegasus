def hindex(citations):
  if len(citations) == 0:
    return 0
  scores = [0] * (1+len(citations))
  for c in citations:
    i = min(c, len(scores)-1)
    scores[i] += 1
  count = 0
  for h in range(len(scores)-1, 0, -1):
    count += scores[h]
    if count >= h:
      return h
  return 0

print hindex([3, 0, 6, 1, 5])
