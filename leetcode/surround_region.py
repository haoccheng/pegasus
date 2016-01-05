# surrounded region.
# https://leetcode.com/problems/surrounded-regions/

def dfs(board, x, y):
  if board[x][y] == 'X':
    return
  elif board[x][y] == 'B':
    return 
  elif board[x][y] == 'O':
    board[x][y] = 'B'
    if (x-1) >= 0:
      if board[x-1][y] == 'O':
        dfs(board, x-1, y)
    if (x+1 <= len(board)-1):
      if board[x+1][y] == 'O':
        dfs(board, x+1, y)
    if (y-1 >= 0):
      if board[x][y-1] == 'O':
        dfs(board, x, y-1)
    if (y+1 <= len(board[x])-1):
      if board[x][y+1] == 'O':
        dfs(board, x, y+1)

def bfs(board, x, y):
  if board[x][y] == 'O':
    queue = [(x,y)]
    while len(queue) > 0:
      (x,y) = queue.pop()
      board[x][y] = 'B'
      if (x-1) >= 0 and board[x-1][y] == 'O':
        queue.append((x-1, y))
      if (x+1 <= len(board)-1) and board[x+1][y] == 'O':
        queue.append((x+1, y))
      if (y-1 >= 0) and (board[x][y-1] == 'O'):
        queue.append((x, y-1))
      if (y+1 <= len(board[x])-1) and (board[x][y+1] == 'O'):
        queue.append((x, y+1))

def solve(board):
  for x in range(len(board)):
    if board[x][0] == 'O':
      #dfs(board, x, 0)
      bfs(board, x, 0)
    if board[x][-1] == 'O':
      #dfs(board, x, len(board[x])-1)
      bfs(board, x, len(board[x])-1)
  for y in range(0, len(board[0])):
    if board[0][y] == 'O':
      #dfs(board, 0, y)
      bfs(board, 0, y)
    if board[len(board)-1][y] == 'O':
      #dfs(board, len(board)-1, y)
      bfs(board, len(board)-1, y)
  
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 'B':
        board[i][j] = 'O'
      elif board[i][j] == 'O':
        board[i][j] = 'X'


board = ['XXXX', 'XOOX', 'XXOX', 'XOXX']
board = [list(e) for e in board]
print board
solve(board)
print board
