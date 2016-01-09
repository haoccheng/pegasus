# strstr()
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of the haystack.
#
# A few things I think about.
# bruteforce, use suffix tree, KMP.

def strstr(haystack, needle):
  if len(haystack) == 0 or len(needle) == 0:
    return -1
  elif len(needle) > len(haystack):
    return -1
  elif len(needle) == len(haystack):
    if needle == haystack:
      return 0
    else:
      return -1
  for i in range(len(haystack)-len(needle)+1):
    match = True
    for j in range(len(needle)):
      if haystack[i+j] == needle[j]:
        continue
      else:
        match = False
        break
    if match == True:
      return i
  return -1

print strstr('This is a simple string', 'simple')
print strstr('abababc', 'ababc')

