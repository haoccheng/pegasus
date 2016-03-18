# odd even linked list.
# https://leetcode.com/problems/odd-even-linked-list/
# O(1) space, O(N) time.

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
  
  def palindrome_base(head, tail):
    if tail is None:
      return (True, None)
    elif tail.next is None:
      if head.val == tail.val:
        return (True, head.next)
      else:
        return (False, None)
    else:
      check = ListNode.palindrome_base(head, tail.next)
      if check[0] == False:
        return (False, None)
      else:
        if check[1].val == tail.val:
          return (True, check[1].next)
        else:
          return (False, None)
  palindrome_base = staticmethod(palindrome_base)

  def palindrome(head):
    if head is None:
      return True
    check = ListNode.palindrome_base(head, head)
    return check[0]
  palindrome = staticmethod(palindrome)

x = ListNode.create_list([1, 2, 3, 2, 1])
print ListNode.palindrome(x)
x = ListNode.create_list([1, 2, 3, 4, 5])
print ListNode.palindrome(x)
x = ListNode.create_list([1, 2, 3, 3, 2, 1])
print ListNode.palindrome(x)
