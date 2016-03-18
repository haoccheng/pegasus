# odd even linked list.
# https://leetcode.com/problems/odd-even-linked-list/

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

  def odd_even(root):
    root_odd = None
    tail_odd = None
    root_even = None
    tail_even = None
    is_odd = True
    curr = root
    while (curr is not None):
      if is_odd == True:
        if root_odd is None:
          root_odd = curr
          tail_odd = curr
        else:
          tail_odd.next = curr
          tail_odd = tail_odd.next
        curr = curr.next
        tail_odd.next = None
        is_odd = False
      else:
        if root_even is None:
          root_even = curr
          tail_even = curr
        else:
          tail_even.next = curr
          tail_even = tail_even.next
        curr = curr.next
        tail_even.next = None
        is_odd = True
    if tail_odd is not None:
      tail_odd.next = root_even
    return root_odd
  odd_even = staticmethod(odd_even)

x = ListNode.create_list(range(10))
y = ListNode.odd_even(x)
print y.pt()
