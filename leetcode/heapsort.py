# heap sort: min heap.

class MinHeap:
  def __init__(self):
    self.heap = []

  def push(self, x):
    self.heap.append(x)
    index = len(self.heap) - 1
    while (index > 0):
      parent = (index / 2 - 1) if index % 2 == 0 else (index + 1) / 2 - 1
      if self.heap[parent] > self.heap[index]:
        t = self.heap[parent]
        self.heap[parent] = self.heap[index]
        self.heap[index] = t
        index = parent
      else:
        break

  def pop(self):
    if len(self.heap) == 1:
      minimum = self.heap.pop()
      return minimum
    else:
      minimum = self.heap[0]
      value = self.heap.pop()
      self.heap[0] = value
      index = 0
      while (True):
        l = 2 * (index + 1) - 1
        r = 2 * (index + 1)
        if (l <= len(self.heap)-1) and (r <= len(self.heap)-1):
          if self.heap[index] < self.heap[l] and self.heap[index] < self.heap[r]:
            break
          elif self.heap[l] < self.heap[index] and self.heap[l] < self.heap[r]:
            t = self.heap[index]
            self.heap[index] = self.heap[l]
            self.heap[l] = t
            index = l
          else:
            t = self.heap[index]
            self.heap[index] = self.heap[r]
            self.heap[r] = t
            index = r
        elif (l <= len(self.heap)-1):
          if self.heap[index] < self.heap[l]:
            break
          else:
            t = self.heap[index]
            self.heap[index] = self.heap[l]
            self.heap[l] = t
            index = l
        else:
          break
      return minimum

h = MinHeap()
h.push(5)
h.push(1)
h.push(2)
h.push(8)
h.push(4)
while (len(h.heap) > 0):
  m = h.pop()
  print m
