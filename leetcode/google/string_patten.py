# . -> arbitrary one character.
# * -> 0 or more arbitrary characters.
# youtube
# y.u.u.e --> true
# you*be --> true
# you.. --> false
# *u*u* --> true

def pattern(s, pt):
  if len(s) == 0 and len(pt) == 0:
    return True
  elif len(s) > 0 and len(pt) == 0:
    return False
  else:
    p1 = pt[0]
    if p1 == '.':
      return pattern(s[1:], pt[1:])
    elif p1 == '*':
      if pattern(s, pt[1:]) == True:
        return True
      if pattern(s[1:], pt) == True:
        return True
    else:
      if s[0] == pt[0]:
        return pattern(s[1:], pt[1:])
      else:
        return False
  return False

print pattern('youtube', 'y.u.u.e')
print pattern('youtube', 'you*be')
print pattern('youtube', 'you..')
print pattern('youtube', '*u*u*')
