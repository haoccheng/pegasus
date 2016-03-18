# connected component of undirected graph.

def dfs(graph, start, cluster, cluster_index):
  cluster[start] = cluster_index
  for i in range(len(graph[start])):
    if cluster[i] != -1:
      continue
    if graph[start][i] == 1:
      dfs(graph, i, cluster, cluster_index)

def connected_component(graph):
  cluster = [-1] * len(graph)
  for i in range(len(graph)):
    if cluster[i] != -1:
      continue
    dfs(graph, i, cluster, i)
  return cluster

graph = [[0, 1, 0, 0, 0, 0],
         [1, 0, 1, 1, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 1, 0]]
print connected_component(graph)
