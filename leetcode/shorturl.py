# simulate the URL shorterner.

def shorturl_base(prefix, suffix):
  if len(suffix) == 0:
    print prefix
    return
  c = suffix[0]
  if c in 'abcdefghijklmnopqrstuvwxyz':
    shorturl_base(prefix+c, suffix[1:])
    uc = chr(ord(c) - ord('a') + ord('A'))
    shorturl_base(prefix+uc, suffix[1:])
  else:
    shorturl_base(prefix+c, suffix[1:])

shorturl_base('', 'ab12cd')
