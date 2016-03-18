# regular expression matching
# 3 characters:
# . (any one letter)
# * (zero or more of previous letter).
# + (one or more of previous letter).

def parse_expression(expression):
  prev = None
  parsed = []
  for curr in expression:
    if (curr == '*'):
      parsed.append((prev, curr))
      prev = None
    elif (curr == '+'):
      parsed.append((prev, 'c'))
      parsed.append((prev, '*'))
      prev = None
    else:
      if prev is not None:
        parsed.append((prev, 'c'))
      prev = curr
  if prev is not None:
    parsed.append((prev, 'c'))
  return parsed

def match_expression(input, expression):
  if len(input) == 0 and len(expression) == 0:
    return True
  elif len(input) == 0 and len(expression) > 0:
    return True if len([e for e in expression if (e[1] == '+') or (e[1] == 'c')]) == 0 else False
  elif len(input) > 0 and len(expression) == 0:
    return False
  else:
    if expression[0][1] == 'c':
      if input[0] == expression[0][0]:
        return match_expression(input[1:], expression[1:])
      elif expression[0][0] == '.':
        return match_expression(input[1:], expression[1:])
      else:
        return False
    elif expression[0][1] == '*':
      if input[0] == expression[0][0] or expression[0][0] == '.':
        c1 = match_expression(input[1:], expression[1:])
        c2 = match_expression(input[1:], expression)
        if c1 or c2:
          return True
      else:
        return match_expression(input, expression[1:])

print match_expression('aa', parse_expression('a'))
print match_expression('aa', parse_expression('aa'))
print match_expression('aaa', parse_expression('aa'))
print match_expression('aa', parse_expression('a*'))
print match_expression('aa', parse_expression('.*'))
print match_expression('ab', parse_expression('.*'))
print match_expression('aab', parse_expression('c*a*b'))
