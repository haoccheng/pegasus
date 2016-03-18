# mini parser: 
# string:"324" or "[123,456,[788,799,833],[[]],10,[]]"
# 324 or [123,456,[788,799,833],[[]],10,[]].

def mini_parser(input):
  stack = []
  prev = ''
  for i in range(len(input)):
    if input[i] == '[':
      stack.append('[')
    elif input[i] == ',':
      if len(prev) > 0:
        stack.append(int(prev))
      prev = ''
    elif input[i] == ']':
      if len(prev) > 0:
        stack.append(int(prev))
      prev = ''
      items = []
      while (True):
        p = stack.pop()
        if p == '[':
          items = items[::-1]
          stack.append(items)
          break
        else:
          items.append(p)
    else:
      prev += input[i]
  if len(prev) > 0:
    stack.append(int(prev))
  print stack[0]

mini_parser('324')
mini_parser('[123,456,[788,799,833],[[]],10,[]]')

