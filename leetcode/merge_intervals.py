# given a collection of intervals, merge all overlapping intervals.

class Interval:
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e
  def __str__(self):
    return '[%d:%d]' % (self.start, self.end)

def compare(i1, i2):
  if i1.start == i2.start:
    return 0
  elif i1.start < i2.start:
    return -1
  else:
    return +1

def merge(its):
  ret = []
  curr = None
  for it in its:
    if curr is None:
      curr = it
    else:
      if (curr.end >= it.start):
        curr.end = max(curr.end, it.end)
      else:
        ret.append(curr)
        curr = it
  if curr is not None:
    ret.append(curr)
  return ret

it1 = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
it2 = sorted(it1, cmp=lambda x,y: compare(x,y))
it3 = merge(it2)
print [str(e) for e in it3]
