# given two sorted arrays, denoted as array1 and array2; merge.
# suppose there is sufficient vacant memory at end of array1.

def merge(array1, array2):
  e1 = len(array1) - 1
  e2 = len(array2) - 1
  for i in range(len(array2)):
    array1.append(0)
  em = e1 + e2 + 1
  while (e1 >= 0) and (e2 >= 0):
    if array1[e1] > array2[e2]:
      array1[em] = array1[e1]
      e1 -= 1
    else:
      array1[em] = array2[e2]
      e2 -= 1
    em -= 1
  while (e2 >= 0):
    array1[em] = array2[e2]
    em -= 1
    e2 -= 1
  return array1

def test():
  print merge([1, 2, 3], [4, 5, 6])
  print merge([1, 3, 5], [2, 4, 6])
  print merge([7, 8, 9], [2, 4, 6])

test()
