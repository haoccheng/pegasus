# implement a function to replace each blank in a string with '%20'
# we are happy -> we%20are$20happy

def encode_blank(input):
  out = ''
  for s in input:
    if s == ' ':
      out += '%20'
    else:
      out += s
  return out

# additional constraint: replace on the initial string, avoid additional storage.
# Then, two pass.
# Pass 1: compute the number of spaces. This is to recognize what would be the end position after the replace.
# Pass 2: start backwards, move each character to the right position accordingly.

print encode_blank('we are happy')
print encode_blank('we are  happy')
print encode_blank(' we are  happy ')
