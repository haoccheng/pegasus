# count the number of prime numbers less than a non-negative number, n.

def count_prime(n):
  memory = [1] * (n)
  memory[0] = 0
  i = 2
  while (i*i < n):
    if memory[i] == 0:
      i += 1
      continue
    j = i*i
    while (j < n):
      memory[j] = 0
      j += i
    i += 1
  return sum(memory)

#count_prime(20)
#print count_prime(999983)
print count_prime(2)
  
