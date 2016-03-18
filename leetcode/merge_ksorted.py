# merge k sorted lists.

class MinHeap:
  def __init__(self):
    self.heap = [] # (value, ith array, jth position at ith array)

  def empty(self):
    return True if len(self.heap) == 0 else False

  def pop(self):
    head = self.heap[0]
    if len(self.heap) == 1:
      self.heap.pop()
    else:
      tail = self.heap.pop()
      i = 0
      self.heap[i] = tail
      while (True):
        x = (i + 1) * 2 - 1
        y = (i + 1) * 2
        if (x <= len(self.heap) - 1) and (y <= len(self.heap) - 1):
          hi = self.heap[i]
          hx = self.heap[x]
          hy = self.heap[y]
          if (hi[0] <= hx[0]) and (hi[0] <= hy[0]):
            break
          elif (hx[0] <= hi[0]) and (hx[0] <= hy[0]):
            self.heap[i] = hx
            self.heap[x] = hi
            i = x
          else:
            self.heap[i] = hy
            self.heap[y] = hi
            i = y
        elif (x <= len(self.heap) - 1):
          hi = self.heap[i]
          hx = self.heap[x]
          if (hi[0] <= hx[0]):
            break
          else:
            self.heap[i] = hx
            self.heap[x] = hi
            i = x
        else:
          break
    return head

  def push(self, item):
    self.heap.append(item)
    if len(self.heap) > 1:
      x = len(self.heap) - 1
      while (True):
        i = (x + 1) / 2 - 1
        hx = self.heap[x]
        hi = self.heap[i]
        if hx[0] >= hi[0]:
          break
        else:
          self.heap[x] = hi
          self.heap[i] = hx
          x = i
        if x == 0:
          break

def merge_ksorted(data):
  heap = MinHeap()
  for i in range(len(data)):
    if len(data[i]) > 0:
      heap.push((data[i][0], i, 0))
  while heap.empty() == False:
    (value, i, j) = heap.pop()
    print value
    if j + 1 <= len(data[i])-1:
      heap.push((data[i][j+1], i, j+1))

merge_ksorted([[1, 3, 5, 7], [2, 4], [6, 8], [9, 10]])

