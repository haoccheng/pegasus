# Given two integer arrays, one is the sequence of numbers pushed into a stack.
# Suppose all numbers are unique.
# Check whether the other array is a corresponding sequence popped from the array.
# push sequence [1,2,3,4,5]
# pop sequence [4,5,3,2,1] accept.
# pop sequence [4,3,5,1,2] reject.

class Stack:
  def __init__(self):
    self.stack = []

  def push(self, value):
    self.stack.append(value)

  def size(self):
    return len(self.stack)

  def peek(self):
    assert(self.size() > 0)
    return self.stack[-1]

  def pop(self):
    self.stack.pop()

# simulate the sequence and check whether the stack is empty in the end and no conflict raise.
def check_push_pop(push, pop):
  stack = Stack()
  push_index = 0
  pop_index = 0
  while (push_index < len(push)) or (pop_index < len(pop)):
    if stack.size() == 0:
      stack.push(push[push_index])
      push_index += 1
    else:
      t = stack.peek()
      if t == pop[pop_index]:
        stack.pop()
        pop_index += 1
      elif (push_index < len(push)):
        stack.push(push[push_index])
        push_index += 1
      else:
        return False
  return True

def test():
  push_seq = [1, 2, 3, 4, 5]
  pop_seq = [4, 5, 3, 2, 1]
  print check_push_pop(push_seq, pop_seq)

  push_seq = [1, 2, 3, 4, 5]
  pop_seq = [4, 3, 5, 1, 2]
  print check_push_pop(push_seq, pop_seq)

test()
