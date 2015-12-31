# Given a string of (), find the length of longest valid (well-formed) parenthese substring.

class Stack:
  def __init__(self):
    self.stack = []
  def pop(self):
    return self.stack.pop()
  def push(self, v):
    self.stack.append(v)
  def empty(self):
    return True if len(self.stack) == 0 else False
  def peek(self):
    return self.stack[-1]

def longest_valid_parentheses(s):
  stack = Stack()
  for c in s:
    if stack.empty() == True:
      stack.push(c)
    elif c == '(':
      stack.push(c)
    elif c == ')':
      if stack.peek() == '(':
        stack.pop()
        if stack.empty() == True:
          stack.push(1)
        else:
          if isinstance(stack.peek(), int):
            v = stack.pop()
            stack.push(v+1)
          else:
            stack.push(1)
      elif stack.peek() == ')':
        stack.push(c)
      else: # must be number.
        v = stack.pop()
        if stack.empty() == True:
          stack.push(v)
          stack.push(c)
        else:
          if stack.peek() == '(':
            stack.pop()
            if stack.empty() == True:
              stack.push(v+1)
            elif isinstance(stack.peek(), int):
              v2 = stack.pop()
              stack.push(v+v2+1)
            else:
              stack.push(v+1)
          else:
            stack.push(v)
            stack.push(c)
  count = 0
  for c in stack.stack:
    if isinstance(c, int):
      if c > count:
        count = c
  return count*2

#print longest_valid_parentheses('(()')
#print longest_valid_parentheses(')()())')
#print longest_valid_parentheses('()(())')
print longest_valid_parentheses('((()))())')
