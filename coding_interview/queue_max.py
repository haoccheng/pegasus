# Define a queue in which we can get a maximum value with a function max().
# The time complexity of max/push_back/pop_front are O(1).

class QueueMax:
  def __init__(self):
    self.queue = []
    self.max_queue = []
    self.index = 0

  def push_back(self, value):
    index = self.index
    self.queue.append((value, index))
    candidates = []
    for (mv, mi) in self.max_queue:
      if (value >= mv):
        break
      else:
        candidates.append((mv, mi))
    candidates.append((value, index))
    self.index += 1
    self.max_queue = candidates

  def max(self):
    if len(self.max_queue) > 0:
      return self.max_queue[0][0]
    else:
      return None

  def pop_front(self):
    if len(self.queue) == 0:
      return None
    e = self.queue[0]
    m = self.max_queue[0]
    self.queue.pop(0)
    if e[1] == m[1]:
      self.max_queue.pop(0)
    return e[0]

q = QueueMax()
q.push_back(4)
print q.max()
q.push_back(4)
q.pop_front()
print q.max()
q.push_back(3)
q.push_back(2)
print q.max()
q.pop_front()
print q.max()
q.pop_front()
print q.max()

