# Given a string containing just characters ()[]{}
# Determine if the input is valid.
# ()[]{} is valid but (] is not.

def is_valid(s):
  stack = []
  for c in s:
    if len(stack) == 0:
      stack.append(c)
    else:
      if (c == ')') and (stack[-1] == '('):
        stack.pop()
      elif (c == ']') and (stack[-1] == '['):
        stack.pop()
      elif (c == '}') and (stack[-1] == '{'):
        stack.pop()
      else:
        stack.append(c)
  if len(stack) == 0:
    return True
  else:
    return False

print is_valid('()')
print is_valid('()[]{}')
print is_valid('([)]')
