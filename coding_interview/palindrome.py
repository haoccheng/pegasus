# check whether a positive number is a palindrome or not.
# 121 is palindrome, but 123 is not.

def pnum2str(number):
  assert(number > 0)
  assert(isinstance(number, int))
  s = ''
  while (True):
    x = number / 10
    y = number % 10
    s = str(y) + s
    if x > 0:
      number = x
    else:
      break
  return s

def palindrome(number):
  assert(number > 0)
  assert(isinstance(number, int))
  s = pnum2str(number)
  assert(len(s) > 0)
  start = 0
  end = len(s) - 1
  while (start < end):
    if s[start] == s[end]:
      start += 1
      end -= 1
    else:
      return False
  return True

def test():
  for number in [5, 123, 1234, 121, 123321, 12321, 12343321]:
    print 'number=%d palindrome=%d' % (number, palindrome(number))

test()
