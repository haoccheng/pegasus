# two strings, one string has 1 extra character than the other;
# other than that, the two strings are identical.
# abc abcd
# abc abdc

def diff1c(str1, str2):
  for i in range(min(len(str1), len(str2))):
    if str1[i] == str2[i]:
      continue
    else:
      return i
  return max(len(str1), len(str2)) - 1

print diff1c('abc', 'abcd')
print diff1c('abc', 'abdc')

# if two strings are shuffle: either sort or hashmap.
