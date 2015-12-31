# Given a list, rotate the list to the right by k places (k: non-negative).


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

  def length(root):
    count = 0
    curr = root
    while (curr is not None):
      count += 1
      curr = curr.next
    return count
  length = staticmethod(length)

  def rotate(root, k):
    total = ListNode.length(root)
    if total == 0:
      return root
    k = k % total
    if k == 0:
      return root
    p0 = root
    p1 = root
    for i in range(k):
      p1 = p1.next
    while (p1 is not None):
      p0 = p0.next
      p1 = p1.next
    p2 = root
    while (p2.next != p0):
      p2 = p2.next
    p2.next = None
    p3 = p0
    while (p3.next is not None):
      p3 = p3.next
    p3.next = root
    return p0
  rotate = staticmethod(rotate)

x = ListNode.create_list([1,2,3,4,5])
print x.pt()
print ListNode.length(x)
y = ListNode.rotate(x, 2)
print y.pt()
