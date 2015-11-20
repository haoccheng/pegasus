# A robot starts at cell (0,0) of a grid with m rows and n columns.
# It can move to left, right, up, down one cell at a time.
# It cannot enter cells where the digit sum of row index and column index are greater than a given K.
# When k=18, the robot can reach (35,37) as 3+5+3+7 = 18. But not (35,38), 3+5+3+8=19.

class Node:
  def __init__(self, x=None, y=None):
    self.child = []
    self.x = x
    self.y = y

def explore_neighbor(root, visit):
  xlimit = len(visit)
  ylimit = len(visit[0])
  x = root.x
  y = root.y
  root.child = []
  if (x-1 >= 0):
    if (visit[x-1][y] == -1):
      root.child.append(Node(x-1,y))
  if (x+1 < xlimit):
    if (visit[x+1][y] == -1):
      root.child.append(Node(x+1,y))
  if (y-1 >= 0):
    if (visit[x][y-1] == -1):
      root.child.append(Node(x,y-1))
  if (y+1 < ylimit):
    if (visit[x][y+1] == -1):
      root.child.append(Node(x,y+1))

def evaluate(root, cutoff, visit, step):
  x = root.x
  y = root.y
  if (visit[x][y] == -1): # -1 means not yet explore; -2 means prohibited; otherwise means touch.
    # adjustment to keep it simple. assume x/y are single digit.
    if (x + y > cutoff):
      visit[x][y] = -2
      return step # same step as before.
    else:
      step += 1
      visit[x][y] = step
      # explore neighbors.
      explore_neighbor(root, visit)
      for candidate in root.child:
        step = evaluate(candidate, cutoff, visit, step)
      return step
  # Basically, if a node is visited (not available, set visit bit to step count).
  # At this stage, all the available neighbors from this node is also actually added to the exploration tree. 
  # So this guarantees the reach of all nodes if possible. 
  return step

def test():
  visit = [[-1,-1,-1,-1,-1,-1], [-1,-1,-1,-1,-1,-1], [-1,-1,-1,-1,-1,-1]]
  root = Node(0, 0)
  print evaluate(root, 5, visit, 0)
  print visit

test()
