# Given a string, determine if palindrome, consider only alphanumeric and ignore case.
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome. 

def is_palindrome(s):
  s = [e.lower() for e in s if e.isalnum()]
  i = 0
  j = len(s) - 1
  while (i < j):
    if s[i] == s[j]:
      i += 1
      j -= 1
    else:
      return False
  return True

print is_palindrome('A man, a plan, a canal: Panama')
print is_palindrome('race a car')
