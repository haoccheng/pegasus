# https://leetcode.com/problems/rectangle-area/

def compute_area(A, B, C, D, E, F, G, H):
  x11 = A if A > E else E
  y11 = D if D < H else H

  x12 = C if C < G else G
  y12 = D if D < H else H

  x21 = A if A > E else E
  y21 = B if B > F else F

  x22 = C if C < G else G
  y22 = B if B > F else F

  if (x12 > x21) and (y12 > y21):
    return (x12 - x21) * (y12 - y21)
  else:
    return 0

