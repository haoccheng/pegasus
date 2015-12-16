# https://leetcode.com/problems/zigzag-conversion/

def convert_bruteforce(s, numRows):
  if numRows == 1:
    return s
  board = []
  for i in range(numRows):
    row = [' '] * len(s)
    board.append(row)
  i = 0
  j = 0
  direction = 'down'
  for e in s:
    board[i][j] = e
    if direction == 'down':
      i = i + 1
      j = j
      if (i == numRows - 1):
        direction = 'up'
    else:
      i = i - 1
      j = j + 1
      if (i == 0):
        direction = 'down'
  ns = ''
  for i in range(len(board)):
    print board[i]
    ns += ''.join([e for e in board[i] if e != ' '])
  return ns

def convert(s, numRows):
  if numRows == 1:
    return s
  ns = ''
  loopa = 2 * numRows - 2
  loopb = 0
  for i in range(numRows):
    start = i
    if start > len(s)-1:
      break
    ns += s[start]
    while (start <= len(s)-1):
      if loopa > 0:
        start += loopa
        if start > len(s)-1:
          break
        ns += s[start]
      if loopb > 0:
        start += loopb
        if start > len(s)-1:
          break
        ns += s[start]
    loopa -= 2
    loopb += 2
  return ns

print convert_bruteforce('PAYPALISHIRING', 3)
print convert('PAYPALISHIRING', 3)
print convert_bruteforce('PAYPALISHIRING', 4)
print convert('PAYPALISHIRING', 4)
print convert_bruteforce('AB', 1)
print convert('AB', 1)

