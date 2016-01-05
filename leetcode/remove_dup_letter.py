# https://leetcode.com/problems/remove-duplicate-letters/
# remove duplicate letters and return in lexicographical order.

def remove_dup(s):
  if len(s) == 0:
    return ''
  count = [0] * 26
  for c in s:
    count[ord(c)-ord('a')] += 1
  pos = 0
  for i in range(len(s)):
    if s[pos] > s[i]:
      pos = i
    count[ord(s[i])-ord('a')] -= 1
    if count[ord(s[i])-ord('a')] == 0:
      break
  remain = s[pos+1:]
  remain = remain.replace(s[pos], '')
  return s[pos] + remove_dup(remain)

print remove_dup('bcabc')
print remove_dup('cbacdcbc')
