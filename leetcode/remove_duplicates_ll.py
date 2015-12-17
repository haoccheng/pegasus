# Given a sorted linked list, delete all duplicates such that each element appeared only once.
# 1->1->2, return 1->2.
# 1->1->2->3->3, return 1->2->3.

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

def dedup(head):
  if head is None:
    return None
  curr = head
  curr_val = curr.val
  next = curr.next
  while (next is not None):
    if next.val == curr_val:
      curr.next = next.next
      next = curr.next
    else:
      curr = curr.next
      curr_val = curr.val
      next = next.next
  return head

h = ListNode.create([1,2,3,4,5])
x = dedup(h)
print x.pt()

h = ListNode.create([1, 1, 2])
x = dedup(h)
print x.pt()

h = ListNode.create([1, 1, 2, 3, 3])
x = dedup(h)
print x.pt()
