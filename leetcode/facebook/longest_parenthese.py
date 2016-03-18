# longest valid parentheses.

def process_stack(stack, c):
  if len(stack) == 0:
    return None
  if isinstance(c, int):
    top = stack[-1]
    if isinstance(top, int):
      stack.pop()
      return top+c
  elif c == ')':
    if len(stack) == 1:
      if stack[0] == '(':
        stack.pop()
        return 1
    else:
      t0 = stack[-1]
      t1 = stack[-2]
      if t0 == '(':
        stack.pop()
        return 1
      elif isinstance(t0, int):
        if t1 == '(':
          stack.pop()
          stack.pop()
          return t0+1
  return None

def parent(input):
  stack = []
  for c in input:
    if len(stack) == 0:
      stack.append(c)
    elif c == '(':
      stack.append(c)
    elif c == ')':
      while True:
        ret = process_stack(stack, c)
        if ret is None:
          stack.append(c)
          break
        else:
          c = ret
  start = 0
  ret = ''
  for c in stack:
    if isinstance(c, int):
      ret += input[start:start+c*2]
      start += c*2
    else:
      start += len(c)
  return ret

print parent('()')
print parent('(())')
print parent('((())')
print parent(')()())')
print parent('())())')

