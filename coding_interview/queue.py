# Design a queue with two stacks and implement enqueue/dequeue.

# queue: FIFO.
# stack: FILO.

class Stack:
  def __init__(self):
    self.queue = []
  def push(self, e):
    self.queue.append(e)
  def pop(self):
    return self.queue.pop()
  def empty(self):
    return (len(self.queue) == 0)

class Queue:
  def __init__(self):
    self.inorder = Stack()
    self.reverse = Stack()
  def enqueue(self, e):
    self.inorder.push(e)
  def dequeue(self):
    if (self.reverse.empty()):
      while (self.inorder.empty() == False):
        e = self.inorder.pop()
        self.reverse.push(e)
    if (not self.reverse.empty()):
      return self.reverse.pop()
    else:
      return None

def test():
  q = Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  print q.dequeue()
  print q.dequeue()
  q.enqueue(4)
  print q.dequeue()
  print q.dequeue()

test()
