# word ladder II: all shortest transformation sequences.

class Node:
  def __init__(self, source):
    self.source = source
    self.branch = []

def ladder(source, target, words):
  if source == target:
    return [target]
  root = Node(source)
  queue = [root]
  exist = 0
  while len(queue) > 0:
    for node in queue:
      s0 = node.source
      for i in range(len(s0)):
        for c in 'abcdefghijklmnopqrstuvwxuz':
          if c == s0[i]:
            continue
          s1 = s0[:i] + c + s0[i+1:]
          if s1 == target:
            node.branch.append(Node(s1))
            exist += 1
          elif s1 in words:
            node.branch.append(Node(s1))
    if exist > 0:
      break
    next_queue = []
    for node in queue:
      next_queue += node.branch
    queue = next_queue
  if exist == 0:
    return []
  path = []
  dfs_traversal(root, target, path)

def dfs_traversal(root, target, path):
  if root.source == target:
    path.append(target)
    print path
    path.pop()
  else:
    path.append(root.source)
    for c in root.branch:
      dfs_traversal(c, target, path)
    path.pop()

ladder('hit', 'cog', set(['hot', 'dot', 'dog', 'lot', 'log']))
