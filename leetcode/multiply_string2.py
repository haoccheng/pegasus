# Given two numbers represented as strings, return mulplications of the numbers as string.
# numbers are arbitrary long and non-negative.

def multiply(num1, num2):
  result = [0] * (len(num1)+len(num2))
  for i in range(len(num1)):
    for j in range(len(num2)):
      zlen = len(num1)-1-i + len(num2)-1-j
      pos = len(result)-1 - zlen
      value = int(num1[i]) * int(num2[j])
      result[pos-1] += value / 10
      result[pos] += value % 10
  print result
  for i in range(len(result)-1, -1, -1):
    v = result[i]
    pos = i
    result[i] = 0
    while (v > 0):
      result[pos] += v % 10
      v = v / 10
      pos -= 1
  start = 0
  while (start < len(result)-1) and (result[start] == 0):
    start += 1
  return ''.join([str(e) for e in result[start:]])

#print multiply('123', '1')
#print multiply('123', '10')
#print multiply('123', '5')
#print multiply('0', '0')
print multiply('123', '456')
