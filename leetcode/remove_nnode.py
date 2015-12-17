# remove nth node from end of list
# Given a linked list, remove nth node from the end, and return the head.
# 1 -> 2 -> 3 -> 4 -> 5, n=2.
# return 1->2->3->5.

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

def remove_nnode(head, n):
  curr = head
  next = head
  for i in range(n):
    if next is None:
      return None
    next = next.next
  if next is None:
    head = head.next
  else:
    while (next.next is not None):
      curr = curr.next
      next = next.next
    curr.next = curr.next.next
  return head

h = ListNode.create([1,2,3,4,5])
print h.pt()
x = remove_nnode(h, 2)
print x.pt()

h = ListNode.create([1,2])
print h.pt()
x = remove_nnode(h, 1)
print x.pt()

h = ListNode.create([1,2])
print h.pt()
x = remove_nnode(h, 2)
print x.pt()

h = ListNode.create([1])
x = remove_nnode(h, 1)
print x
