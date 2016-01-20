# detect cycle.

def has_cycle(root):
  p1 = root
  p2 = root
  while (p1 is not None) and (p2 is not None):
    p1 = p1.next
    p2 = p2.next
    if p2 is None:
      return None
    p2 = p2.next
    if p1 == p2:
      return p1
  return None

def cycle_length(root):
  p1 = root
  length = 0
  p2 = root
  while (True):
    p2 = p2.next
    length += 1
    if p2 == p1:
      break
  return length

def cycle_root(root):
  meet = has_cycle(root)
  if meet is None:
    return None
  clen = cycle_length(meet)
  p1 = root
  p2 = root
  for i in range(clen):
    p2 = p2.next
  while (p1 != p2):
    p1 = p1.next
    p2 = p2.next
  return p1
