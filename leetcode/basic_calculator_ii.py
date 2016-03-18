# basic calculator.
# non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.
# "3+2*2" = 7

def calculate(s):
  sequences1 = []
  value = ''
  for c in s:
    if c in ['+', '-', '*', '/']:
      sequences1.append(int(value))
      sequences1.append(c)
      value = ''
    elif c == ' ':
      continue
    else:
      value += c
  sequences1.append(int(value))

  # compute */
  sequences2 = []
  for c in sequences1:
    if isinstance(c, int):
      if len(sequences2) == 0:
        sequences2.append(c)
      else:
        if sequences2[-1] == '*' or sequences2[-1] == '/':
          op = sequences2.pop()
          v1 = sequences2.pop()
          if op == '*':
            sequences2.append(v1 * c)
          else:
            sequences2.append(v1 / c)
        else:
          sequences2.append(c)
    else:
      sequences2.append(c)

  # compute +-
  sequences3 = []
  for c in sequences2:
    if isinstance(c, int):
      if len(sequences3) == 0:
        sequences3.append(c)
      else:
        op = sequences3.pop()
        v1 = sequences3.pop()
        if op == '+':
          sequences3.append(v1 + c)
        else:
          sequences3.append(v1 - c)
    else:
      sequences3.append(c)
  print s, sequences3

calculate('3 + 2 * 2')
calculate('3/2')
calculate('3+5 / 2')
