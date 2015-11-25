# Design a stack that can get minimum number with function min.
# The time complexity of min/push/pop are all O(1).

class MinStack:
  def __init__(self):
    self.stack = []
    self.min_stack = []

  def push(self, value):
    if len(self.stack) == 0:
      self.stack.append(value)
      self.min_stack.append(value)
    else:
      curr_min = self.min_stack[-1]
      if curr_min > value:
        self.min_stack.append(value)
      else:
        self.min_stack.append(curr_min)
      self.stack.append(value)

  def min(self):
    return self.min_stack[-1]

  def pop(self):
    self.stack.pop()
    self.min_stack.pop()

  def pt(self):
    print self.stack
    print self.min_stack

if __name__ == '__main__':
  ms = MinStack()
  ms.push(3)
  ms.push(1)
  ms.push(4)
  ms.push(0)
  print ms.min()
  ms.pop()
  print ms.min()

