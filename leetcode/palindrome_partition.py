# palindrome partition. 
# partition
# 'aab' -> a/a/b, aa/b

def partition(input, cache):
  if len(input) == 0:
    return [[]]
  elif input in cache:
    return cache[input]
  else:
    parts = []
    for i in range(len(input)):
      start = 0
      end = i
      check = True
      while (start < end):
        if input[start] != input[end]:
          check = False
          break
        start += 1
        end -= 1
      if check == True:
        prefix = input[:i+1]
        ret = partition(input[i+1:], cache)
        parts += [[prefix]+e for e in ret]
    if len(parts) > 0:
      cache[input] = parts
      return parts
    else:
      return []

cache = {}
#print partition('aab', cache)
print partition('aabaac', cache)

