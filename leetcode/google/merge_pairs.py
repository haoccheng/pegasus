# list of pairs (a,b), (b,c), (c,d), (e,f), (f,g)
# return (a,b,c,d), (e,f,g)

class StrInt:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def prepend(self, c):
    prev_start = self.start
    self.start = c if c < self.start else self.start
    return prev_start

  def append(self, c):
    prev_end = self.end
    self.end = c if c > self.end else self.end
    return prev_end

def merge_pairs(input):
  cache = {}
  for (s, e) in input:
    ts = cache[s] if s in cache else None
    te = cache[e] if e in cache else None
    if ts is None and te is None:
      tu = StrInt(s, e)
      cache[s] = tu
      cache[e] = tu
    elif ts is not None and te is None:
      # [ts.start, ts.end] (s, e)
      ts1 = ts.start
      ts2 = ts.end
      tu = StrInt(min(ts1, s), max(ts2, e))
      del cache[ts1]
      del cache[ts2]
      cache[tu.start] = tu
      cache[tu.end] = tu
    elif ts is None and te is not None:
      # (s, e) [te.start, te.end]
      te1 = te.start
      te2 = te.end
      tu = StrInt(min(te1, s), max(te2, e))
      del cache[te1]
      del cache[te2]
      cache[tu.start] = tu
      cache[tu.end] = tu
    else:
      ts1 = ts.start
      ts2 = ts.end
      te1 = te.start
      te2 = te.end
      tu = StrInt(min(ts1, ts2, s), max(te1, te2, e))
      del cache[ts1]
      del cache[ts2]
      del cache[te1]
      del cache[te2]
      cache[tu.start] = tu
      cache[tu.end] = tu
  for k,v in cache.items():
    print v.start, v.end

#merge_pairs([('a','b'), ('b','c'), ('c','d'), ('e','f'), ('f','g')])
merge_pairs([('a','b'), ('c','d'), ('e','f'), ('d','e')])
