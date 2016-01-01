class MinStack:
  def __init__(self):
    self.data = []
    self.min = []

  def push(self, x):
    if len(self.data) == 0:
      self.data.append(x)
      self.min.append(x)
    else:
      self.data.append(x)
      self.min.append(min(self.min[-1], x))

  def pop(self):
    self.data.pop()
    self.min.pop()

  def top(self):
    return self.data[-1]

  def get_min(self):
    return self.min[-1]
    
