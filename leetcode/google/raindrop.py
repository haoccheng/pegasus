# rain drop simulation
# Given length L, rain drop diameter D, each position equal probability to rain.
# simulate.

import random

class RainDrop:
  def __init__(self, length, diameter, num_drops):
    self.length = length
    self.diameter = diameter
    self.radius = self.diameter / 2.0
    self.num_drops = num_drops
    self.intervals = []
    self.pcover = 0.0

  def run(self):
    for i in range(self.num_drops):
      x = random.random() * self.length
      xl = max(0, x - self.radius)
      xu = min(self.length, x + self.radius)
      new_intervals = []
      for it in self.intervals:
        if xl is None:
          new_intervals.append(it)
        else:
          # it[0], it[1]
          # xl, xu
          if it[1] < xl:
            new_intervals.append(it)
          elif xu < it[0]:
            new_intervals.append((xl, xu))
            xl = None
          else:
            xl = min(it[0], xl)
            xu = max(it[1], xu)
      if xl is not None:
        new_intervals.append((xl, xu))
      self.intervals = new_intervals

  def compute_cover(self):
    cover = 0.0
    for (l, u) in self.intervals:
      cover += (u - l)
    self.pcover = cover * 100.0 / self.length

for i in range(1, 200, 20):
  rd = RainDrop(10, 1, i)
  rd.run()
  rd.compute_cover()
  print i, rd.pcover
