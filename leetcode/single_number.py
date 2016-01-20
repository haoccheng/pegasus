# single number.
# In the array of integers, each element appears twice except one.

def single_number(numbers):
  value = 0
  for v in numbers:
    value = value ^ v
  print value

single_number([1, 2, 3, 2, 3])
single_number([1, 2, 3, 2, 3, 1, 4])
