# Given a set of integers, any form to combine them +-*/ to arrive to a target.
# {1,2,3,7,60}, target=48 -> 2*60/3+1+7 = 48. -> return True

class Expression:
  def __init__(self, left, right, operator):
    self.left = left
    self.right = right
    self.operator = operator
    self.value = None
    self.compute()

  def compute(self):
    left = self.left if isinstance(self.left, int) else self.left.value
    right = self.right if isinstance(self.right, int) else self.right.value
    if self.operator == '+':
      self.value = left + right
    elif self.operator == '-':
      self.value = left - right
    elif self.operator == '*':
      self.value = left * right
    elif self.operator == '/':
      self.value = left / right

  def __str__(self):
    left = self.left if isinstance(self.left, int) else self.left.value
    right = self.right if isinstance(self.right, int) else self.right.value
    return '(%d %s %d)' % (left, self.operator, right)

def compute_math_base(left, right, target):
  if len(right) == 1:
    for op in '+-*/':
      if Expression(left, right[0], op).value == target:
        print left, op, right[0]
        return True
  else:
    for i in range(len(right)):
      v = right[i]
      remain = list(right)
      remain.pop(i)
      for op in '+-*/':
        e = Expression(left, v, op)
        check = compute_math_base(e, remain, target)
        if check == True:
          return True
  return False

def compute_math(input, target):
  for i in range(len(input)):
    left = input[i]
    remain = list(input)
    remain.pop(i)
    check = compute_math_base(left, remain, target)
    if check == True:
      return True
  return False

#print compute_math([1,2,3], 6)
#print compute_math([1,2,3], 7)
#print compute_math([1,2,3], 8)
#print compute_math([1,2,3], 9)
#print compute_math([1,2,3], 10)
for target in range(0, 100):
  print '================================'
  print target, compute_math([1,2,3,7,60], target)
