def kth_minimium(data1, data2, K):
    if (len(data1) == 0) and (len(data2) == 0):
        return None
    elif len(data1) == 0:
        return data2[K] if K <= len(data2) - 1 else None
    elif len(data2) == 0:
        return data1[K] if K <= len(data1) - 1 else None
    elif (K < 0) or (K > len(data1) + len(data2) - 1):
        return None
    x1 = 0
    x2 = 0
    index = K
    while (x1 < len(data1) and x2 < len(data2)):
        if index == 0:
            return data1[x1] if data1[x1] <= data2[x2] else data2[x2]
        if data1[x1] <= data2[x2]:
            x1 += 1
        else:
            x2 += 1
        index -= 1
    if x1 < len(data1):
        return data1[x1 + index]
    else:
        return data2[x2 + index]
    
data1 = [0, 1, 3, 5, 7, 9]
data2 = [2, 4, 6, 8, 10, 11, 12]
for i in range(-1, 15):
  print kth_minimium(data1, data2, i)

data1 = []
data2 = []
print kth_minimium(data1, data2, 3)
