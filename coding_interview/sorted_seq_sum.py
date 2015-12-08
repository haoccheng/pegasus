# Given an increasingly sorted array and a number s.
# Is there a pair of two numbers in the array whose sum is s.
# {1,2,4,7,11,15} target=15 -> (4,11)

def sorted_seq_sum(inputs, target):
  i = 0
  j = len(inputs) - 1
  while (i < j):
    vi = inputs[i]
    vj = inputs[j]
    s = vi + vj
    if s == target:
      return (vi, vj)
    elif s > target:
      j -= 1
    else:
      i += 1
  return None

def test():
  print sorted_seq_sum([1, 2, 4, 7, 11, 15], 15)
  print sorted_seq_sum([1, 2, 5, 7, 11, 15], 15)

test()
