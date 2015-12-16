# Given n non-negative integers a1, a2 .. an
# Each represent a point at coordinate ai.
# N vertical lines are drawn such that two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that it has the most water.

def max_area(height):
  li = 0
  ri = len(height) - 1
  candidate = None
  while (li < ri):
    lh = height[li]
    rh = height[ri]
    x = ri - li
    if lh > rh:
      mh = rh
      if candidate is None:
        candidate = (mh, x, mh*x)
      else:
        if (mh*x > candidate[2]):
          candidate = (mh, x, mh*x)
      ri -= 1
    else:
      mh = lh
      if candidate is None:
        candidate = (mh, x, mh*x)
      else:
        if (mh*x > candidate[2]):
          candidate = (mh, x, mh*x)
      li += 1
  return candidate

print max_area([3, 1, 2])
print max_area([4, 3, 5, 3, 4])
print max_area([4, 3, 5, 3, 3])
print max_area([4, 3, 5, 3, 2])

