# remove all elements in the linked list that have value val.

def remove(root, val):
  new_root = None
  new_curr = None
  curr = root
  while (curr is not None):
    if curr.val == val:
      curr = curr.next
    else:
      if new_root is None:
        new_root = curr
        new_curr = new_root
      else:
        new_curr.next = curr
        new_curr = new_curr.next
      curr = curr.next
  if new_curr is not None:
    new_curr.next = None
  return new_root
