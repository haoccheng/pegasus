# Given two linked list representing two non-negative numbers.
# The digits are stored in reverse order and each of their node contains a single digit.
# Add two numbers and return as linked list.
# (2 4 3) + (5 6 4) -> (7 0 8)

class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

  def pt(self):
    r = []
    r.append(self.val)
    if self.next is not None:
      r += self.next.pt()
    return r

class Solution:
  def create_value_node(self, value, carryover, root, rcur):
    if value >= 10:
      value = value - 10
      carryover = 1
    else:
      carryover = 0
    if root is None:
      root = ListNode(value)
      rcur = root
    else:
      rcur.next = ListNode(value)
      rcur = rcur.next
    return (value, carryover, root, rcur)

  def add_two_numbers(self, l1, l2):
    carryover = 0
    c1 = l1
    c2 = l2
    root = None
    rcur = None
    while (c1 is not None) and (c2 is not None):
      value = c1.val + c2.val + carryover
      (value, carryover, root, rcur) = self.create_value_node(value, carryover, root, rcur)
      c1 = c1.next
      c2 = c2.next
    while (c1 is not None):
      value = c1.val + carryover
      (value, carryover, root, rcur) = self.create_value_node(value, carryover, root, rcur)
      c1 = c1.next
    while (c2 is not None):
      value = c2.val + carryover
      (value, carryover, root, rcur) = self.create_value_node(value, carryover, root, rcur)
      c2 = c2.next
    if carryover == 1:
      rcur.next = ListNode(1)
    return root

def test():
  l1 = ListNode(2)
  l1.next = ListNode(4)
  l1.next.next = ListNode(3)
  l2 = ListNode(5)
  l2.next = ListNode(6)
  l2.next.next = ListNode(4)
  s = Solution()
  r = s.add_two_numbers(l1, l2)
  print r.pt()

test()
