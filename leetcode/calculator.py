# basic calculator to evaluate a simple expression string.
# ()+- and non-negative integers and empty space.
# Can assume the given expression is always valid.
# 1 + 1 -> 2
# 2-1 + 2 -> 3
# (1+(4+5+2)-3)+(6+8) -> 23

# key = 1: number.
# key = 2: +
# key = 3: -
# key = 4: (
# key = 5: )
def process_stack(stack, c):
  if c == ' ':
    1 # no-op
  elif c in '0123456789':
    if len(stack) > 0:
      (key, value) = stack[-1]
      if key == 1:
        stack.pop()
        stack.append((key, value+c))
      else:
        stack.append((1, c))
    else:
      stack.append((1, c))
  elif c == '(':
    stack.append((4, None))
  elif (c == '+') or (c == '-'):
    op = 2 if c == '+' else 3
    if len(stack) >= 3:
      c3 = stack[-1]
      c2 = stack[-2]
      c1 = stack[-3]
      if (c1[0] == 1) and (c2[0] == 2 or c2[0] == 3) and (c3[0] == 1):
        stack.pop()
        stack.pop()
        stack.pop()
        v = int(c1[1]) + int(c3[1]) if c2[0] == 2 else int(c1[1]) - int(c3[1])
        stack.append((1, str(v)))
      stack.append((op, None))
    else:
      stack.append((op, None))
  elif c == ')':
    if len(stack) == 0:
      raise RuntimeError(')..')
    elif len(stack) == 2:
      c2 = stack[-1]
      c1 = stack[-2]
      if (c1[0] == 4) and (c2[0] == 1):
        stack.pop()
        stack.pop()
        stack.append(c2)
      else:
        raise RuntimeError(')..')
    elif len(stack) >= 4:
      c4 = stack[-1]
      c3 = stack[-2]
      c2 = stack[-3]
      c1 = stack[-4]
      if (c4[0] == 1) and (c2[0] == 1) and (c3[0] == 2 or c3[0] == 3) and (c1[0] == 4):
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        v = int(c2[1]) + int(c4[1]) if c3[0] == 2 else int(c2[1]) - int(c4[1])
        stack.append((1, str(v)))
      elif (c3[0] == 4) and (c4[0] == 1):
        stack.pop()
        stack.pop()
        stack.append(c4)
    else:
      raise RuntimeError('..')
  print c, stack

def calculate(s):
  stack = []
  for c in s:
    process_stack(stack, c)
  process_stack(stack, '+')
  v = int(stack[0][1])
  return v

#print calculate('1+1')
#print calculate('10-1')
#print calculate('2-1 + 2')
#print calculate('(1+(4+5+2)-3)+(6+8)')
print calculate('(5-(1+(5)))')
