# merge two sorted linked list and return a new list.

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  def create_list(values):
    root = None
    curr = None
    for v in values:
      n = ListNode(v)
      if root is None:
        root = n
        curr = root
      else:
        curr.next = n
        curr = curr.next
    return root
  create_list = staticmethod(create_list)

  def pt(self):
    ret = []
    ret.append(self.val)
    if self.next is not None:
      ret += self.next.pt()
    return ret

  def merge(l1, l2):
    root = None
    curr = None
    p1 = l1
    p2 = l2
    while (p1 is not None) and (p2 is not None):
      if p1.val < p2.val:
        if root is None:
          root = p1
          curr = root
        else:
          curr.next = p1
          curr = curr.next
        p1 = p1.next
      else:
        if root is None:
          root = p2
          curr = root
        else:
          curr.next = p2
          curr = curr.next
        p2 = p2.next
    if p1 is not None:
      if root is Nont:
        root = p1
      else:
        curr.next = p1
    if p2 is not None:
      if root is None:
        root = p2
      else:
        curr.next = p2
    return root
  merge = staticmethod(merge)

x = ListNode.create_list([1, 3, 5, 7])
y = ListNode.create_list([2, 4, 6, 8])
z = ListNode.merge(x, y)
print z.pt()

x = ListNode.create_list([1, 3, 5, 7])
y = ListNode.create_list([12, 14, 16, 18])
z = ListNode.merge(x, y)
print z.pt()
