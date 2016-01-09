# permutation sequence
# [1,2,..n] return n! unique combination
# Given n/k, return the kth permutation sequence.
# n = 1-9 (inclusive).

def permute_base(prefix, numbers, start, target):
  if len(numbers) == 1:
    if start + 1 == target:
      return prefix + numbers
    else:
      raise RuntimeError('exception...')
  split_size = 1
  for i in range(1, len(numbers)):
    split_size *= i
  numbers = sorted(numbers)
  for i in range(len(numbers)):
    lower = start + i*split_size + 1
    upper = start + (i+1)*split_size
    if (lower <= target) and (target <= upper):
      prefix.append(numbers[i])
      numbers.pop(i)
      start = lower - 1
      break
  return permute_base(prefix, numbers, start, target)

def permute(n, k):
  prefix = []
  numbers = range(1, n+1)
  print permute_base(prefix, numbers, 0, k)

permute(3, 1)
permute(3, 6)
