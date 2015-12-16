# Given a non-negative number represented as an array of digits, plus one to the number.
# The digits are stored such that most significant digit is at the head of the list.

def plus_one(digits):
  carry = 1
  ret = []
  for i in range(len(digits)-1, -1, -1):
    v = digits[i]
    if carry + v == 10:
      ret.insert(0, 0)
      carry = 1
    else:
      ret.insert(0, carry+v)
      carry = 0
  if carry == 1:
    ret.insert(0, 1)
  return ret

print plus_one([1, 2, 3])
print plus_one([9, 9])
