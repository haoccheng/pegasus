# Implement BigInt and addition.

class BigInt:
  def __init__(self, value=0):
    self.set_value(value)

  def set_value(self, value):
    s = ('%d' % value)
    self.buffer = (s[::-1]) # in reverse order.

  def set_buffer(self, buf):
    self.buffer = buf

  def add(self, value):
    buffer = ''
    carryover = 0
    overlap = min(len(self.buffer), len(value.buffer))
    for i in range(overlap):
      x = int(self.buffer[i])
      y = int(value.buffer[i])
      z = x + y + carryover
      if (z >= 10):
        buffer += (str(z - 10))
        carryover = 1
      else:
        buffer += (str(z))
        carryover = 0
    remain = self.buffer if (len(self.buffer) > len(value.buffer)) else value.buffer
    for i in range(overlap, len(remain)):
      x = int(remain[i])
      z = x + carryover
      if (z >= 10):
        buffer += (str(z - 10))
        carryover = 1
      else:
        buffer += (str(z))
        carryover = 0
    if carryover == 1:
      buffer += '1'
    ret = BigInt()
    ret.set_buffer(buffer)
    return ret

  def __str__(self):
    return self.buffer[::-1]

def test():
  for (xi, yi) in [(123, 123), (12, 18), (12, 98), (123, 9987)]:
    x = BigInt(xi)
    y = BigInt(yi)
    z = x.add(y)
    print xi, yi, xi+yi, z

test()
