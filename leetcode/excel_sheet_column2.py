# excel sheet column number
# A->1
# B->2
# Z -> 26
# AA -> 27
# ..

def title_to_number(s):
  v = 0
  for c in s:
    v = v * 26 + (ord(c) - ord('A') + 1)
  return v

print title_to_number('A')
print title_to_number('Z')
print title_to_number('AA')
