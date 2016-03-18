# string compressor that turn 123abkkkkkc to 123ab5xkc.

def compress(input):
  prev_char = None
  prev_count = 0
  output = ''
  for c in input:
    if prev_char is None:
      prev_char = c
      prev_count = 1
    elif prev_char == c:
      prev_count += 1
    else:
      if prev_count == 1:
        output += prev_char
      else:
        output += str(prev_count) + 'x' + prev_char
      prev_char = c
      prev_count = 1
  if prev_count == 1:
    output += prev_char
  else:
    output += str(prev_count) + 'x' + prev_char
  return output

print compress('123abkkkkkc')
