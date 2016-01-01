# delete node in a linked list.

def delete_node(root):
  curr = root
  if curr.next is not None:
    if curr.next.next is not None:
      p3 = curr
      p2 = curr.next
      p1 = curr.next.next
      while (p1 is not None):
        p3.val = p2.val
        p3 = p2
        p2 = p1
        p1 = p1.next
      p3.val = p2.val
      p3.next = None
    else:
      curr.val = curr.next.val
      curr.next = None
