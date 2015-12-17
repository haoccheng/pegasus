# Given a linked list, swap every two adjacent nodes and return the head.
# 1->2->3->4 return: 2->1->4->3.
# Use constant space. May not modify the values in the list; only nodes itself can be changed.

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

def swap_nodes(head):
  curr = head
  if curr is None:
    return None
  else:
    next = curr.next
    if next is None:
      return curr
    curr.next = next.next
    next.next = curr
    curr = next
    next = swap_nodes(curr.next.next)
    curr.next.next = next
  return curr

h = ListNode.create([1,2,3,4,5])
print h.pt()
x = swap_nodes(h)
print x.pt()
