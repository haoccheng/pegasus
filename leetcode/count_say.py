# count-and-say sequence is the sequence of integers as below:
# 1, 11, 21, 1211, 111221, ..
#
# 1 -> 'one 1' -> 11
# 11 -> 'two 1' -> 21
# 21 -> 'one 2 one 1' -> 1211
# Given n, generate the nth sequence.

def count_say_base(ns):
  stack = []
  ret = ''
  for c in ns:
    if len(stack) == 0:
      stack.append(c)
    else:
      if stack[-1] == c:
        stack.append(c)
      else:
        ret = ret + str(len(stack)) + stack[-1]
        stack = []
        stack.append(c)
  if len(stack) > 0:
    ret = ret + str(len(stack)) + stack[-1]
  return ret

def count_say(n):
  curr = '1'
  next = None
  for i in range(1, n):
    next = count_say_base(curr)
    curr = next
  return curr

for i in range(1, 5):
  print count_say(i)
  
