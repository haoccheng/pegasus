# determine if two recetangles overlap
# if multiple, use RTree kind bounding box; extend Rectangle class as composite/basic.

class Rectangle:
  def __init__(self, xl, xu, yl, yu):
    self.xl = xl
    self.xu = xu
    self.yl = yl
    self.yu = yu

  def overlap(rect1, rect2):
    # overlap in x and overlap in y
    oxl = max(rect1.xl, rect2.xl)
    oxu = min(rect1.xu, rect2.xu)
    oyl = max(rect1.yl, rect2.yl)
    oyu = min(rect1.yu, rect2.yu)
    if (oxl < oxu) and (oyl < oyu):
      return (oxl, oxu, oyl, oyu)
    else:
      return None
  overlap = staticmethod(overlap)

x = Rectangle(0, 2, 0, 1)
y = Rectangle(1, 3, 0.5, 1.5)
print Rectangle.overlap(x, y)
