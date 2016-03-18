# implement LRU.

class ListNode:
  def __init__(self):
    self.prev = None
    self.next = None
    self.val = None

class LRU:
  def __init__(self, limit):
    self.limit = limit
    self.cache = {}
    self.start = ListNode() # dummy head.
    self.end = self.start

  def set(self, key, value):
    if key not in self.cache:
      if self.limit - len(self.cache) == 0:
        lru = self.start.next
        del self.cache[lru.val]
        self.start.next = lru.next
        if lru.next is not None:
          lru.next.prev = self.start
      n = ListNode()
      n.val = key
      n.prev = self.end
      self.end.next = n
      self.end = n
      self.cache[key] = (value, n)
    else:
      (prev_value, it) = self.cache[key]
      if it.next is not None:
        it.prev.next = it.next
        it.next.prev = it.prev
        it.prev = self.end
        it.next = None
        self.end.next = it
        self.end = it
      self.cache[key] = (value, it)

  def get(self, key):
    if key not in self.cache:
      return -1
    (value, it) = self.cache[key]
    self.set(key, value)
    return value

#lru = LRU(10)
#for v in range(20):
#  lru.push((v, v))
#  lru.get(0)
#print lru.cache.keys()

lru = LRU(10)
lru.set(10,13)
lru.set(3,17)
lru.set(6,11)
lru.set(10,5)
lru.set(9,10)
lru.get(13)
lru.set(2,19)
lru.get(2)
lru.get(3)
lru.set(5,25)
lru.get(8)
lru.set(9,22)
lru.set(5,5)
lru.set(1,30)
lru.get(11)
lru.set(9,12)
lru.get(7)
lru.get(5)
lru.get(8)
lru.get(9)
lru.set(4,30)
lru.set(9,3)
lru.get(9)
lru.get(10)
lru.get(10)
lru.set(6,14)
lru.set(3,1)
lru.get(3)
lru.set(10,11)
lru.get(8)
lru.set(2,14)
lru.get(1)
lru.get(5)
lru.get(4)
lru.set(11,4)
lru.set(12,24)
lru.set(5,18)
lru.get(13)
lru.set(7,23)
lru.get(8)
lru.get(12)
lru.set(3,27)
lru.set(2,12)
lru.get(5)
lru.set(2,9)
lru.set(13,4)
lru.set(8,18)
lru.set(1,7)
lru.get(6)
lru.set(9,29)
lru.set(8,21)
lru.get(5)
lru.set(6,30)
lru.set(1,12)
lru.get(10)
lru.set(4,15)
lru.set(7,22)
lru.set(11,26)
lru.set(8,17)
lru.set(9,29)
lru.get(5)
lru.set(3,4)
lru.set(11,30)
lru.get(12)
lru.set(4,29)
lru.get(3)
lru.get(9)
lru.get(6)
lru.set(3,4)
lru.get(1)
lru.get(10)
lru.set(3,29)
lru.set(10,28)
lru.set(1,20)
lru.set(11,13)
lru.get(3)
lru.set(3,12)
lru.set(3,8)
lru.set(10,9)
lru.set(3,26)
lru.get(8)
lru.get(7)
lru.get(5)
lru.set(13,17)
lru.set(2,27)
lru.set(11,15)
lru.get(12)
lru.set(9,19)
lru.set(2,15)
lru.set(3,16)
lru.get(1)
lru.set(12,17)
lru.set(9,1)
lru.set(6,19)
lru.get(4)
lru.get(5)
lru.get(5)
lru.set(8,1)
lru.set(11,7)
lru.set(5,2)
lru.set(9,28)
lru.get(1)
lru.set(2,2)
lru.set(7,4)
lru.set(4,22)
lru.set(7,24)
lru.set(9,26)
lru.set(13,28)
lru.set(11,26)
