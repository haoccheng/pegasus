# connected component of undirected graph.
# input: set of edges.

def connected_component(edges):
  cluster = {}
  for (start, end) in edges:
    if start not in cluster and end not in cluster:
      c = start if start < end else end
      cluster[start] = c
      cluster[end] = c
    elif start not in cluster:
      c = start if start < cluster[end] else cluster[end]
      if c == start:
        for k, v in cluster.items():
          if v == cluster[end]:
            cluster[k] = c
      else:
        cluster[start] = c
    elif end not in cluster:
      c = end if end < cluster[start] else cluster[start]
      if c == end:
        for k, v in cluster.items():
          if v == cluster[start]:
            cluster[k] = c
      else:
        cluster[end] = c
    else:
      c = cluster[start] if cluster[start] < cluster[end] else cluster[end]
      u = cluster[start] if cluster[start] > cluster[end] else cluster[end]
      for k, v in cluster.items():
        if v == u:
          cluster[k] = c
  return cluster

print connected_component([(0,1), (1,2), (1,3), (4,5)])
