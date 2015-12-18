# N gas station in a circular route: gas[i], cost[i]
# Start with an empty tank. Is it possible to finish the journey?
# Return the starting gas station's index if can travel around the circuit once, other -1.

def complete_circuit(gas, cost):
  tank = 0
  start = 0
  curr = 0
  while (True):
    tank = tank + gas[curr] - cost[curr]
    if tank >= 0:
      if (curr + 1) % (len(gas)) == start: # full cycle.
        return start
      curr = (curr + 1) % (len(gas))
    else:
      new_start = (curr + 1) % (len(gas))
      if new_start <= start:
        return -1
      else:
        start = new_start
        curr = start
        tank = 0

print complete_circuit([1, 2, 5], [1, 3, 1])
