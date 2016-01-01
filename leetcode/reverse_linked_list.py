# reverse linked list
# iterative.

def reverse_list(root):
  if root is None:
    return None
  p1 = root
  p2 = p1.next
  p1.next = None
  while (p2 is not None):
    p3 = p2.next
    p2.next = p1
    p1 = p2
    p2 = p3
  return p1
