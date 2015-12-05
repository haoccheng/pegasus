# Given a string, find the length of longest substring without repeating characters.
# 'abcabcbb' is 'abc', 3.
# 'bbbbbb' is 'b', 1.

def length_longest_substring(s):
  # build index
  max_len = None
  cum_len = None
  # everytime attach a new character.
  # Two decision
  # What would be the new cum_len up till this position.
  # Could this new cum_len be the maximum length.
  index = {}
  for i in range(len(s)):
    c = s[i]
    if max_len is None:
      max_len = 1
      cum_len = 1
    else:
      if c in index:
        last_position = index[c]
        last_position_len = (i - last_position) # maximal possible length beyond last repeat.
        if (last_position_len > cum_len):
          cum_len = cum_len + 1
        elif (last_position_len == cum_len):
          cum_len = last_position_len
        else:
          cum_len = last_position_len
      else:
        cum_len = cum_len + 1
      if cum_len > max_len:
        max_len = cum_len
    index[c] = i
  return max_len

def test():
  print length_longest_substring('abcabcbb')
  print length_longest_substring('bbbbbb')

test()
