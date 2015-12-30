# playing the nim game with friend.
# There is a heap of stones on the table, each time, one of your turns to remove 1 to 3 stones.
# The one who removes the last stone would be winner. Each one play with optimal strategy.
# e.g. if there are 4 stones in heap, you would never win the game.
# Write a function to decide whether you can win given number of stones in the heap.

def win_nim(n):
  if n <= 3:
    return True
  elif n == 4:
    return False
  elif n > 4:
    w1 = False
    w2 = True
    w3 = True
    w0 = None
    for i in range(5, n+1):
      w0 = True if ((w1 == False) or (w2 == False) or (w3 == False)) else False
      w3 = w2
      w2 = w1
      w1 = w0
    return w0

for i in range(4, 100):
  print i, win_nim(i)

# there are deterministic pattern.
# n % 4 == 0..
