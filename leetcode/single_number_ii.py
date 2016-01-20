# single number.
# In the array of integers, each element appears 3 times except one.

def single_number(numbers):
  state1 = 0
  state2 = 0
  for v in numbers:
    for i in range(32):
      mask = 1 << i
      vb = v & mask
      if vb > 0:
        s1b = state1 & mask
        s2b = state2 & mask
        if s1b == 0 and s2b == 0:
          state1 = state1 | mask
        elif s1b > 0 and s2b == 0:
          state1 = state1 & (~mask)
          state2 = state2 | mask
        elif s1b == 0 and s2b > 0:
          state1 = state1 & (~mask)
          state2 = state2 & (~mask)
  if state1 >= 2**31:
    state1 -= 2**32
  return state1

print single_number([1,1,1,2,2,2,20])
print single_number([2,2,2,3])
