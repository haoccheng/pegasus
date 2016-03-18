# longest consecutive sequence.
# Given an unsorted array of integers, find the length of longest consecutive sequence.
# [100, 4, 200, 1, 3, 2] -> [1, 2, 3, 4]
# O(n)

def lcs(input):
  hit = {}
  candidate = None
  for value in input:
    if value not in hit:
      lhs = value - 1
      rhs = value + 1
      lit = hit[lhs] if lhs in hit else None
      rit = hit[rhs] if rhs in hit else None
      if lit is None and rit is None:
        hit[value] = (value, value)
      elif lit is not None and rit is None:
        (l1, l2) = lit
        if l2 + 1 == value:
          if l1 in hit:
            del hit[l1]
          if l2 in hit:
            del hit[l2]
          hit[l1] = (l1, value)
          hit[value] = (l1, value)
      elif lit is None and rit is not None:
        (r1, r2) = rit
        if value + 1 == r1:
          if r1 in hit:
            del hit[r1]
          if r2 in hit:
            del hit[r2]
          hit[value] = (value, r2)
          hit[r2] = (value, r2)
      else:
        (l1, l2) = lit
        (r1, r2) = rit
        if l1 in hit:
          del hit[l1]
        if l2 in hit:
          del hit[l2]
        if r1 in hit:
          del hit[r1]
        if r2 in hit:
          del hit[r2]
        if (l2 + 1 == value) and (value + 1 == r1):
          hit[l1] = (l1, r2)
          hit[r2] = (l1, r2)
        elif (l2 + 1 == value) and (value + 1 != r1):
          n1 = min(l1, r1)
          hit[n1] = (n1, r2)
          hit[r2] = (n1, r2)
        elif (l2 + 1 != value) and (value + 1 == r1):
          n2 = max(l2, r2)
          hit[l1] = (l1, n2)
          hit[n2] = (l1, n2)
        else:
          n1 = min(l1, r1)
          n2 = max(l2, r2)
          hit[n1] = (n1, n2)
          hit[n2] = (n1, n2)
  print hit

lcs([100, 4, 200, 1, 3, 2])
