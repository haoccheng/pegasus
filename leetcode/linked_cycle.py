# detect cycle.

def has_cycle(root):
  p1 = root
  p2 = root
  while (p1 is not None) and (p2 is not None):
    p1 = p1.next
    p2 = p2.next
    if p2 is None:
      return False
    p2 = p2.next
    if p1 == p2:
      return True
  return False
