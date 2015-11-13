# check whether a positive number is a palindrome or not.
# 121 is palindrome, but 123 is not.

# constraint: try not to use additional storage like a buffer.

def palindrome(number):
  assert(number > 0)
  assert(isinstance(number, int))
  onum = number
  rnum = 0
  while (True):
    x = number / 10
    y = number % 10
    rnum = rnum * 10 + y
    if x > 0:
      number = x
    else:
      break
  return (onum == rnum)

def test():
  for number in [5, 123, 1234, 121, 123321, 12321, 12343321]:
    print 'number=%d palindrome=%d' % (number, palindrome(number))

test()
