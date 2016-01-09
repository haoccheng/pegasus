# word search in 2D board.

def exist(board, word):
  if len(word) == 0:
    return True
  for x in range(len(board)):
    for y in range(len(board[x])): # pick x/y as start point.
      if exist_base(board, word, x, y):
        return True
  return False

def exist_base(board, word, x, y):
  if len(word) == 0:
    return True
  if board[x][y] == word[0]:
    if len(word[1:]) == 0:
      return True
    curr_char = board[x][y]
    board[x][y] = ''
    if (x-1) >= 0 and exist_base(board, word[1:], x-1, y):
      return True
    if (x+1) <= len(board)-1 and exist_base(board, word[1:], x+1, y):
      return True
    if (y-1) >= 0 and exist_base(board, word[1:], x, y-1):
      return True
    if (y+1) <= len(board[x])-1 and exist_base(board, word[1:], x, y+1):
      return True
    board[x][y] = curr_char
  return False

board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
print exist(board, 'ABCCED')
board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
print exist(board, 'SEE')
board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
print exist(board, 'ABCB')
