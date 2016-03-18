# sort linked list.

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

  def quick_sort(root):
    p1 = root
    p2 = p1.next
    p1.next = None
    # split
    psmall_root = None
    psmall = None
    plarge_root = None
    plarge = None
    while (p2 is not None):
      p3 = p2.next
      p2.next = None
      if p2.val <= p1.val:
        if psmall_root is None:
          psmall_root = p2
          psmall = psmall_root
        else:
          psmall.next = p2
          psmall = psmall.next
      else:
        if plarge_root is None:
          plarge_root = p2
          plarge = plarge_root
        else:
          plarge.next = p2
          plarge = plarge.next
      p2 = p3
    # 
    if psmall_root is not None:
      (psmall_root, psmall) = ListNode.quick_sort(psmall_root)
    if plarge_root is not None:
      (plarge_root, plarge) = ListNode.quick_sort(plarge_root)
    new_root = None
    curr = None
    if psmall_root is not None:
      new_root = psmall_root
      curr = psmall
    if new_root is None:
      new_root = p1
      curr = p1
    else:
      curr.next = p1
      curr = curr.next
    curr.next = plarge_root
    curr = curr.next if curr.next is not None else curr
    if plarge_root is not None:
      curr = plarge
    return (new_root, curr)
  quick_sort = staticmethod(quick_sort)

x = ListNode.create_list([3, 1, 2, 4, 5])
y = ListNode.quick_sort(x)
print y[0].pt()
x = ListNode.create_list([1, 2, 3, 4, 5])
y = ListNode.quick_sort(x)
print y[0].pt()
x = ListNode.create_list([5, 4, 3, 2, 1])
y = ListNode.quick_sort(x)
print y[0].pt()

