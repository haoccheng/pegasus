# Given an integer array containing positive/negative numbers.
# Find the maximum sum its subarrays.
# Continuous numbers form a subarray of an array.
# {1,-2,3,10,-4,7,2,-5} -> {3,10,-4,7,2} = 18.

def great_sum(input):
  max_sum = input[0]
  acc_sum = input[0]
  for i in range(1, len(input)):
    value = input[i]
    # compute acc_sum
    c0 = value
    c1 = acc_sum + value
    if c1 > c0:
      acc_sum = c1
    else:
      acc_sum = c0
    # compute max_sum. Either previous max, or the new acc_sum.
    if acc_sum > max_sum:
      max_sum = acc_sum
  return max_sum

def test():
  print great_sum([1, -2, 3, 10, -4, 7, 2, -5])

test()

