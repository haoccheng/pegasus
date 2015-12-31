# delete all nodes that have duplicates.
# 1->2->3->3->4->4->5, return 1->2->5

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

  def remove_dup(root):
    if root is None:
      return root
    curr = root
    new_root = None
    new_curr = None
    prev_value = None
    while (curr is not None):
      if (prev_value is None):
        if curr.next is None:
          if new_root is None:
            new_root = curr
            new_curr = new_root
          else:
            new_curr.next = curr
            new_curr = new_curr.next
        else:
          if curr.val != curr.next.val:
            if new_root is None:
              new_root = curr
              new_curr = new_root
            else:
              new_curr.next = curr
              new_curr = new_curr.next
      else:
        if (curr.val != prev_value):
          if curr.next is None:
            if new_root is None:
              new_root = curr
              new_curr = new_root
            else:
              new_curr.next = curr
              new_curr = new_curr.next
          else:
            if curr.val != curr.next.val:
              if new_root is None:
                new_root = curr
                new_curr = new_root
              else:
                new_curr.next = curr
                new_curr = new_curr.next
      prev_value = curr.val
      curr = curr.next
    if new_curr is not None:
      new_curr.next = None
    return new_root
  remove_dup = staticmethod(remove_dup)

x = ListNode.create_list([1,2,3,4,5])
y = ListNode.remove_dup(x)
print y.pt()

x = ListNode.create_list([1,2,3,3,4,4,5])
y = ListNode.remove_dup(x)
print y.pt()
