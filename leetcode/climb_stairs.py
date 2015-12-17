# climb stair case. It takes n step to reach top.
# Each time can either climb 1 or 2 steps. How many distinct ways can you climb to the top.

def climb_stairs_recursive(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  else:
    return climb_stairs(n-1) + climb_stairs(n-2)

def climb_stairs(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  else:
    h1 = 1
    h2 = 2
    for v in range(3, n+1):
      h = h1 + h2
      h1 = h2
      h2 = h
    return h2

for i in range(1, 10):
  print i, climb_stairs_recursive(i), climb_stairs(i)
