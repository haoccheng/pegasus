# check whether a string stands for a number of not, include positive/negative integer/float.
# +100., 4e2 -.123 3.1416, -1E-16
# 12e, 1a3.14, 1.2.3, +-5, 12e+5.4

# It is a bit like FSM: accept a token, move to next state.

def is_number(text):
  if len(text) == 0:
    return False
  index = 0
  if (text[index] in '+-'):
    index += 1
  # expect float
  s1 = 0
  while (index < len(text)):
    if text[index] in '0123456789':
      index += 1
      s1 += 1
    else:
      break
  if (index >= len(text)):
    if s1 > 0:
      return True
    else:
      return False
  if text[index] == '.':
    index += 1
    s2 = 0
    while (index < len(text)):
      if text[index] in '0123456789':
        index += 1
        s2 += 1
      else:
        break
    s1 = s1 + s2
  if (index >= len(text)):
    if s1 > 0:
      return True
    else:
      return False
  if text[index] in ['e', 'E']:
    index += 1
    if (index < len(text)):
      if (text[index] in '+-'):
        index += 1
    s3 = 0
    while (index < len(text)):
      if text[index] in '0123456789':
        index += 1
        s3 += 1
      else:
        break
    if s3 == 0:
      return False
    elif index < len(text):
      return False
    else:
      if s1 == 0:
        return False
      else:
        return True
  else:
    return False

for n in ['123', '+123', '-123', '+123.0', '-123.0', '+123.', '-.123', '123.', '.123', '123e1', '123.e1', '123.123e100', '+123.123e+123', '+123.123e-123', '.', '123a', '.13e12.']:
  print n, is_number(n)
