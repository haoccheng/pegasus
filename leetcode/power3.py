# determine if an integer is power of 3

def power3(n):
  if n == 0:
    return False
  while (n % 3 == 0):
    n = n / 3
  return True if n == 1 else False

class Power3:
  def __init__(self, input):
    self.next = None
    if input == 0:
      self.flag = False
    elif input == 1:
      self.flag = True
    else:
      if input % 3 == 0:
        self.next = Power3(input / 3)
      else:
        self.flag = False

  def check(self):
    if self.next is not None:
      return self.next.check()
    else:
      return self.flag

p = Power3(27)
print p.check()
p = Power3(25)
print p.check()
