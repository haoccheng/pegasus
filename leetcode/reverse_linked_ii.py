# reverse linked list II
# 1->2->3->4->5->NULL, m = 2 and n = 4, 1->4->3->2->5->NULL
# reverse linked list from position m to n.
# 1 <= m <= n <= length of list.
# In place, one pass.

class Node:
  def __init__(self, x):
    self.val = x
    self.next = None

  def create(values):
    root = None
    curr = None
    for v in values:
      n = Node(v)
      if root is None:
        root = n
        curr = root
      else:
        curr.next = n
        curr = curr.next
    return root
  create = staticmethod(create)
  
  def pt(self):
    ret = []
    ret.append(self.val)
    if self.next is not None:
      ret += self.next.pt()
    return ret

  def reverse(root, m, n):
    p1 = root
    for i in range(1, m-1):
      p1 = p1.next
    p2 = p1.next if m != 1 else p1
    p5 = p2
    p3 = p2.next
    p2.next = None
    for i in range(m, n):
      p4 = p3.next
      p3.next = p2
      p2 = p3
      p3 = p4
    if m != 1:
      p1.next = p2
    p5.next = p3
    return root if m != 1 else p2
  reverse = staticmethod(reverse)

x = Node.create([1,2,3,4,5])
print x.pt()
y = Node.reverse(x, 2, 5)
print y.pt()
x = Node.create([1,2,3,4,5])
y = Node.reverse(x, 1, 5)
print y.pt()
