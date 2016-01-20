# clone undirected graph.

def clone_base(node, cache):
  if node.label in cache:
    return cache[node.label]
  root = UndirectedGraphNode(node.label)
  cache[node.label] = root
  for c in node.neighbors:
    r = clone_base(c, cache)
    root.neighbors.append(r)
  return root

def clone(node):
  if node is None:
    return None
  cache = {}
  root = clone_base(node, cache)
  return root
