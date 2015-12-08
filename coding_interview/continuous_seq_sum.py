# Given a positive value s, print all sequences with continuous numbers
# (with two numbers at least) whose sum is s.
# input=15
# 3 sequences: 1~5, 4~6, 7~8

# This can be solved numerically.

def compute_k_parts(target, k):
  # k * x + (k-1)k/2
  offset = (k - 1) * k / 2
  r = target - offset
  if r < 0:
    return None
  mod = r % k
  if mod == 0:
    x = r / k
    ret = []
    for i in range(k):
      ret.append(x + i)
    return ret
  return []

def continuous_seq_sum(target):
  part = 1
  while (True):
    part += 1
    r = compute_k_parts(target, part)
    if r is None:
      break
    if len(r) == 0:
      continue
    print r

continuous_seq_sum(15)
