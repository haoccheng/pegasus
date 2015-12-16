# string to integer (atoi)

def atoi(input):
  input = input.strip()
  if len(input) == 0:
    return None
  sign = +1
  if (input[0] == '+'):
    sign = +1
    input = input[1:]
  elif (input[0].isdigit()):
    sign = +1
  elif (input[0] == '-'):
    sign = -1
    input = input[1:]
  else:
    return None
  if len(input) == 0:
    return None
  value = 0
  for i in range(len(input)):
    if input[i].isdigit():
      value = value * 10 + int(input[i])
    else:
      return None
  return value if sign == +1 else -value


