# Given a singly linked list L: L0 -> L1 -> .. Ln-1 -> Ln
# reorder it to: L0 -> Ln -> L1 -> Ln-1 -> L2

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
 
  def length(head):
    count = 0
    curr = head
    while (curr is not None):
      count += 1
      curr = curr.next
    return count
  length = staticmethod(length)

  def reverse(head):
    # change to iterative one.
    if head is None:
      return (head, head)
    elif head.next is None:
      return (head, head)
    curr = head
    next = curr.next
    curr.next = None
    (reverse_next_head, reverse_next_tail) = ListNode.reverse(next)
    reverse_next_tail.next = curr
    return (reverse_next_head, curr)
  reverse = staticmethod(reverse)

  def reorder(head):
    list_len = ListNode.length(head)
    if list_len <= 2:
      return head
    p1 = head
    advance = (list_len / 2 - 1) if list_len % 2 == 0 else list_len / 2
    t = head
    while (advance > 0):
      t = t.next
      advance -= 1
    p2 = t.next
    t.next = None
    p2 = ListNode.reverse(p2)
    p2 = p2[0]
    while (p2 is not None):
      t1 = p1.next
      t2 = p2.next
      p1.next = None
      p2.next = None
      p1.next = p2
      p2.next = t1
      p1 = t1
      p2 = t2
    return head
  reorder = staticmethod(reorder)

x = ListNode.create_list([1, 2, 3, 4])
print ListNode.reorder(x).pt()
x = ListNode.create_list([1, 2, 3, 4, 5])
print ListNode.reorder(x).pt()
