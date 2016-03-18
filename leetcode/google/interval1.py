# intervals are left close and right open.
# [1,3)
# implment a method to decide if two intervals have overlap.

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

def overlap(interval1, interval2):
  left = max(interval1.start, interval2.start)
  right = min(interval1.end, interval2.end)
  return True if left < right else False

print overlap(Interval(2,3), Interval(1,3))
print overlap(Interval(2,3), Interval(3,4))
print overlap(Interval(2,5), Interval(3,4))
