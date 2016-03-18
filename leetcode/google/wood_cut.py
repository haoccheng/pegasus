# wood cut.
# Given n pieces of wood with length L[i]
# cut into small pieces to guarantee you could have equal or more than k pieces with same length.
# What is the longest length you can cut from these n pieces of wood?
# L=[232, 124, 456], k=7, return 114

def woodcut(woods, k):
  if sum(woods) < k:
    return None
  start = 1
  end = max(woods)
  while (start <= end):
    if start == end:
      if sum([e/start for e in woods]) >= k:
        return start
    elif start + 1 == end:
      if sum([e/end for e in woods]) >= k:
        return end
      if sum([e/start for e in woods]) >= k:
        return start
    else:
      middle = (start + end) / 2
      cut = sum([e/middle for e in woods])
      if cut >= k:
        start = middle
      else:
        end = middle
  return None

print woodcut([232, 124, 456], 7)
print woodcut([10, 19, 28, 37], 10)
