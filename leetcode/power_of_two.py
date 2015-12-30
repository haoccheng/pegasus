# Given an integer, determine if it is a power of two.

def power_of_two(n):
  if n <= 0:
    return False
  else:
    value = n
    while (value > 0):
      if value == 1:
        return True
      else:
        r = value % 2
        if r != 0:
          return False
        else:
          value = value / 2
    return True

print power_of_two(1)
print power_of_two(2)
print power_of_two(8)
print power_of_two(9)
