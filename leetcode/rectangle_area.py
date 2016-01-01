# https://leetcode.com/problems/rectangle-area/
# area of recentangle.

def compute_area(A, B, C, D, E, F, G, H):
  x11 = E if A < E else A
  y11 = H if D > H else D

  x12 = C if C < G else G
  y12 = H if D > H else D

  x21 = E if A < E else A
  y21 = B if B > F else F

  x22 = C if C < G else G
  y22 = B if B > F else F

  overlap = 0
  if (x12 > x11) and (y12 > y22):
    overlap = (x12 - x11) * (y12 - y22)
  total = (D-B)*(C-A) + (G-E)*(H-F) - overlap
  return total

