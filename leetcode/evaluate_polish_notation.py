# evaluate the value of arhithmetic expression in reverse polish notation.
# ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
# ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

def evaluate_rpn(tokens):
  stack = []
  for c in tokens:
    if c in '+-*/':
      if len(stack) >= 2:
        v2 = int(stack.pop())
        v1 = int(stack.pop())
        v = 0
        if c == '+':
          v = v1 + v2
        elif c == '-':
          v = v1 - v2
        elif c == '*':
          v = v1 * v2
        else:
          v = (int)(v1 * 1.0 / v2)
        stack.append(str(v))
      else:
        return 0
    else:
      stack.append(c)
  return int(stack[-1]) if len(stack) > 0 else 0

#print evaluate_rpn(["2", "1", "+", "3", "*"])
#print evaluate_rpn(["4", "13", "5", "/", "+"])
print evaluate_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
