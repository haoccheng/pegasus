# Implement a function to check whether there is a path for a string in a matrix of characters.
# The path cannot enter the same cell twice.
#
# a b c e   -> bcced (yes)
# s f c s   -> abcd (no).
# a d e e

class Node:
  def __init__(self, x=None, y=None):
    self.child = []
    self.x = x
    self.y = y

def build_root(maze):
  root = Node()
  for i in range(len(maze)):
    for j in range(len(maze[i])):
      root.child.append(Node(i, j))
  return root

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

def evaluate(root, maze, path, visit, step):
  if (step == len(path)):
    return True
  for candidate in root.child:
    if (path[step] == maze[candidate.x][candidate.y]): # if match, explore
      visit[candidate.x][candidate.y] = step
      explore_neighbor(candidate, visit)
      hit = evaluate(candidate, maze, path, visit, step+1)
      if hit == True:
        return True
      visit[candidate.x][candidate.y] = -1 # non-subsequent path converge to a match.
  return False

def test():
  maze = [list('abce'), list('sfcs'), list('adee')]
  #path = 'bcced'
  path = 'abcd'
  visit = [[-1,-1,-1,-1], [-1,-1,-1,-1], [-1,-1,-1,-1]]
  root = build_root(maze)
  print evaluate(root, maze, path, visit, 0)
  print visit

test()
