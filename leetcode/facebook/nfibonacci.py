# nth fibonacci number % 10

def pattern():
  hit = {}
  a0 = 0
  a1 = 1
  hit[(a0, a1)] = 0
  for i in range(1, 200):
    print i, a0, a1
    a2 = a0 + a1
    a0 = a1
    a1 = a2

    b0 = a0 % 10
    b1 = a1 % 10
    if (b0, b1) in hit:
      print hit[(b0, b1)], i
      break
    hit[(b0, b1)] = i

pattern()

