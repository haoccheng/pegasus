# Given a linked list and value x, partition such that all nodes less than x come before nodes greater than or equal to x.
# 1,4,3,2,5,2   x=3
# -> 1,2,2,4,3,5

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  def pt(self):
    ret = []
    ret.append(self.val)
    if self.next is not None:
      ret += self.next.pt()
    return ret

  def create(input):
    head = ListNode(input[0])
    if len(input) > 1:
      tail = ListNode.create(input[1:])
      head.next = tail
    return head
  create = staticmethod(create)

def partition_list(head, x):
  h1 = None
  p1 = None
  h2 = None
  p2 = None
  curr = head
  while (curr is not None):
    if curr.val < x:
      if h1 is None:
        h1 = curr
        p1 = curr
      else:
        p1.next = curr
        p1 = p1.next
    else:
      if h2 is None:
        h2 = curr
        p2 = curr
      else:
        p2.next = curr
        p2 = p2.next
    curr = curr.next
  if p1 is not None:
    p1.next = None
  if p2 is not None:
    p2.next = None
  if p1 is None:
    return h2
  else:
    p1.next = h2
    return h1

h = ListNode.create([1, 4, 3, 2, 5, 2])
x = partition_list(h, 3)
print x.pt()
