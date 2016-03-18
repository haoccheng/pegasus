# serialize a list of strings; and deserialize.

# format
# [1 byte:length of length][variable byte:length of string][variable byte:string]
# or use escape.
class Encoder:
  def __init__(self):
    1

  def encode(self, input):
    ret = ''
    for s in input:
      slen = len(s)
      sslen = len(str(slen))
      assert(sslen > 0 and sslen <= 255)
      b1 = chr(sslen)
      ret += (b1 + str(slen) + s)
    return ret

  def decode(self, input):
    ret = []
    start = 0
    while (start < len(input)):
      b1 = ord(input[start])
      slen = int(input[(start+1):(start+1+b1)])
      s = input[(start+1+b1):(start+1+b1+slen)]
      ret.append(s)
      start = start + 1 + b1 + slen
    return ret

enc = Encoder()
ret = enc.encode(['hello', 'world'])
print enc.decode(ret)
ret = enc.encode(['a', '', '', 'b'])
print enc.decode(ret)
ret = enc.encode(['abc', 'abcdefghijklmnopqrstuvwxyz'])
print enc.decode(ret)
