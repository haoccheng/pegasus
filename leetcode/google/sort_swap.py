# Given a list of integers, sort them in a way that if output is s1, s2 .. sn
# then: s1 <= s2 >= s3 <= s4 ..

def sort_swap(input):
  input = sorted(input)
  start = 1
  while (start + 1 < len(input)):
    t = input[start]
    input[start] = input[start+1]
    input[start+1] = t
    start += 2
  return input

def validate(input):
  for i in range(1, len(input), 2):
    # input[i-1] <= input[i] >= input[i+1]
    if input[i] < input[i-1]:
      return False
    if i+1 < len(input) and input[i] < input[i+1]:
      return False
  for i in range(2, len(input), 2):
    # input[i-1] >= input[i] <= input[i+1]
    if input[i] > input[i-1]:
      return False
    if i+1 < len(input) and input[i] > input[i+1]:
      return False
  return True

ret = sort_swap(range(10))
print ret, validate(ret)

ret = sort_swap(range(10, -1, -1))
print ret, validate(ret)
