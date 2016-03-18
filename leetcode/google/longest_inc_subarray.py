# longest increasing subarray.
# 1 5 4 2

# O(n2)

def longest_inc_subarray(input):
  scores = [0] * len(input)
  scores[0] = 1
  for i in range(1, len(input)):
    choice = 1
    for j in range(i):
      if input[i] > input[j]:
        choice = max(choice, scores[j]+1)
    scores[i] = choice
  print scores
  return max(scores)

print longest_inc_subarray([1, 5, 4, 2])
print longest_inc_subarray([1, 5, 4, 2, 3])
print longest_inc_subarray([10, 9, 2, 5, 3, 7, 101, 18])
