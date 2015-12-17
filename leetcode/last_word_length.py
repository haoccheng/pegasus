# Given a string consist of upper/lower case and empty space.
# Return the length of last word in string.
# If last word does not exist, return 0.

def last_word_length(s):
  last_wl = 0
  curr_wl = 0
  for e in s:
    if e == ' ':
      if curr_wl > 0:
        last_wl = curr_wl
      curr_wl = 0
    else:
      curr_wl += 1
  if curr_wl > 0:
    last_wl = curr_wl
  return last_wl

print last_word_length('hello world')
