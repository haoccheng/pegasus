# determine if a sudoku is valid.
# The Sudoku board could be partially filled where empty cells are filled with character '.'
# A valid sudoku board (partially filled) is not necessarily solvable.

from collections import defaultdict

def is_valid_sudoku_block(input):
  count = defaultdict(int)
  for e in input:
    if e == '.':
      continue
    count[e] += 1
    if count[e] == 2:
      return False
  return True

def is_valid_sudoku(board): 
  # board: List[List[str]]
  for i in range(len(board)): # row
    if is_valid_sudoku_block(board[i]) == False:
      return False
  for i in range(len(board[0])): # column
    input = [row[i] for row in board]
    if is_valid_sudoku_block(input) == False:
      return False
  for i in range(3):
    for j in range(3):
      input = [board[m][n] for m in range((i*3+0), (i*3+3)) for n in range((j*3+0), (j*3+3))]
      if is_valid_sudoku_block(input) == False:
        return False
  return True

