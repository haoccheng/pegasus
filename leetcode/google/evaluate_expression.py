# evaluate expression.
# (+ 7 81 2) -> 90
# if expressions do not match, throw exception.
# next: (* 7 (+ 1 2))

def evaluate(input):
  stack = []
  number = ''
  for c in input:
    if c in '() +-*/':
      if len(number) > 0:
        stack.append(int(number))
        number = ''
      if c == '(':
        stack.append(c)
      elif c in '+-*/':
        stack.append(c)
      elif c == ')':
        exp = []
        while len(stack) > 0:
          v = stack.pop()
          if v == '(':
            break
          else:
            exp.insert(0, v)
        v1 = exp[1]
        for i2 in range(2, len(exp)):
          v2 = exp[i2]
          if exp[0] == '+':
            v1 = v1 + v2
          elif exp[0] == '-':
            v1 = v1 - v2
          elif exp[0] == '*':
            v1 = v1 * v2
          else:
            v1 = v1 / v2
        stack.append(v1)
    else:
      number += c
  print stack

evaluate('(+ 7 81 2)')
evaluate('(* 7 (+ 1 2))')
