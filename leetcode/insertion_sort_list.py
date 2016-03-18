# insertion sort in linked list.

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
  
  def insertion_sort(head):
    p1 = head
    p2 = None
    while (p1 is not None):
      curr = p1
      p1 = p1.next
      curr.next = None
      if p2 is None:
        p2 = curr
      elif curr.val <= p2.val:
        curr.next = p2
        p2 = curr
      else:
        p3 = p2
        while (p3.next is not None):
          if p3.next.val < curr.val:
            p3 = p3.next
          else:
            curr.next = p3.next
            p3.next = curr
            curr = None
            break
        if curr is not None:
          p3.next = curr
    return p2
  insertion_sort = staticmethod(insertion_sort)

x = ListNode.create_list([1, 2, 3, 2, 1])
y = ListNode.insertion_sort(x)
print y.pt()
x = ListNode.create_list([5, 4, 3, 2, 1])
y = ListNode.insertion_sort(x)
print y.pt()
x = ListNode.create_list([1, 2, 3, 4, 5])
y = ListNode.insertion_sort(x)
print y.pt()
