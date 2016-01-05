# sqrt(x)

def sqrt2(x):
  if x < 0:
    return None
  elif x == 0:
    return 0
  elif (x >= 1) and (x <= 3):
    return 1
  start = 2
  end = x
  while (start <= end):
    mid = (int)((start + end) / 2)
    v = mid * mid
    if v == x:
      return mid
    elif v > x:
      end = mid - 1
    else:
      start = mid
    if (start == end):
      return start
    elif (start + 1 == end):
      if end * end <= x:
        return end
      else:
        return start

print sqrt2(1842248264)
print sqrt2(2147395599)
    
