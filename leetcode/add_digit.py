# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

def add_digit(num):
  if num == 0:
    return 0
  v = num % 9
  return 9 if v == 0 else v

print add_digit(38)
