# longest common prefix among an array of strings.

def longest_common_prefix(strs):
  prefix = None
  for s in strs:
    if prefix is None:
      prefix = s
    elif len(prefix) == 0:
      return prefix
    else:
      h = 0
      for i in range(min(len(s), len(prefix))):
        if (s[i] == prefix[i]):
          h += 1
        else:
          break
      prefix = prefix[:h]
  return prefix

print longest_common_prefix(['abc', 'ab'])
print longest_common_prefix(['abc', 'abcde'])
print longest_common_prefix(['abc', 'abcde', 'abcf'])
print longest_common_prefix(['abc', 'abcde', 'abcf', 'd'])
