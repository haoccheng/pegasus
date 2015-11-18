# Given number n, find the nth element in the Fibonacci sequence.
# f(n) = 0 if n = 0
#        1    n = 1
#        f(n-1)+f(n-2) if n > 1.

def fibonacci(n):
  f0 = 0
  f1 = 1
  if (n == 0):
    return f0
  elif (n == 1):
    return f1
  for i in range(1, n):
    fn = f1 + f0
    f0 = f1
    f1 = fn
  return f1

def fibonacci_recursive(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  elif n > 1:
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

for i in range(0, 10):
  print fibonacci_recursive(i) == fibonacci(i)

