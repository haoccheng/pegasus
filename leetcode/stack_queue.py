# implement stack using queue

class Stack:
  def __init__(self):
    self.back = []
    self.front = []
  
  def push(self, x):
    self.back.append(x)

  def reverse_base(self):
    if len(self.back) > 0:
      first = self.back.pop(0)
      self.reverse_base()
      self.back.append(first)
    
  def reverse(self):
    if len(self.back) > 0:
      self.reverse_base()
      while (len(self.front) > 0):
        first = self.front.pop(0)
        self.back.append(first)
      tmp = self.front
      self.front = self.back
      self.back = tmp

  def pop(self):
    self.reverse()
    return self.front.pop(0)

  def top(self):
    self.reverse()
    return self.front[0]

  def empty(self):
    return True if len(self.front) + len(self.back) == 0 else False

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print s.pop()
s.push(4)
print s.pop()
print s.pop()
