# implement queue using stack.

class Stack:
  def __init__(self):
    self.queue = []
  def push(self, x):
    self.queue.append(x)
  def pop(self):
    return self.queue.pop()
  def peek(self):
    return self.queue[-1]
  def size(self):
    return len(self.queue)
  def empty(self):
    return True if self.size() == 0 else False

class Queue:
  def __init__(self):
    self.front_stack = Stack()
    self.back_stack = Stack()
  def push(self, x):
    self.front_stack.push(x)
  def pop(self):
    if not self.back_stack.empty():
      return self.back_stack.pop()
    while (not self.front_stack.empty()):
      v = self.front_stack.pop()
      self.back_stack.push(v)
    if not self.back_stack.empty():
      return self.back_stack.pop()
  def peek(self):
    if not self.back_stack.empty():
      return self.back_stack.peek()
    while (not self.front_stack.empty()):
      v = self.front_stack.pop()
      self.back_stack.push(v)
    if not self.back_stack.empty():
      return self.back_stack.peek()

  def empty(self):
    return True if self.front_stack.empty() and self.back_stack.empty() else False

q = Queue()
q.push('a')
q.push('b')
print q.pop()
print q.pop()
