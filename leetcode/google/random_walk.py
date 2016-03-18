# in x-axis, start from position 0.
# At each step, make a random choice to advance to left or to right.
# Question: after 1000 steps, what is the probability that it is still at the origin position 0.

class Combine:
  def __init__(self, N):
    self.perm = [1] * (N+1)
    self.select = [1] * (N+1)
    t = 1
    for i in range(1, len(self.perm)):
      t = t*i
      self.perm[i] = t
    t = 1
    for i in range(1, len(self.select)):
      t = t * (N - i + 1)
      self.select[i] = t

  def choose(self, K):
    return self.select[K] / self.perm[K]

#com = Combine(5)
#for i in range(0, 6):
#  print com.choose(i)

def odd(N):
  com = Combine(N)
  total = 0
  for c in range(N+1):
    total += com.choose(c)
  hit = com.choose(N/2)
  return hit * 1.0 / total

for i in [2, 4, 8, 16, 100, 1000]:
  print i, odd(i)
