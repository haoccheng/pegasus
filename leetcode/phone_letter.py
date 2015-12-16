# Given a digital string, return all possible letter combinations that the number could represent.
# 1:''
# 2:abc
# 3:def
# 4:gni
# 5:jkl
# 6:mno
# 7:pqrs
# 8:tuv
# 9:wxyz
# 0:' '
# digit: 23 -> [ad, ae, af..]

def phone_letter(digits):
  phone = {'1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz', '0':' '}
  if len(digits) == 1:
    hit = phone[digits]
    return list(hit)
  else:
    head = phone_letter(digits[0])
    tail = phone_letter(digits[1:])
    ret = [h+t for h in head for t in tail]
    return ret

print phone_letter('23')
