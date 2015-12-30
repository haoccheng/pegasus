# merge two sorted linked list and return a new list.

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  def length(root):
    count = 0
    curr = root
    while (curr is not None):
      count += 1
      curr = curr.next
    return count
  length = staticmethod(length)

  def intersection(self, headA, headB):
    lengthA = ListNode.length(headA)
    lengthB = ListNode.length(headB)
    if (lengthA == 0) or (lengthB == 0):
      return None
    p1 = headA
    p2 = headB
    if (lengthA > lengthB):
      for i in range(lengthA - lengthB):
        p1 = p1.next
    if (lengthB > lengthA):
      for i in range(lengthB - lengthA):
        p2 = p2.next
    while (p1 is not None) and (p2 is not None):
      if p1 == p2:
        return p1
      else:
        p1 = p1.next
        p2 = p2.next
    return None
  intersection = staticmethod(intersection)
